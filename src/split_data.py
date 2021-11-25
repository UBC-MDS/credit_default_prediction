#!/usr/bin/env python

# Author: Taiwo Owoseni
# date: 2021-11-25

"""
Splits raw data into train and test data set and save to file path as csv file.

Usage: src/split_data.py --input_path=<input_path> --out_path =<out_path>

Options:
--input_path=<input_path>   Path (directory) to raw data (script supports only csv)
--out_path=<out_path>       Path (directory) to save train and test data
"""

import os
import pandas as pd
from docopt import docopt
from sklearn.model_selection import train_test_split

opt = docopt(__doc__)

def save_file(path_dir, file_name, obj_name ):
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
    obj_name: pd.DataFrame
        The object to be saved.
        
    Returns
    -------
    csv

    Examples
    --------
    save_file('data/split/', 'train_data',  train_df)
    
    """
    file_path = os.path.join(path_dir, file_name)
    try:
        obj_name.to_csv(file_path, index = False, encoding='utf-8')
    except:
        os.makedirs(os.path.dirname(file_path))
        obj_name.to_csv(file_path, index = False, encoding='utf-8')
    
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
    save_file('data/split/train.csv')
    """
    try:
        abs_path = os.path.abspath(file_path)
    except FileNotFoundError:
        raise ("Absolute path to {input_file} not found in home directory")
    else:
        data = pd.read_csv(abs_path)
    return data

def main(input_path, out_path):

    data = read_data(input_path)
    train_data, test_data = train_test_split(data, test_size=0.2, random_state=123)

    save_file(out_path, "train.csv", train_data)
    save_file(out_path,"test.csv", test_data)

if __name__ == "__main__":
    main(opt["--input_path"],  opt["--out_path"])
