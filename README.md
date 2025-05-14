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





# Akinator Mind Game
HI USER! Meet Akinator - a mind reading game. 
You think of a character. The Akinator ask yes-or-no questions. Then it tries to guess who it is. If I'm wrong, you can tell me. I get better each time.

How It Works
- Think of a character.
- Answer questions about their traits(like bollywood , fight, real or fictional).
= It makes a guess about the character.
= If incorrect, add the character to help akinator learn.

Character Data
= Characters are saved in char.json. They all possess a name and traits. There are 40 characters which are unique to each other and have unique differentiating features
- Dynamic edits can be made to file or add characters to the game.
  
Game Stats
- Game data is entered into game_stats.json. It saves your answer, the game guess, if model was correct, and when the game was played. Check "Show previous game stats" to see them.
For Resetting
- Click "Restart Game" to start anew.
To restart all, delete char.json, q_table.json, and game_stats.json from the game directory.

Tips

- Start with simple characters.
- trained with clear and distinct attributes like.
- No Jargon's used.
- Play tons so model can learn.
- keep adding any new character if you can think of as 7! characters are possible.

How to Run

- Download game files from GitHub.
- Open the folder on your computer.
- Make sure you have Python and Streamlit installed.
- Install utilities: Open terminal, type pip install -r requirements.txt, press Enter.
- Run the game: Type streamlit run main.py, press Enter.

Credits
Developed by Shruti Brahma. 
