import multiprocessing
import time
   

def factorize(*number):
    result = []
    for num in number:
        factors = []
        for i in range(1, num + 1):
            if num % i == 0:
                factors.append(i)
        result.append(factors)
    return result

def test_factorize():
    
            

    