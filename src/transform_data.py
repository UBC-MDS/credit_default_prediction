#!/usr/bin/env python

# Author: Taiwo Owoseni
# date: 2021-11-23

"""Cleans and transforms csv file and outputs cleaned data to file path as csv file.


Usage: src/transform_data.py --input_file=<input_file> --transformed_train_file=<transformed_train_file>
        --train_file=<train_file> --test_file=<test_file> --y_train_file=<y_train_file> --y_test_file=<y_test_file>  

Options:
--input_file=<input_file>                              Path (including filename) of the data to be transformed (script supports only csv)
--transformed_train_file=<transformed_train_file>      Path (including filename) of where to locally write the transformed train data file
--train_file=<train_file>                              Path (including filename) of where to locally write the train file
--test_file=<test_file>                                Path (including filename) of where to locally write the test file
--y_train_file=<y_train_file>                          Path (including filename) of where to locally write the y_train file
--y_test_file=<y_test_file>                            Path (including filename) of where to locally write the y_test file
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

def save_file(file_path, doc_name ):
    """
    Function to Save file 
    """
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

def main(input_file, transformed_train_file, train_file, test_file, y_train_file, y_test_file ):
    subprocess.run("src/download_data.py \
                    --out_type=csv \
                    --url=https://archive.ics.uci.edu/ml/machine-learning-databases/00350/default%20of%20credit%20card%20clients.xls \
                    --out_file=data/raw/default_credit_card_clients.csv",
                    shell=True)


    data = read_data(input_file)
    X = data.drop(columns="default_payment_next_month")
    y = data["default_payment_next_month"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=123)

    # save test and train data after splitting 
    save_file(test_file, X_test)
    save_file(y_test_file, y_test)
    save_file(train_file, X_train)
    save_file(y_train_file, y_train)


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

    # get the column names of the preprocessed data

    column_names = np.concatenate(
    [np.array(numeric_features),
     preprocessor.named_transformers_['onehotencoder'].get_feature_names_out(),
     np.array(ordinal_features)]
    )

    transformed_data = pd.DataFrame(
    data = preprocessed_X_train, 
    columns = column_names
    )
   
    # save transformed data after splitting 
    save_file(transformed_data, transformed_train_file)

if __name__ == "__main__":
    main(opt["--input_file"], opt["--transformed_train_file"], 
        opt["--train_file"],  opt["--test_file"], 
        opt["--y_train_file"],  opt["--y_test_file"]  
)
