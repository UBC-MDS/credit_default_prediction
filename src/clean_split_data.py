#!/usr/bin/env python

# Author: Taiwo Owoseni
# date: 2021-11-25

"""
Cleans and splits raw data into train and test data set and save to file path as csv file.

Usage: src/clean_split_data.py --input_path=<input_path> --out_dir=<out_dir>

Options:
--input_path=<input_path>   Path (file path) to raw data (script supports only csv)
--out_dir=<out_dir>       Path (directory) to save transformed train and test data
"""

import os
import pandas as pd
from docopt import docopt
from sklearn.model_selection import train_test_split

opt = docopt(__doc__)

def save_file(path_dir, file_name, processed_data): 
    """
    Saves file.

    This function creates a new file by
    saving it to the specified path.

    Parameters
    ----------
    path_dir : str
        The path to save the file.
    file_name: str
        The file name of the document.
    processed_data: pd.DataFrame
        The object to be saved.

    Examples
    --------
    save_file('data/split', 'train_data',  train_df)
    """
    
    file_path = os.path.join(path_dir, file_name)
    try:
        processed_data.to_csv(file_path, index = False, encoding='utf-8')
    except:
        os.makedirs(os.path.dirname(file_path))
        processed_data.to_csv(file_path, index = False, encoding='utf-8')
    
def read_data(file_path):
    """
    Reads a csv file from path.

    Parameters
    ----------
    file_path : str
        The path of the file.
   
    Returns
    -------
    data : pd.DataFrame
        A csv file

    Examples
    --------
    read_data('data/split/train.csv')
    """
    try:
        abs_path = os.path.abspath(file_path)
    except FileNotFoundError:
        raise ("Absolute path to {input_file} not found in home directory")
    else:
        data = pd.read_csv(abs_path)
    return data

def main(input_path, out_dir):

    data = read_data(input_path)
    data = data.rename(columns={'default payment next month':'DEFAULT_PAYMENT_NEXT_MONTH'})
    train_data, test_data = train_test_split(data, test_size=0.2, random_state=123)

    save_file(out_dir, "cleaned_train.csv", train_data)
    save_file(out_dir, "cleaned_test.csv", test_data)
    save_file(out_dir, "cleaned_data.csv", data)

if __name__ == "__main__":
    main(opt["--input_path"],  opt["--out_dir"])