import matplotlib.pyplot as plt
import numpy as np


def value(k,A,s):
    return k*A**s

ks = range(1,3)
amount = range(22)
ss = range(1,3)
subject_value = []


for k in ks:
    subject_value = []
    for s in ss:
        # subject_value = []
        for a in amount:    
            # subject_value = [value(k,amount,s)            
            subject_value.append(value(a,s,k))    
        plt.plot(amount, subject_value) 
        subject_value = []
            
        
plt.legend()
plt.xlabel("amount")
plt.ylabel("valor do jogo")
plt.show()