'''
Created on Jun 11, 2015

@author: YDuan
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_digits


class Digit_Comparison(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        digits = load_digits()
        self.data = digits.data
        self.target = digits.target
    
    
    def plot_hist(self):
        # set bin
        bins = np.linspace(0, 16, 17)
        digit_1, digit_2, row = self.get_user_input() 
        
        # get data for plotting
        df_digit_1 = self.get_data(digit_1, row)
        df_digit_2 = self.get_data(digit_2, row)
        
        # set figure
        fig, axs = plt.subplots(3,3,figsize=(15,15))
        for row in xrange(3):
            for col in xrange(3):
                plot_index = row*3+col
                if  plot_index < 8 :
                    print plot_index
                    axs[row, col].hist(df_digit_1.iloc[:, plot_index], bins, alpha=0.5, label=str(digit_1))
                    axs[row, col].hist(df_digit_2.iloc[:, plot_index], bins, alpha=0.5, label=str(digit_2))
                    axs[row, col].legend(loc='upper right')
        
        fig.savefig('Digit_Hist.png')
        plt.show()           
        # function to get data
    def get_data(self, digit, row):
            digit_data = self.data[self.target==digit]
            row_data = digit_data[:, row*8:(row+1)*8]
            return pd.DataFrame(row_data)
        
    def get_user_input(self):
        digit_1 = raw_input('Enter Digit 1')
        digit_2 = raw_input('Enter Digit 2')
        row = raw_input('Enter Row Number')
        return int(digit_1), int(digit_2), int(row)


if __name__ == '__main__':
    dc = Digit_Comparison()
    dc.plot_hist()
    

