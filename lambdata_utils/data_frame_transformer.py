import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split as sklearn_train_test_split


class DataFrameTransformer(object):
    def __init__(self, df):
        """Param df pandas dataframe"""
        self.df = df

    def null_count(self):
        """
        df is a dataframe
        Check a dataframe for nulls and return the number of missing values.
        """
        return self.df.isnull().sum().sum()

    def train_test_split(self, frac):
        """
        df is a dataframe
        A Train/Test split function for a dataframe and returns both the Training and Testing sets. 
        frac referes to the precent of data you would like to set aside for training.
        """
        train, test = sklearn_train_test_split(self.df, train_size=frac, random_state=42)
        return train, test

    def randomize(self, seed): 
        pass

    def addy_split(self, add_series):
        pass

    def abbr_2_st(self, state_series, abbr_2_st=True):
        pass

    def list_2_series(self, list_2_series):
        pass

    def rm_outlier(self): 
        pass

    def split_dates(self, date_series):
        pass


if __name__ == "__main__":

    df = pd.DataFrame({"abbrevs": ["CA", "CO", "CT", "DC", "TX"]})

    transformer = DataFrameTransformer(df)
    print(transformer.null_count())
    train, test = transformer.train_test_split(0.8)
    print(test)