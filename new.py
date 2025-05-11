import streamlit as st
import json
import os
import textwrap
from datetime import datetime
import numpy as np
from collections import defaultdict

# --- Constants ---
DB_PATH = r"C:\Users\shrut\Downloads\akinator\revised\char.json"
STATS_PATH = "game_stats.json"
Q_TABLE_PATH = "q_table.json"
MAX_QUESTIONS = 7
LEARNING_RATE = 0.1
DISCOUNT_FACTOR = 0.9
EXPLORATION_RATE = 0.1

# --- Load and Save Functions ---
def load_db():
    if os.path.exists(DB_PATH):
        with open(DB_PATH, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def save_db(db):
    with open(DB_PATH, 'w', encoding='utf-8') as f:
        json.dump(db, f, indent=2, ensure_ascii=False)

def load_stats():
    if os.path.exists(STATS_PATH):
        with open(STATS_PATH, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def save_stats(stats):
    with open(STATS_PATH, 'w', encoding='utf-8') as f:
        json.dump(stats, f, indent=2, ensure_ascii=False)

def load_q_table():
    if os.path.exists(Q_TABLE_PATH):
        with open(Q_TABLE_PATH, 'r', encoding='utf-8') as f:
            raw_data = json.load(f)
            # Convert string keys back to tuples
            q_table = defaultdict(lambda: defaultdict(float))
            for state_str, actions in raw_data.items():
                # Convert string representation of tuple back to actual tuple
                state_tuple = eval(state_str)
                for action, value in actions.items():
                    q_table[state_tuple][action] = value
            return q_table
    return defaultdict(lambda: defaultdict(float))

def save_q_table(q_table):
    # Convert tuple keys to strings for JSON serialization
    serializable_dict = {}
    for state, actions in q_table.items():
        state_str = str(state)  # Convert tuple to string
        serializable_dict[state_str] = dict(actions)
    
    with open(Q_TABLE_PATH, 'w', encoding='utf-8') as f:
        json.dump(serializable_dict, f, indent=2, ensure_ascii=False)

# --- Q-Learning Functions ---
def get_state_key(answers):
    return tuple(sorted(answers.items()))

def get_reward(correct_guess, num_questions):
    if correct_guess:
        return 10.0 - (num_questions * 0.5)  # Reward for correct guess, penalize for more questions
    return -5.0  # Penalty for wrong guess

def select_question(q_table, state, available_traits, exploration_rate):
    if np.random.random() < exploration_rate:
        return np.random.choice(available_traits)
    
    state_key = get_state_key(state)
    q_values = {trait: q_table[state_key][trait] for trait in available_traits}
    return max(q_values.items(), key=lambda x: x[1])[0]

def update_q_value(q_table, state, action, reward, next_state):
    state_key = get_state_key(state)
    next_state_key = get_state_key(next_state)
    
    # Get max Q-value for next state
    next_max_q = max(q_table[next_state_key].values()) if q_table[next_state_key] else 0
    
    # Update Q-value using Q-learning formula
    current_q = q_table[state_key][action]
    new_q = current_q + LEARNING_RATE * (reward + DISCOUNT_FACTOR * next_max_q - current_q)
    q_table[state_key][action] = new_q

# --- Scoring Function ---
def score_candidates(db, answers):
    scores = {}
    for char in db:
        score = 0
        for k, v in answers.items():
            if k in char:
                score += 1 if char[k] == v else -0.5
        scores[char['name']] = score
    return sorted(scores.items(), key=lambda x: -x[1])

# --- Streamlit App ---
st.set_page_config(page_title="Akinator Lite", layout="wide")
st.title("Akinator Lite - Think of a Character!")

# Load database and Q-table
db = load_db()
if not db:
    st.error("Database empty. Please add characters first.")
    st.stop()

q_table = load_q_table()

# --- Display Character Grid (Mental Pick Only) ---
st.subheader("Think of a Character from the List Below")
st.markdown("Pick any one of these characters in your **mind**, then scroll down to answer the questions. I'll try to guess who you're thinking of!")

cols = st.columns(8)
characters = sorted([c["name"] for c in db])

for i, name in enumerate(characters):
    wrapped_name = "<br>".join(textwrap.wrap(name, width=14))
    with cols[i % 8]:
        st.markdown(
            f"""
            <div style="
                background-color: #0e1117;
                border: 1px solid #00bfff;
                border-radius: 8px;
                padding: 6px 8px;
                margin-bottom: 8px;
                text-align: center;
                font-size: 14px;
                min-height: 50px;
                color: #00bfff;">
                {wrapped_name}
            </div>
            """,
            unsafe_allow_html=True
        )

# --- Setup ---
traits = [k for k in db[0].keys() if k != "name"]
if "answers" not in st.session_state:
    st.session_state.answers = {}
if "step" not in st.session_state:
    st.session_state.step = 0
if "finished" not in st.session_state:
    st.session_state.finished = False
if "available_traits" not in st.session_state:
    st.session_state.available_traits = traits.copy()

# --- Ask Questions ---
if not st.session_state.finished:
    if st.session_state.step < min(MAX_QUESTIONS, len(traits)):
        # Select question using Q-learning
        current_trait = select_question(
            q_table,
            st.session_state.answers,
            st.session_state.available_traits,
            EXPLORATION_RATE
        )
        
        ans = st.radio(
            f"Q{st.session_state.step + 1}: Does your character have the trait: **{current_trait}**?",
            ["Yes", "No"],
            key=f"q{current_trait}"
        )
        
        if st.button("Submit", key=f"submit_{st.session_state.step}"):
            # Update state
            old_state = st.session_state.answers.copy()
            st.session_state.answers[current_trait] = (ans == "Yes")
            st.session_state.available_traits.remove(current_trait)
            st.session_state.step += 1
            
            # Update Q-table if we have enough information
            if len(old_state) > 0:
                update_q_value(
                    q_table,
                    old_state,
                    current_trait,
                    0,  # Intermediate reward
                    st.session_state.answers
                )
            
            if st.session_state.step >= MAX_QUESTIONS:
                st.session_state.finished = True
            st.rerun()
    else:
        st.session_state.finished = True

# --- Final Guess ---
if st.session_state.finished:
    st.subheader("My Guess:")
    top_scores = score_candidates(db, st.session_state.answers)
    if top_scores and top_scores[0][1] > 0:
        st.success(f"I guess your character is: **{top_scores[0][0]}**!")
        guessed = top_scores[0][0]
        correct_guess = True
    else:
        st.error("I couldn't guess! Want to teach me?")
        guessed = None
        correct_guess = False

    # Update Q-table with final reward
    if len(st.session_state.answers) > 0:
        update_q_value(
            q_table,
            st.session_state.answers,
            list(st.session_state.answers.keys())[-1],
            get_reward(correct_guess, len(st.session_state.answers)),
            st.session_state.answers
        )
        save_q_table(q_table)

    # --- Teach New Character ---
    st.markdown("###  Teach Me")
    new_name = st.text_input("Who was your character?")
    if new_name:
        new_traits = {}
        for trait in traits:
            new_traits[trait] = st.radio(f"{trait} for {new_name}?", ["Yes", "No"], key=f"teach_{trait}_{new_name}") == "Yes"
        if st.button("Add Character"):
            if any(c['name'].lower() == new_name.lower() for c in db):
                st.warning("Character already exists.")
            else:
                db.append({"name": new_name, **new_traits})
                save_db(db)
                st.success(f"Added **{new_name}** to my brain!")

    # --- Save Stats ---
    stats = load_stats()
    stats.append({
        "timestamp": datetime.now().isoformat(),
        "answers": st.session_state.answers,
        "guess": guessed,
        "correct": correct_guess,
        "questions_asked": len(st.session_state.answers)
    })
    save_stats(stats)

    # --- Show Stats ---
    if st.checkbox("Show previous game stats"):
        st.json(stats)

# --- Restart Game ---
if st.button("🔄 Restart Game"):
    st.session_state.answers = {}
    st.session_state.step = 0
    st.session_state.finished = False
    st.session_state.available_traits = traits.copy()
    st.rerun()
