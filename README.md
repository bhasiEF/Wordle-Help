# Wordle-Help

Wordle-Help contains code that takes an information theoretic approach to solving Wordle puzzles. 

The first .py file 'Relations.py' reads in a master list of 12,972 words that Wordle acceps (taken from Collins Scrabble Words 2019), and generates (i) an array that represents the wordle 'output' for any (guess, target) pair of words and (ii) arrays that contain the corresponding entropy of each word as a potential guess. Two such entropy arrays are generated: one that presupposes no prior knowledge of which of the 12,972 words are likely to be Wordle answers, and another which already incorporates knowledge of the 2315 word subset that represent all past and future Wordle answers. 

The second .py file 'WordleHelp.py' defines the function wordle_help(), which advises the user on strategy based on the user's guesses. 
