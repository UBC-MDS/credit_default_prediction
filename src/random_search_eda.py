# author: Arushi Ahuja
# date: 2021-11-24

'''This script generates all the EDA diagrams used in the final report 
  after model generation, specifically the random search diagram

Usage: random_search_eda.py --file_path=<file_path> --out_dir=<out_dir>

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
  random_search_scores_df = pd.read_csv(file_path)
  random_search_scores_df["param_logisticregression__C"] = random_search_scores_df["param_logisticregression__C"].apply(str)
  
  random_search_scores_df["param_logisticregression__C"] = random_search_scores_df["param_logisticregression__C"].apply(str)
  random_search_graph = alt.Chart(random_search_scores_df, title = "Random Search scores for different hyperparameters"
  ).mark_errorbar(extent='ci', rule=alt.LineConfig(size=2)
  ).encode( x=alt.X('param_logisticregression__C', title = "Hyperparamter C"),
            y= alt.Y('scores',scale= alt.Scale(zero= False), title = "F1 scores"),
            color = alt.Color("param_logisticregression__class_weight", title = "Class weights hyperparemter")
  ).properties(
    width=300,
    height=500)


  random_search_graph_final = random_search_graph + random_search_graph.mark_point(size=80).encode(y='mean(scores)')
  
  out_dir_random_search = out_dir + "random_search.png"
  random_search_graph_final.save(out_dir_random_search, scale_factor = 2.0)
  
if __name__ == "__main__":
    main(opt["--file_path"], opt["--out_dir"])
