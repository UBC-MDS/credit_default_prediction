# Adapted from code draft by Tiffany Timbers
# Author: Lianna Hovhannisyan, Karanpreet Kaur
# date: 2021-11-19

"""Downloads xls data from the web to a local filepath as csv file.

Usage: src/download_data.py --out_type=<out_type> --url=<url> --out_file=<out_file>

Options:
--out_type=<out_type>    Type of file to write locally (script supports only csv)
--url=<url>              URL from where to download the data (must be in standard xls format)
--out_file=<out_file>    Path (including filename) of where to locally write the file
"""
  
from docopt import docopt
import requests
import os
import pandas as pd

opt = docopt(__doc__)

def main(out_type, url, out_file):
  try: 
    request = requests.get(url)
    request.status_code == 200
  except Exception as req:
    print("Website at the provided url does not exist.")
    print(req)
    
  data = pd.read_excel(url, header=1)
  if out_type == "csv":
    try:
      data.to_csv(out_file, index = False, encoding='utf-8')
    except:
      os.makedirs(os.path.dirname(out_file))
      data.to_csv(out_file, index = False, encoding='utf-8')

if __name__ == "__main__":
  main(opt["--out_type"], opt["--url"], opt["--out_file"])
