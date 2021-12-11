# author: Arushi Ahuja
# date: 2021-12-04

'''This script generates the correlation heat map of the 
   transformed data

Usage: credit_card_default_eda.py --file_path=<file_path> --out_dir=<out_dir>

Options:
--file_path=<file_path>   Path to the data file
--out_dir=<out_dir>       Path (directory) to save the images
'''
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from docopt import docopt

opt = docopt(__doc__)

def main(file_path, out_dir):
  
  # making a string variable to store information on where to save the file
  saving_to = out_dir + "correlation_heatmap_plot"
  
  #saving the transformed data frame file 
  tranformed_df = pd.read_csv(file_path)
  
  #shortning the target column name to DEFAULT_PAYMENT to fit better in the graph
  tranformed_df = tranformed_df.rename(columns={"DEFAULT_PAYMENT_NEXT_MONTH": "DEFAULT_PAYMENT"})
  
  #Splitting the transformed Data Frame into X_train and y_train
  X_train, y_train = tranformed_df.drop(columns=["DEFAULT_PAYMENT"]), tranformed_df["DEFAULT_PAYMENT"]
  
  #Creating the correlation plot
  cor = pd.concat((y_train, X_train), axis=1).iloc[:, :15].corr()
  plt.figure(figsize=(15, 15))
  sns.set(font_scale=1)
  sns.heatmap(cor, annot=True, cmap=plt.cm.Blues)
  try:
    plt.savefig(saving_to);
  except:
    os.makedirs(os.path.dirname(saving_to))
    plt.savefig(saving_to);
  
if __name__ == "__main__":
    main(opt["--file_path"], opt["--out_dir"])
