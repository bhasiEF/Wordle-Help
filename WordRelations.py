# -*- coding: utf-8 -*-
"""
Created on Fri Feb  4 13:09:39 2022

@author: bhasi
"""

import numpy as np
import string

alphabet = list(string.ascii_lowercase)
master_list = np.loadtxt('csw19.csv', dtype=str)
num_words = len(master_list)

#%%

def tensorize(z):
    chars = np.array([list(s) for s in z])
    return np.moveaxis(np.array([(chars == alphabet[i]) for i in range(len(alphabet))], dtype=bool),[0,1,2], [2, 0, 1])

def condense(z):
    num1, num2 = np.shape(z)[:2]
    z = np.reshape(z,(num1*num2, 25))
    x = np.reshape(np.arange(0,25),(5,5))
    
    for n in range(5):
        a = np.ones(25,dtype=bool)
        a[np.setxor1d(x[n,:], x[:,n])] = False
        z[z[:,x[n,n]]] = a*z[z[:,x[n,n]]==1]
    
    for n in range(5):
        for m in np.setxor1d(x[0,:], n):   
            a = np.ones(25,dtype=bool)
            a[np.setxor1d(x[n,:], x[:,m])] = False
            z[z[:,x[n,m]]] = a*z[z[:,x[n,m]]==1]
    
    y = np.zeros((np.shape(z)[0],5),dtype='uint8')
    
    for n in range(5):
        a = np.setxor1d(x[n,:], 6*n)
        y[:,n] = 2*(z[:,n*6]) + (z[:,a[0]]) + (z[:,a[1]]) + (z[:,a[2]]) + (z[:,a[3]])
       
    y = np.sum(np.array([81,27,9,3,1],dtype='uint8')*y,axis=1)
    
    return np.reshape(y,(num1, num2))

#%%

master_list_tensor = tensorize(master_list)
inner_products = np.tensordot(master_list_tensor,master_list_tensor, axes=([2],[2])).swapaxes(1,2)
del master_list_tensor

relations = np.array(condense(inner_products), dtype='uint8')  
del inner_products

#%%
uz = np.delete(np.arange(0,243),242-np.array([81,27,9,3,1]))

# no prior knowledge of answer list
prob = np.array([np.sum(relations == u,axis=1)/num_words for u in uz])
log_prob = np.where(prob==0,0,np.log2(prob))
info = -np.sum(prob*log_prob, axis=0)

# prior knowledge of answer list
prob2 = np.array([np.sum(relations[:,:2315] == u,axis=1)/2315 for u in uz])
log_prob2 = np.where(prob2==0,0,np.log2(prob2))
info2 = -np.sum(prob2*log_prob2, axis=0)

#%%
np.save('word_relations_csw19.npy', relations)
np.save('seed_entropies_csw19_no_prior.npy', info)
np.save('seed_entropies_csw19_prior_2315.npy', info2)
