# -*- coding: utf-8 -*-
"""
Created on Fri Feb  4 18:24:55 2022

@author: bhasi
"""

import numpy as np
import string

master_list = np.loadtxt('csw19.csv', dtype=str)
num_words = len(master_list)

relations = np.load('word_relations_csw19.npy')
info = np.load('seed_entropies_no_prior.npy')

nth = {
    1: "first",
    2: "second",
    3: "third",
    4: "fourth",
    5: "fifth",
    6: "sixth",
}

#%%

def wordle_help():
    status = 0
    match = 242
    round_num = 1
    
    sub = master_list
    rel = relations
    inf = info
    
    i = np.argmax(inf)
    
    print(f"Which word will you play as your {nth[round_num]} guess?")
    print("Wordle helper recommends that you try \"", master_list[i], "\".", sep='')
    print(f'We expect {inf[i]:2.2f} bits of information from guessing \"', master_list[i], "\".", sep='')
    
    temp = input()
    while not temp in master_list:
        print("This word is not on the master list of words on file. Please try another word. (If Wordle accepted the word, please update the master files)")
        temp = input()
    
    print("You guessed \"", temp, "\".", sep='')
    
    if not temp == master_list[i]: 
        i = np.argwhere(master_list == temp)[0][0]
        print(f'We expect {inf[i]:2.2f} bits of information from guessing \"', temp, "\".", sep='')
    
    x,y = np.unique(rel[i,:],axis=0,return_inverse=True)
    
    print(f"Enter wordle output for \"{temp}\":")
    
    need_input = True
    while need_input:
        try:
            status = int(input(), 3)
            need_input = False
        except:    
            print(f"Please enter a valid wordle output for \"{temp}\".")
            print("The output should be coded as a 5-digit number consisting of 0s,1s, and 2s")
            print("0 corresponds to a letter that is not in the word.")
            print("1 corresponds to a letter that is in the word, but in the incorrect position.")
            print("2 corresponds to a letter in the correct position.")
        
    round_num += 1
    
    while not (status == match):
        inds = np.where([np.all(r == status) for r in x])[0][0] == y

        rel = rel[:,inds]
        sub = sub[inds]

        p = np.array([np.sum(rel == u,axis=1)/np.shape(rel)[1] for u in np.unique(rel)])
        log_p = np.log2(np.where(p==0,1E-10,p))
        inf = -np.sum(p*log_p, axis=0)
        
        print("Possible wordles still in the running:")
        print(sub)
        
        i_s = np.squeeze(np.argwhere(inf == np.amax(inf)))
        guess_candidates = master_list[i_s]
        guess_overlap = [w for w in guess_candidates if w in sub]

        
        if len(guess_overlap) == 0 and np.ndim(i_s) > 0:
            i = i_s[0]
        elif len(guess_overlap) == 0:
            i = int(i_s)
        else:
            i = np.argwhere(master_list == guess_overlap[0])[0][0]
       
        
        if len(sub)>1:
            print(f"Which word will you play as your {nth[round_num]} guess?")
            print("Wordle helper recommends that you try \"", master_list[i], "\".", sep='')
            print(f'We expect {inf[i]:2.2f} bits of information from guessing \"', master_list[i], "\".", sep='')
            
            temp = input()
            
            while not temp in master_list:
                print("This word is not on the master list of words on file. Please try another word. (If Wordle accepted the word, please update the master files)")
                temp = input()
            
            print("You guessed \"", temp, "\".", sep='')
            
   
            if not temp == master_list[i]: 
                i = np.argwhere(master_list == temp)[0][0]
                print(f'We expect {inf[i]:2.2f} bits of information from guessing \"', temp, "\".", sep='')
            
        else:
            print("Based on its word list, wordle helper has narrowed the possiblities down to one word: \"", sub[0], "\".", sep='')
            temp = sub[0]
        x,y = np.unique(rel[i,:,],axis=0,return_inverse=True)
                
        print("Enter wordle output:")
        
        need_input = True
        while need_input:
            try:
                status = int(input(), 3)
                need_input = False
            except:    
                print(f"Please enter a valid wordle output for \"{temp}\".")
                print("The output should be coded as a 5-digit number consisting of 0s,1s, and 2s")
                print("0 corresponds to a letter that is not in the word.")
                print("1 corresponds to a letter that is in the word, but in the incorrect position.")
                print("2 corresponds to a letter in the correct position.")

        round_num += 1