Sure! Below is the **continued and completed version** of your `README.md`, with everything explained in a clear, complete way.

---

````markdown
# 🧠 Akinator_MindGame

Akinator_MindGame is a lightweight, interactive guessing game built using **Streamlit** and **Q-learning**. You mentally choose a character from a list, answer yes/no trait-based questions, and the app tries to guess your character based on what it has learned. If it fails, you can teach it!

---

## 📌 Features

- 🎮 Interactive trait-based guessing game  
- 🧠 Reinforcement learning with Q-learning  
- 🔄 Learns from every game session  
- 🧑‍🏫 Add new characters with traits dynamically  
- 📊 View previous game stats  
- 💾 Local JSON storage for data persistence  

---

## 🚀 How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Akinator_MindGame.git
cd Akinator_MindGame
````

### 2. Install Required Libraries

Make sure Python 3.7 or higher is installed.

Then, install the dependencies:

```bash
pip install streamlit numpy
```

> Optionally, create a virtual environment first:
>
> ```bash
> python -m venv env
> source env/bin/activate  # On Windows: env\Scripts\activate
> ```

### 3. Run the Application

Launch the app with:

```bash
streamlit run akinator_app.py
```

The app will open in your browser at `http://localhost:8501`.

---

## 📁 Project Structure

```
Akinator_MindGame/
│
├── akinator_app.py         # Main Streamlit application
├── char.json               # Character database with traits
├── q_table.json            # Q-values for state-action learning
├── game_stats.json         # Logs for previous game sessions
└── README.md               # Project documentation
```

---

## 🧠 How It Works

1. You are shown a list of characters.
2. You **mentally choose one** character from the list.
3. The app will ask you up to **7 yes/no questions** about traits.
4. Based on your answers, it will **guess the character**.
5. If it fails, you can **teach it** the correct character and its traits.
6. The model uses **Q-learning** to improve over time.

---

## 🧪 Q-Learning Logic

Q-learning is a reinforcement learning algorithm used here to select the best questions to ask based on past outcomes.

* **State**: A dictionary of known answers so far (e.g., `{has_hat: True, brave: False}`)
* **Action**: A new trait to ask about (e.g., `"has_glasses"`)
* **Reward**:

  * `10 - 0.5 × num_questions` → if guess is correct
  * `-5` → if guess is incorrect

### Parameters

* **Learning Rate (α)** = `0.1`
* **Discount Factor (γ)** = `0.9`
* **Exploration Rate (ε)** = `0.1` (10% chance of random trait to explore new paths)

The model updates Q-values with:

```python
Q(s,a) ← Q(s,a) + α × [r + γ × max(Q(s',a')) - Q(s,a)]
```

---

## 🧬 Example Character Entry in `char.json`

```json
{
  "name": "Iron Man",
  "has_suit": true,
  "is_billionaire": true,
  "flies": true,
  "has_glasses": false
}
```

You can add characters manually, or through the app interface when the model guesses incorrectly.

---

## 📊 Game Stats

After each round, the game logs useful details in `game_stats.json`, including:

* Your answers
* The app’s guess
* Whether the guess was correct
* Number of questions used
* Timestamp of the session

These stats are shown in-app when you enable the checkbox **"Show previous game stats"**.

---

## 🔁 Restarting or Resetting

To restart the game during a session, click the **"🔄 Restart Game"** button in the app.

To reset the model and start fresh (clear all saved data):

```bash
del char.json q_table.json game_stats.json  # On Windows
rm char.json q_table.json game_stats.json  # On Mac/Linux
```

---

## 🧰 Tips for Best Experience

* Start with a few manually added characters for better guessing.
* The model gets smarter the more you play and teach.
* Avoid traits that are too vague or too specific.

---

## 👩‍💻 Contributing

If you'd like to add features or fix bugs:

1. Fork the repository
2. Create a new branch (`git checkout -b feature-name`)
3. Make your changes
4. Commit and push (`git push origin feature-name`)
5. Submit a pull request

---

## 📄 License

This project is open source and available under the [MIT License](https://opensource.org/licenses/MIT).

---

## 🙋‍♀️ Created by

**Shruti Brahma**
Made with ❤️ to help machines guess your thoughts.

```

Let me know if you'd like to include example screenshots or demo links next!
```
