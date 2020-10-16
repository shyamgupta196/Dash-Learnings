import numpy as np
import time
import random

print('starting to add to data.txt file ')


def conti():
    '''
    this function will generate x's and y's 
    and the script of app4 will be continuously be
reading from data.txt
    '''
    while True:
        rand_nos_x = int(np.ones(1,dtype=np.int8))
        rand_nos_y = np.random.randint(-20, 20)

        joins = ','.join([str(rand_nos_x), str(rand_nos_y)])
        print(joins)
        time.sleep(1)
        filer = open('data.txt', 'a')
        filer.write(str(joins))
        filer.write('\n')
        filer.close()


conti()
