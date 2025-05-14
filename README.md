# Akinator Mind Game
HI USER! Meet Akinator - a mind reading game. 
You think of a character. The Akinator ask yes-or-no questions. Then it tries to guess who it is. If I'm wrong, you can tell me. I get better each time.

How It Works
Think of a character.
Answer questions about their traits(like bollywood , fight, real or fictional).
It makes a guess about the character.
If incorrect, add the character to help akinator learn.

Character Data
Characters are saved in char.json. They all possess a name and traits. There are 40 characters which are unique to each other and have unique differentiating features


Dynamic edits can be made to file or add characters to the game.
Game Stats
Game data is entered into game_stats.json. It saves your answer, the game guess, if model was correct, and when the game was played. Check "Show previous game stats" to see them.
Resetting

Click "Restart Game" to start anew.
To restart all, delete char.json, q_table.json, and game_stats.json from the game directory.

Tips

Start with simple characters.
trained with clear and distinct attributes like.
No Jargon's used.
Play tons so model can learn.
keep adding any new character if you can think of as 7! characters are possible.

How to Run

Download game files from GitHub.
Open the folder on your computer.
Make sure you have Python and Streamlit installed.
Install utilities: Open terminal, type pip install -r requirements.txt, press Enter.
Run the game: Type streamlit run main.py, press Enter.

Credits
Developed by Shruti Brahma. 
