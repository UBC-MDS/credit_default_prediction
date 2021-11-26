# author: Arushi Ahuja
# date: 2021-11-24

'''This script generates all the EDA diagrams used in the final report 
   before model generation

Usage: credit_card_default_eda.py --file_path=<file_path> --out_dir=<out_dir>

Options:
--file_path=<file_path>   Path to the data file
--out_dir=<out_dir>       Path (directory) to save the images
'''

import pandas as pd
import altair as alt
alt.renderers.enable('mimetype') 
alt.data_transformers.enable('data_server')
from docopt import docopt

opt = docopt(__doc__)

def main(file_path, out_dir):
  train_df_viz = pd.read_csv(file_path)
  train_df_viz["DEFAULT_PAYMENT_NEXT_MONTH"] = train_df_viz["DEFAULT_PAYMENT_NEXT_MONTH"].apply(str)
  
  histogram_numeric_feat = alt.Chart(train_df_viz).mark_bar(opacity = 0.8).encode(
     alt.X(alt.repeat(), type='quantitative', bin=alt.Bin(maxbins=40), scale= alt.Scale(zero= False)),
     y=alt.Y('count()', stack = False),
     color = alt.Color("DEFAULT_PAYMENT_NEXT_MONTH", title = "Default next month")
     ).properties(
       width=200,
       height=200
       ).repeat(
         ["LIMIT_BAL", "AGE", "BILL_AMT1", "BILL_AMT2", "BILL_AMT3", 
         "BILL_AMT4", "BILL_AMT5", "BILL_AMT6",
         "PAY_AMT1",  "PAY_AMT2",  "PAY_AMT3", "PAY_AMT4",
         "PAY_AMT5", "PAY_AMT6"],
         columns =4
         )
  out_dir_numeric = out_dir + "histogram_numeric_feat.png"
  histogram_numeric_feat.save(out_dir_numeric, scale_factor = 2.0)
  
  categorical = ["EDUCATION", "MARRIAGE", "PAY_0", "PAY_2", "PAY_3", "PAY_4", "PAY_5", "PAY_6"]
  categorical_graph = []

  for i in range(len(categorical)):
      train_df_viz[categorical[i]] = train_df_viz[categorical[i]].apply(str)
      cate = alt.Chart(train_df_viz).mark_bar().encode(
         y= "count()",
         x = categorical[i],
          color = alt.Color("DEFAULT_PAYMENT_NEXT_MONTH", title = "Default next month")
      )
      categorical_graph.append(cate)

  categorical_feat_graph = (categorical_graph[0] & categorical_graph[1] & categorical_graph[2]) | (categorical_graph[3] & categorical_graph[4] & categorical_graph[5]) | (categorical_graph[6] & categorical_graph[7])
  
  out_dir_categorical = out_dir + "categorical_feat_graph.png"
  categorical_feat_graph.save(out_dir_categorical, scale_factor = 2.0)
  
if __name__ == "__main__":
    main(opt["--file_path"], opt["--out_dir"])
