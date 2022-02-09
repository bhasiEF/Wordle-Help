# Wordle-Help

Wordle-Help contains code that takes an information theoretic approach to solving Wordle puzzles. 

The first file 'Relations.py' reads in a master list of 12,972 words that Wordle acceps (taken from Collins Scrabble Words 2019), and outputs (i) a file that represents the wordle 'output' for any (guess, target) pair of words and (ii) files that contain the corresponding entropy of each word as a potential guess. Two such files are generated: one that presupposes no prior knowledge of which of the 12,972 words are likely to be Wordle answers, and another which already incorporates knowledge of the 2315 word subset that represent all past and future Wordle answers. 

The second file 'WordleHelp.py' defines the function wordle_help(), which advises the user on strategy based on the user's guesses. 
