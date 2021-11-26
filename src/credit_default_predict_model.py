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
  Returns the f1 score for each cross validation folds in RandomizedSearch
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
  Do hyperparameter tuning of linear regression model and returns the tuned model 
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
  return random_search

def main(train_path, test_path, out_dir):
  # Read train and test data from respective arguments in opt
  train_df = pd.read_csv(train_path)
  test_df = pd.read_csv(test_path)

  # Split train data into input and target 
  X_train = train_df.drop(columns = ['DEFAULT_PAYMENT_NEXT_MONTH'])
  y_train = train_df['DEFAULT_PAYMENT_NEXT_MONTH']

  # Split train data into input and target 
  X_test = test_df.drop(columns = ['DEFAULT_PAYMENT_NEXT_MONTH'])
  y_test = test_df['DEFAULT_PAYMENT_NEXT_MONTH']

  model_lr = LogisticRegression(max_iter=500)
  model_lr.fit(X_train, y_train)

  # Do hyperparameter tuning 
  model_lr_tuned = model_hyperparameter_tuning(X_train, y_train)

  # Generate random_search_cv_score file for visualization in report
  random_search_cv_score(model_lr_tuned, out_dir)

  # Save both model_lr and model_lr_tuned as a pickle object
  out_path = out_dir + 'final_model.pkl'
  try:
    pickle.dump(model_lr, open(out_path, 'wb'))
    pickle.dump(model_lr_tuned, open(out_path, 'wb'))
  except:
    os.makedirs(os.path.dirname(out_path))
    pickle.dump(model_lr, open(out_path, 'wb'))
    pickle.dump(model_lr_tuned, open(out_path, 'wb'))
  

if __name__ == "__main__":
  main(opt["--train_path"], opt["--test_path"], opt["--out_dir"])
