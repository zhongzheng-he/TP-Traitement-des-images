# -*- coding: utf-8 -*-
"""
time measurment fonctions to evaluate execution time of code :
- tic : initialize chrono
- toc : stop chrono and return elapsed time in secondes

@author: emilien
"""
import time

ticSharedVar=0

def tic():
    """
    Initialize chrono
    """
    global ticSharedVar 
    ticSharedVar = time.time()
    
def toc():
    """
    stop chrono and return elapsed time in secondes
    """
    global ticSharedVar 
    return time.time() - ticSharedVar

if __name__ == '__main__':
    tic()
    
    toc1 = toc()
    
    print(toc1)