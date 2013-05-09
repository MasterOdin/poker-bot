poker-bot
=========

A 2 player poker bot who learns hand values based off playing against itself.

Written for CSC 370: Artificial Intelligence

All probabilities for specific hand strengths are saved in results/ for the different parts of the game

Currently, only a very simple betting policy is in place:
    if below .3 probability, check or fold
    if below .6 probability, check or call
    if above .6 probability, bet  
A more remarkable policy would be a future consideration

Files:
./bot.py (logic beyond bot making an action)
./card.py (basic card object for inserting into a deck)
./game.py (main game logic. allows for playing through the game)
./setup.py (logic behind setting up the bot and its data)
./main.py (actual texas hold'em game)

Currently, bet doesn't have any money attached to it

Final Report:
    A final report for the project is contained within the upload and can be seen at ./FINALREPORT.pdf
