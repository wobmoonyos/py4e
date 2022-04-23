# import method from http://net-informations.com/ds/pda/multiple.htm

import pandas as pd
import numpy as np
import glob
# What is you folder path?
path = r'C:/Users/14253/Desktop/py4e/Bulk_Read'
# What is your data type and naming pattern?
all_files = glob.glob(path + "/*.csv")
# Where should the unformatted data go?
df_files = (pd.read_csv(f) for f in all_files)
# This is where you will store the formatted data/dataframe:
df   = pd.concat(df_files, ignore_index=True)
