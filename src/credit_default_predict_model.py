#!/usr/bin/env python

# Author: Karanpreet Kaur
# date: 2021-11-25

"""Fits a logistic regression model on the pre-processed training data from the default of credit card client data (from https://archive.ics.uci.edu/ml/machine-learning-databases/00350/default%20of%20credit%20card%20clients.xls)
Saves the model as a pkl file.

Usage: src/credit_default_predict_model.py --train_path=<train_path> --test_path=<test_path> --out_dir=<out_dir>

Options:
--train_path=<train_path>        Path (including filename) to training data (which needs to be saved as a .csv file)
--test_path=<test_path>          Path (including filename) to test data (which needs to be saved as a .csv file)
--out_dir=<out_dir>              Path of directory where to locally save model (model needs to be saved as .pkl object)
"""
  
from docopt import docopt
import os
import numpy as np
import pandas as pd
import pickle

from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import RandomizedSearchCV

opt = docopt(__doc__)

def random_search_cv_score(model_tuned, out_dir):
  """
  Extract and save cross validation f1 scores on hypertuned model.

  This function takes tuned model as input and extract cross validation
  f1 score for each fold (defined as cv = 10 folds) with defined hyperparameters
  values C and class_weight and save it on out_dir.

  Parameters
  ----------
  model_tuned : object
      Tuned model on defined hyperparameters of Logistic regression model
  out_dir : str
      docopt argument --outdir

  Returns
  -------
  None
      Save the extracted cross validation results to random_search_cv_scores.csv in out_dir
  """
  final_selected_cols = ['param_logisticregression__class_weight', 'param_logisticregression__C',
                       'split0_test_f1', 'split1_test_f1',
                       'split2_test_f1', 'split3_test_f1',
                       'split4_test_f1', 'split5_test_f1',
                       'split6_test_f1', 'split7_test_f1',
                       'split8_test_f1', 'split9_test_f1']
  random_search_cv_scores = pd.DataFrame(model_tuned.cv_results_)[final_selected_cols]
  random_search_cv_scores = pd.melt(random_search_cv_scores, 
                                    id_vars=['param_logisticregression__class_weight', 'param_logisticregression__C'],
                                    var_name='split_number',
                                    value_name='scores')
  # Save random_search_cv_scores to the out_dir                   
  cv_scores_out_path = out_dir + 'random_search_cv_scores.csv'
  try:
    random_search_cv_scores.to_csv(cv_scores_out_path, index = False, encoding='utf-8')
  except:
    os.makedirs(os.path.dirname(cv_scores_out_path))
    random_search_cv_scores.to_csv(cv_scores_out_path, index = False, encoding='utf-8')

def model_hyperparameter_tuning(X_train, y_train):
  """
  Hyperparameter tuning on Logistic Regression model.

  This function takes X_train and y_train dataframes and does model tuning using
  RandomizedSearchCV with given set of hyperparameter C & class_weight and 
  returns tuned model.

  Parameters
  ----------
  X_train : dataframe
      Input parameters in train split
  y_train : str
      Target column of train split

  Returns
  -------
  object
      Returns the tuned model object
  """
  scoring = [
    "accuracy",
    "f1",
    "recall",
    "precision",
    "roc_auc",
    "average_precision"
  ]

  param_grid = {
    'logisticregression__C': [0.001, 0.01, 0.1, 1, 10, 100, 1000],
    'logisticregression__class_weight':['None', 'balanced']
  }
  pipe = make_pipeline(LogisticRegression(max_iter=2000))
  random_search = RandomizedSearchCV(pipe, 
                                     param_grid, 
                                     cv=10, 
                                     n_jobs=-1, 
                                     scoring=scoring, 
                                     refit='f1', 
                                     random_state=123)
  random_search.fit(X_train, y_train)
  # Test to check the return type of tuned model
  assert isinstance(random_search, RandomizedSearchCV), "random_search is not a RandomizedSearchCV model"
  return random_search

def main(train_path, test_path, out_dir):
  # Read train and test data from respective arguments in opt
  train_df = pd.read_csv(train_path)
  test_df = pd.read_csv(test_path)

  # Split train data into input and target 
  X_train = train_df.drop(columns = ['DEFAULT_PAYMENT_NEXT_MONTH'])
  y_train = train_df['DEFAULT_PAYMENT_NEXT_MONTH']

  # Split test data into input and target 
  X_test = test_df.drop(columns = ['DEFAULT_PAYMENT_NEXT_MONTH'])
  y_test = test_df['DEFAULT_PAYMENT_NEXT_MONTH']

  model_lr = LogisticRegression(max_iter=500)
  model_lr.fit(X_train, y_train)

  # Test to check the type of Logistic Regression model with default hyperparameters
  assert isinstance(model_lr, LogisticRegression), "model_lr is not a Logistic Regression model"

  # Save logistic regression model with default parameters as .pkl object
  default_model_out_path = out_dir + 'default_lr_model.pkl'
  try:
    pickle.dump(model_lr, open(default_model_out_path, 'wb'))
  except:
    os.makedirs(os.path.dirname(default_model_out_path))
    pickle.dump(model_lr, open(default_model_out_path, 'wb'))

  # Do hyperparameter tuning 
  model_lr_tuned = model_hyperparameter_tuning(X_train, y_train)

  # Generate random_search_cv_score file for visualization in report
  random_search_cv_score(model_lr_tuned, out_dir)

  # Save tuned logistic regression model with hyperparameters as .pkl object
  final_tuned_model_out_path = out_dir + 'final_tuned_model.pkl'
  try:
    pickle.dump(model_lr_tuned, open(final_tuned_model_out_path, 'wb'))
  except:
    os.makedirs(os.path.dirname(final_tuned_model_out_path))
    pickle.dump(model_lr_tuned, open(final_tuned_model_out_path, 'wb'))
  

if __name__ == "__main__":
  main(opt["--train_path"], opt["--test_path"], opt["--out_dir"])
