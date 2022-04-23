# Batch processing from "How to read multiple csv files in python | for-loop + 2 more"
# Working with many files in

import pandas as pd
import csv
import numpy as np
import matplotlib.pyplot as plt
import glob


path = "C:/Users/14253/Desktop/py4e/"

all_files = glob.glob(path+"*.csv")

print(all_files)

df = [pd.read_csv(filename,index_col=0,header=0) for filename in all_files]

df = pd.DataFrame(df)

df.to_csv('C:/Users/14253/Desktop/py4e/bulk_analysis_outfile.csv')
