import json
import os
import random
import time
from datetime import datetime

import streamlit as st
import pandas as pd
from sklearn.tree import DecisionTreeClassifier, _tree

# --- Constants & Paths ---
DB_PATH = "character_sample_20.json"
STATS_PATH = "game_stats.json"

# --- Load or initialize database ---
def load_db():
    if not os.path.exists(DB_PATH):
        with open(DB_PATH, 'w') as f:
            json.dump([], f)
    with open(DB_PATH, 'r') as f:
        return json.load(f)

def save_db(db):
    with open(DB_PATH, 'w') as f:
        json.dump(db, f, indent=2)

# --- Load or initialize stats ---
def load_stats():
    if not os.path.exists(STATS_PATH):
        return []
    with open(STATS_PATH, 'r') as f:
        return json.load(f)

def save_stats(stats):
    with open(STATS_PATH, 'w') as f:
        json.dump(stats, f, indent=2)

# --- Build decision tree for optimal questions ---
@st.cache_data
def train_tree(db):
    df = pd.DataFrame(db)
    X = df.drop(columns=["name"])
    y = df["name"]
    clf = DecisionTreeClassifier(criterion='entropy', random_state=42)
    clf.fit(X, y)
    return clf, df.columns.tolist()

# --- Tree traversal to get question order ---
def traverse_tree(clf, feature_names):
    tree = clf.tree_
    questions = []
    def recurse(node):
        if tree.feature[node] != _tree.TREE_UNDEFINED:
            feat = feature_names[tree.feature[node]]
            questions.append(feat)
            recurse(tree.children_left[node])
            recurse(tree.children_right[node])
    recurse(0)
    # remove duplicates, preserve order
    seen = set(); ordered = []
    for q in questions:
        if q not in seen:
            seen.add(q)
            ordered.append(q)
    return ordered

# --- Probabilistic scoring fallback ---
def score_candidates(db, answers):
    scores = {c['name']: 0 for c in db}
    for char in db:
        name = char['name']
        for feat, ans in answers.items():
            scores[name] += (1 if char.get(feat) == ans else -1)
    return sorted(scores.items(), key=lambda x: -x[1])

# --- Streamlit UI ---
st.title("🎮 Shruti's Enhanced Akinator")

# Load data
db = load_db()
st.sidebar.header("Game Settings")
max_questions = st.sidebar.slider("Max Questions", 3, 12, 8)
timed_mode = st.sidebar.checkbox("Timed Mode (30s)")

# Initialize session state
if 'start_time' not in st.session_state:
    st.session_state.start_time = None
if 'answers' not in st.session_state:
    st.session_state.answers = {}
if 'asked' not in st.session_state:
    st.session_state.asked = []
if 'step' not in st.session_state:
    st.session_state.step = 0

tree, features = train_tree(db)
question_order = traverse_tree(tree, features)

# New game helper
def new_game():
    st.session_state.start_time = time.time() if timed_mode else None
    st.session_state.answers = {}
    st.session_state.asked = []
    st.session_state.step = 0
    st.rerun()  # Changed from st.experimental_rerun()

if st.sidebar.button("Restart Game"):
    new_game()

# Show characters
st.markdown("**Think of one of these characters:**")
for c in db:
    st.write(f"- {c['name']}")

# Timer
if timed_mode and st.session_state.start_time:
    elapsed = time.time() - st.session_state.start_time
    remaining = max(0, 30 - int(elapsed))
    st.progress(remaining / 30)
    st.write(f"Time left: {remaining}s")
    if remaining == 0:
        st.warning("⏰ Time's up!")
        st.session_state.step = max_questions

# Ask questions
if st.session_state.step < max_questions:
    if st.session_state.step < len(question_order):
        feat = question_order[st.session_state.step]
        ans = st.radio(f"Q{st.session_state.step+1}: Is your character '{feat}'?", ["Yes", "No"], key=feat)
        if st.button("Submit", key=f"sub_{st.session_state.step}"):
            st.session_state.answers[feat] = (ans == "Yes")
            st.session_state.asked.append(feat)
            st.session_state.step += 1
            st.rerun()  # Changed from st.experimental_rerun()
else:
    # Filter exact
    candidates = [c for c in db if all(c.get(f)==v for f,v in st.session_state.answers.items())]
    if len(candidates)==1:
        st.success(f"🧠 I got it! **{candidates[0]['name']}**")
        guessed = candidates[0]['name']
    elif candidates:
        st.info("🤔 Multiple matches—top by score:")
        top = score_candidates(db, st.session_state.answers)[:3]
        for name, sc in top:
            st.write(f"- {name} (score {sc})")
        guessed = top[0][0]
    else:
        st.error("❌ No match found.")
        guessed = None

    # Teach new
    new_name = st.text_input("If I was wrong, who were you thinking of?", key="teach_name")
    if new_name:
        new_feats = {}
        for feat in features:
            new_feats[feat] = st.radio(f"Is {new_name} '{feat}'?", ["Yes","No"], key=f"teach_{feat}")=="Yes"
        if st.button("Add to DB"):
            db.append({"name": new_name, **new_feats})
            save_db(db)
            st.success(f"Added **{new_name}**!")

    # Save stats
    stats = load_stats()
    stats.append({
        "timestamp": datetime.now().isoformat(),
        "questions": st.session_state.step,
        "result": guessed
    })
    save_stats(stats)

    if st.checkbox("Show past stats"):
        st.table(pd.DataFrame(stats))

    st.audio("success.wav")