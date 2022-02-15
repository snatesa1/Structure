

# From here I am going to run the prpgram

import constants as c
from helper import *

def run():
    #print (f'Prime numbers for an given number range',calculate_prime_numbers(start=c.START,finish=c.FINISH))
    #print (f'The factorial for {c.START} % 2  is ->',factorial(start=c.START))
    #read_file("C:\Admin\Stock_Upgrades_News\Robin_stocks_2021-02-03.csv")        
    display_name('sathish',45,sex='male')
    rows=10
    cols=3
    freq='D'
    print (generate_sample_data(rows,cols,freq))

    

if __name__ == '__main__':
    run()
