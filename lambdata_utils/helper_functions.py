import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split as sklearn_train_test_split

def null_count(df):
    """
    df is a dataframe
    Check a dataframe for nulls and return the number of missing values.
    """
    return df.isnull().sum().sum()

def train_test_split(df, frac):
    """
    df is a dataframe
    A Train/Test split function for a dataframe and returns both the Training and Testing sets. 
    frac referes to the precent of data you would like to set aside for training.
    """
    train, val = sklearn_train_test_split(df, train_size=frac, random_state=42)
    return train, val

def randomize(df, seed): 
    pass

def addy_split(add_series):
    pass

def abbr_2_st(state_series, abbr_2_st=True):
    pass

def list_2_series(list_2_series, df):
    pass

def rm_outlier(df): 
    pass

def split_dates(date_series):
    pass
