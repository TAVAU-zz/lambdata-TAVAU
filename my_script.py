import pandas as pd
import numpy as np
from helper_functions import null_count, train_test_split

def my_dataframe():
    dict = {'A':[1, 4, 6, 9], 
            'B':[np.NaN, 5, 8, np.NaN], 
            'C':[7, 3, np.NaN, 2], 
            'D':[1, np.NaN, np.NaN, np.NaN]}  
        
    # creating dataframe from the dictionary  
    return pd.DataFrame(dict)

if __name__ == "__main__":
    df = my_dataframe()
    # df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/abalone/abalone.data')
    print(null_count(df))
    # train, val = train_test_split(df, 0.8)
    # print(train)
    # print(val)