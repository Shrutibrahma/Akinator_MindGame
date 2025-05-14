# Akinator Mind Game
Akinator Mind Game is a fun guessing game made with Streamlit and Q-learning. You think of a character, answer yes-or-no questions, and the app tries to guess who it is. If it’s wrong, you can add the character and their traits to help it learn for next time.
How It Works

Pick a character in your mind (real or made-up).
The app asks questions about traits, like "Do they have a cape?" or "Can they fly?"
Using your answers, it guesses the character.
If it guesses wrong, you can add the right character and their traits to teach the app.

Character Data (char.json)
The app saves characters and their traits in a file called char.json. Each character has a name and traits marked as true or false. For example:
{
  "name": "Batman",
  "has_cape": true,
  "is_billionaire": true,
  "can_fly": false
}

You can add characters by editing this file or by teaching the app when it makes a wrong guess.
Game Stats (game_stats.json)
Every game is saved in game_stats.json. It stores:

Your answers
The app’s guess
If the guess was right
How many questions were asked
When the game happened

You can see this info by checking the "Show previous game stats" box in the app.
Resetting the Game

To start a new game, click the "Restart Game" button in the app.
To clear everything (all characters, stats, and learning), delete these files: char.json, q_table.json, and game_stats.json. You can find them in the game’s folder.

Tips for Playing

Begin with 3–5 different characters to help the app guess better.
Use simple, clear traits like "has_hat" or "is_magic".
Avoid traits that are too specific (like "lives_in_London") or too vague (like "is_awesome").
The more you play, the smarter the app gets.

How to Run

Download the game files from the GitHub page to your computer.
Open the game folder.
Make sure you have Python and Streamlit installed. If not, ask someone to help you install them.
Install the needed tools by running this in your terminal or command prompt:
Type: pip install -r requirements.txt and press Enter.


Start the game by running:
Type: streamlit run main.py and press Enter.



Credits
Made by Shruti Brahma.This game was created to mix AI and fun, letting the app guess your thoughts and improve with every game.
