#!/usr/bin/env python

# Author: Taiwo Owoseni
# date: 2021-11-23

"""Cleans and transforms csv file and outputs cleaned data to file path as csv file.


Usage: src/transform_data.py --input_path=<input_path> --out_path =<out_path>

Options:
--input_path=<input_path>   Path (including filename) of the data to be transformed (script supports only csv)
--out_path=<out_path>    Path (including filename) of where to locally write the transformed train data file
"""

import numpy as np
import os
import pandas as pd
import subprocess
from docopt import docopt
from sklearn.compose import  make_column_transformer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder,StandardScaler

opt = docopt(__doc__)

def save_file(path_dir, file_name, doc_name ):
    """
    Function to Save file to preprocessed folder
    """
    file_path = os.path.join(path_dir, file_name)
    try:
        doc_name.to_csv(file_path, index = False, encoding='utf-8')
    except:
        os.makedirs(os.path.dirname(file_path))
        doc_name.to_csv(file_path, index = False, encoding='utf-8')
    
def read_data(file_path):
    """
    Function to Read a csv file
    """
    try:
        abs_path = os.path.abspath(file_path)
    except FileNotFoundError:
        raise ("Absolute path to {input_file} not found in home directory")
    else:
        data = pd.read_csv(abs_path)
    return data

def main(input_path, out_path ):

    data = read_data(input_path)
    X = data.drop(columns="default payment next month")
    y = data["default payment next month"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=123)

    numeric_features = ['LIMIT_BAL', 'AGE', 'BILL_AMT1', 'BILL_AMT2',
                        'BILL_AMT3', 'BILL_AMT4', 'BILL_AMT5', 'BILL_AMT6', 'PAY_AMT1',
                        'PAY_AMT2', 'PAY_AMT3', 'PAY_AMT4', 'PAY_AMT5', 'PAY_AMT6']

    categorical_features = ['SEX', 'MARRIAGE', 'PAY_0', 'PAY_2',
                            'PAY_3', 'PAY_4', 'PAY_5', 'PAY_6' ]

    ordinal_features = ['EDUCATION']

    preprocessor = make_column_transformer(
    (StandardScaler(),numeric_features), 
    (OneHotEncoder(drop="if_binary", sparse=False,
                    handle_unknown="ignore", dtype="int"),
                    categorical_features), 
     ("passthrough", ordinal_features)
    )

    preprocessed_X_train = preprocessor.fit_transform(X_train)
    preprocessed_X_test = preprocessor.transform(X_test)

    # get the column names of the preprocessed data

    column_names = np.concatenate(
                    [np.array(numeric_features),
                    preprocessor.named_transformers_['onehotencoder'].get_feature_names_out(),
                    np.array(ordinal_features)]
    
    )
    trans_train_data = pd.DataFrame(
                         data = preprocessed_X_train, 
                         columns = column_names
    )
    trans_test_data = pd.DataFrame(
                         data = preprocessed_X_test, 
                         columns = column_names
     )
     
    trans_train_data["default payment next month"] = y_train.values
    trans_test_data["default payment next month"]  = y_test.values

    # save transformed data after splitting 
    save_file(out_path, "transformed_train.csv", trans_train_data)
    save_file(out_path,"transformed_test.csv",  trans_test_data)

if __name__ == "__main__":
    main(opt["--input_path"],  opt["--out_path"])
