# Modules for data processing
import pandas as pd
import numpy as np
import os
import re
import sys
from datetime import datetime
import calendar

# ########################################################################
# ### analyze_dataset
# ########################################################################
# #
# # Simple function to help quickly analyze information & usability of
# # a dataset. Provides information about shape, null values, unique
# # values & basic statistical features.
# #
# # Inputs:
# #   1.  df_path (string) -> Dataset path (if available)
# #   2.  df (pandas dataframe) -> Dataset (if available)
# #   3.  direct_df (boolean) -> Whether dataset path or dataset is
# #       being provided
# #   4.  processing_func (function) -> If dataset needs to be processed
# #       before analyzing
# #   5.  Other arguments for pd.read_csv(...) if dataset path is being
# #       provided
# #
# # Return:   Either dataframe itself (if path provided) or head of
# #           dataframe (if dataframe provided)
# #
# ########################################################################

def analyze_dataset(df_path = None, df = None, direct_df = False, processing_func = lambda x: x, **read_csv_args):
    
    if(direct_df == False):
        df = pd.read_csv(df_path, **read_csv_args)
    df = processing_func(df)
    
    num_rows, num_cols = df.shape
    dtypes = dict(df.dtypes.items())
    print("*****************")
    print("Basic Info:")
    print("*****************\n")
    print(f"Shape of Dataset: {num_rows} rows, {num_cols} cols")
    print("Columns:")
    for col_idx, col in enumerate(df.columns):
        print(f"\t{col_idx+1}. {col}\n\t\t\t\t\t\t\t\t{dtypes[col]}")
    
    print("\n\n\n*****************")
    print("Null Values:")
    print("*****************\n")
    nulls = pd.isnull(df).sum()
    print(f"Total Nulls: {nulls.sum()}")
    nulls = nulls[nulls > 0]
    nulls = list(sorted(nulls.items(), key = lambda x: x[1], reverse = True))
    print("Columns with missing values:")
    for col_idx, (col_name, col_missin_num) in enumerate(nulls):
        print(f"\t{col_idx + 1}. {col_name}\n\t\t\t\t\t\t\t\t{col_missin_num} missing ({col_missin_num / num_rows * 100:.1f}%)")
    
    print("\n\n\n*****************")
    print("Column-specific:")
    print("*****************\n")
    print("Unique values in columns:")
    idx = 1
    for col in df.columns:
        nunique = df[col].nunique()
        if(nunique < 10):
            unique_vals = ["'" + str(x) + "'" for x in df[col].unique()]
            print(f"{idx}. {col} has {nunique} unique values")
            idx += 1
            print(f"\t[ {', '.join(unique_vals)} ]")
    print("\n\nStatistical Features:")
    print(df.describe())
    
    print("\n\n")
    if(direct_df == True):
        return df.head()
    else:
        return df