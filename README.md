# Wordle-Help

Wordle-Help contains code that takes an information theoretic approach to solving Wordle puzzles. 

The first .py file 'WordleRelations.py' reads in a master list of 12,972 words that Wordle accepts (taken from Collins Scrabble Words 2019), and generates (i) an array that represents the wordle 'output' for any (guess, target) pair of words and (ii) arrays that contain the corresponding entropy of each word as a potential guess. Two such entropy arrays are generated: one that presupposes no prior knowledge of which of the 12,972 words are likely to be Wordle answers, and another which already incorporates knowledge of the 2315 word subset that represent all past and future Wordle answers. 

The array containing the wordle 'outputs' for every (guess, target) pair is split across the files 'relations_csw19_0.npy' through 'relations_csw19_7.npy'.

The array containing entropies for each guess, without taking into account prior knowledge of the Wordle subset is called 'entropies_no_prior.npy'

The array containing entropies, based on prior knowledge of the subset of past+future Wordle answers (2315 words) for each guess,is called 'entropies_prior_2315.npy'

The second .py file 'WordleHelp.py' defines the function wordle_help(), which advises the user on strategy based on the user's guesses. This file runs independently of the first file, as it loads all data from the github repo. 
