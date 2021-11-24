#!/usr/bin/env python

# Author: Taiwo Owoseni
# date: 2021-11-23

"""Cleans and transforms csv file and outputs cleaned data to file path as csv file.


Usage: src/transform_data.py --input_file=<input_file> --out_file=<out_file> --test_file=<test_file>

Options:
--input_file=<input_file>  Path (including filename) of the data to be transformed (script supports only csv)
--out_file=<out_file>      Path (including filename) of where to locally write the file
--test_file=<test_file>    Path (including filename) of where to locally write the test file
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

def main(input_file, output_file, test_file):

    subprocess.call("src/download.py --out_type=xls --url=https://archive.ics.uci.edu/ml/machine-learning-databases/00350/default%20of%20credit%20card%20clients.xls --out_file=data/raw/default_credit.csv", shell=True)

    try:
        abs_path = os.path.abspath(input_file)
    except FileNotFoundError:
        raise ("Absolute path to {input_file} not found in home directory")
    else:
        data = pd.read_csv(abs_path)
        train_data, test_data = train_test_split(data, test_size=0.2, random_state=123)

    # save test data after splitting 
    try:
        test_data.to_csv(test_file, index = False, encoding='utf-8')
    except:
        os.makedirs(os.path.dirname(test_file))
        test_data.to_csv(test_file, index = False, encoding='utf-8')

    # transforming the train data
    X_train = train_data.drop(columns=["default_payment_next_month"])
    y_train = train_data["default_payment_next_month"]

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

    # append y to the newly transformed data

    transformed_data = pd.DataFrame(
    data = preprocessed_X_train, 
    columns = column_names
    )
    transformed_data["default_payment_next_month"] = y_train.values

    # save transformed data after splitting 

    try:
        transformed_data.to_csv(output_file, index = False, encoding='utf-8')
    except:
        os.makedirs(os.path.dirname(output_file))
        transformed_data.to_csv(output_file, index = False, encoding='utf-8')


if __name__ == "__main__":
    main(opt["--out_type"], opt["--test_file"], opt["--out_file"])
