# functions that are going to help calculate prime
from ast import For
import os
import re
from unicodedata import name
import pandas as pd
import numpy as np
import pydantic
from constants import *



class Book(pydantic.BaseModel):
    sym: str
    author: str
    price: float
    #isbn: Optional[str]
    

def is_prime(num):
    if num > 1:
        for n in range(2,num):
            if num % n != 0:
                continue
            else:
                return False
    return True

#print (is_prime(18))

def calculate_prime_numbers(start,finish):
    
    prime=[]
    for n in range(start,finish):
        if is_prime(n):
            prime.append(n)
    return prime

def factorial(start):
    fact=1
    for num in range(1,start+1):
        fact = fact * num
    return fact
            
def read_file(name):
    #print (name)
    df = pd.read_csv(name)
    print(df.head(15))

            
def name_greeting(name_function):
    '''
    Decator function to wrap the greeting message
    -----------
    
    Parameters:
    Name of the function
    
    
    '''
    def wrapper(*args,**kwargs):
        print (f'The name greeting is using the wrapper so say Hi')
        name_function(*args,**kwargs)
    return wrapper
@name_greeting
def display_name(name,age,sex):
    print (f'The name is {name} and the age is {age} and greeitng {name}',sex+name)

def generate_sample_data(rows, cols, freq='1min'):
    '''
    Function to generate sample financial data.

    Parameters
    ==========
    rows: int
        number of rows to generate
    cols: int
        number of columns to generate
    freq: str
        frequency string for DatetimeIndex

    Returns
    =======
    df: DataFrame
        DataFrame object with the sample data
    '''
    rows = int(rows)
    cols = int(cols)
    # generate a DatetimeIndex object given the frequency
    index = pd.date_range('2000', periods=rows, freq=freq)
    # determine time delta in year fractions
    dt = (index[1] - index[0]) / pd.Timedelta(value='365D')
    #print (dt)
    # generate column names
    columns = ['No%d' % i for i in range(cols)]
    # generate sample paths for geometric Brownian motion
    raw = np.exp(np.cumsum((r - 0.5 * sigma ** 2) * dt +
                 sigma * np.sqrt(dt) *
                 np.random.standard_normal((rows, cols)), axis=0))
    # normalize the data to start at 100
    raw = raw / raw[0] * 100
    # generate the DataFrame object
    df = pd.DataFrame(raw, index=index, columns=columns)
    return df

def factorial(n):
    if n == 0 or n ==1:
        return 1
    else:
        return n * factorial(n-1)

print (factorial(55))
list_of_dic=[{"prod":"aws","uat":"az","dev":"gcp"},{"prod_size":"XXL","uat_size":"XL","dev_size":"L"}]
dat = pd.DataFrame(list_of_dic)
for k,x in enumerate(list_of_dic):
    dic={}
    for z,v in x.items():
        print (f'key is --> {z} and value is --> {v}')
        if "prod" in z:
            dic[z] = v
print (f'The size of the prod {x.keys()} is {dic}')

print (dat)    




