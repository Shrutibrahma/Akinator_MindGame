# Akinator Mind Game

Hey there! Welcome to Akinator, a cool mind-reading game. You pick a character in your head. I ask simple yes-or-no questions. Then I guess who it is. If I mess up, you can teach me, and I’ll get sharper next time.

## How It Works

- Think of any character.
- Answer questions about their traits (like "from Bollywood?" or "can fight?").
- I make a guess.
- If I’m off, add your character to help me learn.

## Character Data

Characters live in `char.json`. Each has a name and unique traits. There are 40 characters, all different with special features. You can edit the file or add new ones while playing.

## Game Stats

Game details are stored in `game_stats.json`. It keeps your answers, my guess, if I got it right, and when we played. Want to see past games? Just check "Show previous game stats" in the app.

## Resetting

- Hit "Restart Game" to start fresh.
- To wipe everything, delete `char.json`, `q_table.json`, and `game_stats.json` from the game folder.

## Tips

- Pick simple characters to start.
- Use clear traits like "is_real" or "has_magic".
- Skip confusing terms or jargon.
- Keep playing to make me smarter.
- Add new characters—tons of combos are possible!

## How to Run

- Grab the game files from GitHub.
- Open the folder on your computer.
- Make sure Python and Streamlit are installed.
- Install tools: Open a terminal, type `pip install -r requirements.txt`, and hit Enter.
- Start the game: Type `streamlit run main.py` and press Enter.

## Credits

Created by Shruti Brahma. Just a fun project to make AI read your mind!
