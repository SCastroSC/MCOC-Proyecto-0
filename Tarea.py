# -*- coding: utf-8 -*-
"""
Created on Sat Aug 04 18:44:51 2018

@author: Chopita Castro
"""

import math
import numpy as np
from matplotlib import pyplot


def esperanza16(n) :
    i = 1
    t = 0
    while i <= n : 
        x = np.log(i, dtype=np.float16)
        t += x*i
        i += 1 
    return t 

    
def esperanza32(n) :
    i = 1
    t = 0
    while i <= n : 
        x = np.log(i, dtype=np.float32)
        t += x*i
        i += 1 
    return t



def esperanza64(n) :
    i = 1
    t = 0
    while i <= n : 
        x = np.log(i, dtype=np.float64)
        t += x*i
        i += 1 
    return t 

#Calculamos y comparamos error para distintos valores de n 

esperanza_1 = esperanza16(128)
esperanza_2 = esperanza32(128) 
esperanza_3 = esperanza64(128) 


error_1 = ((esperanza_1 - esperanza_3)/esperanza_3)*100 
error_2 = ((esperanza_2 - esperanza_3)/esperanza_3)*100 
error_3 = ((esperanza_3 - esperanza_3)/esperanza_3)*100 

print 'N = 128'
print 'Esperanza_1 = ', esperanza_1 , 'Error_1 = ' , error_1,'%'
print 'Esperanza_2 =' , esperanza_2 , 'Error_2 = ' , error_2,'%'
print 'Esperanza_3 =' , esperanza_3 , 'Error_3 = ' , error_3,'%'

esperanza_1 = esperanza16(256)
esperanza_2 = esperanza32(256) 
esperanza_3 = esperanza64(256) 

error_1 = ((esperanza_1 - esperanza_3)/esperanza_3)*100
error_2 = ((esperanza_2 - esperanza_3)/esperanza_3)*100 
error_3 = ((esperanza_3 - esperanza_3)/esperanza_3)*100 

print 'N = 256'
print 'Esperanza_1 = ', esperanza_1 , 'Error_1 = ' , error_1 ,'%'
print 'Esperanza_2 =' , esperanza_2 , 'Error_2 = ' , error_2 ,'%'
print 'Esperanza_3 =' , esperanza_3 , 'Error_3 = ' , error_3 ,'%'

esperanza_1 = esperanza16(512)
esperanza_2 = esperanza32(512) 
esperanza_3 = esperanza64(512) 

error_1 = ((esperanza_1 - esperanza_3)/esperanza_3)*100
error_2 = ((esperanza_2 - esperanza_3)/esperanza_3)*100 
error_3 = ((esperanza_3 - esperanza_3)/esperanza_3)*100

print 'N = 512'
print 'Esperanza_1 = ', esperanza_1 , 'Error_1 = ' , error_1,'%' 
print 'Esperanza_2 =' , esperanza_2 , 'Error_2 = ' , error_2,'%'
print 'Esperanza_3 =' , esperanza_3 , 'Error_3 = ' , error_3,'%'

esperanza_1 = esperanza16(1024)
esperanza_2 = esperanza32(1024) 
esperanza_3 = esperanza64(1024) 



error_1 = ((esperanza_1 - esperanza_3)/esperanza_3)*100 
error_2 = ((esperanza_2 - esperanza_3)/esperanza_3)*100 
error_3 = ((esperanza_3 - esperanza_3)/esperanza_3)*100

print 'N = 1024'
print 'Esperanza_1 = ', esperanza_1 , 'Error_1 = ' , error_1,'%' 
print 'Esperanza_2 =' , esperanza_2 , 'Error_2 = ' , error_2,'%'
print 'Esperanza_3 =' , esperanza_3 , 'Error_3 = ' , error_3,'%'

 
esperanza_1 = esperanza16(2048)
esperanza_2 = esperanza32(2048) 
esperanza_3 = esperanza64(2048) 

error_1 = ((esperanza_1 - esperanza_3)/esperanza_3)*100
error_2 = ((esperanza_2 - esperanza_3)/esperanza_3)*100 
error_3 = ((esperanza_3 - esperanza_3)/esperanza_3)*100 

print 'N = 2048'
print 'Esperanza_1 = ', esperanza_1 , 'Error_1 = ' , error_1,'%' 
print 'Esperanza_2 =' , esperanza_2 , 'Error_2 = ' , error_2,'%'
print 'Esperanza_3 =' , esperanza_3 , 'Error_3 = ' , error_3,'%'

esperanza_1 = esperanza16(4096)
esperanza_2 = esperanza32(4096) 
esperanza_3 = esperanza64(4096) 

error_1 = ((esperanza_1 - esperanza_3)/esperanza_3)*100
error_2 = ((esperanza_2 - esperanza_3)/esperanza_3)*100
error_3 = ((esperanza_3 - esperanza_3)/esperanza_3)*100

print 'N = 4096'
print 'Esperanza_1 = ', esperanza_1 , 'Error_1 = ' , error_1,'%' 
print 'Esperanza_2 =' , esperanza_2 , 'Error_2 = ' , error_2,'%'
print 'Esperanza_3 =' , esperanza_3 , 'Error_3 = ' , error_3,'%'

Error1 = [0.00319150616015,0.000285208993822, 0.000602229178051,0.000703932850825,0.000117867501319,0.000118770338351] 
Error2 = [2.93313793364e-07,3.22650830947e-07, 2.27569834482e-07, 1.29640431375e-07, 7.27694185697e-08, 7.64372449085e-08] 
Error3 = [0.0 , 0.0, 0.0, 0.0, 0.0, 0.0]

#pyplot.plot([7,8,9,10,11,12], Error1 , 'm' ) 
#pyplot.plot([7,8,9,10,11,12], Error3, 'b')
#pyplot.xlabel('N, donde a.size = 2^N')
#pyplot.ylabel('Error relativo')
#pyplot.legend(['a.dtype=float16 y a.dtype=float64', 'a.dtype=float64' ])
#pyplot.title('Perdida de significancia')
#pyplot.show() 

pyplot.plot([7,8,9,10,11,12], Error2, 'r' ) 
pyplot.plot([7,8,9,10,11,12], Error3, 'b')
pyplot.legend(['a.dtype=float32 y a.dtype=float64', 'a.dtype=float64' ])
pyplot.title('Perdida de significancia')
pyplot.xlabel('N, donde a.size = 2^N')
pyplot.ylabel('Error relativo')
pyplot.show()








        
    


