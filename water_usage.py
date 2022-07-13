"""This script is done with the intention to read the water usage of multiple areas in 6 months which are recorded over 50 excel files and aggregate that
reading in one place."""

def  water_usage(filepath): #filepath should be in a raw string format
  import pandas as pd
  import os
  import glob
  from openpyxl import load_workbook

  df = pd.DataFrame()

  filenames = glob.glob(filepath + "\*.xlsx")

  # for loop to iterate all excel files 
  for file in filenames:
    print(f"READING:{file}")
    #formatting string variable as raw string
    file=r"{}".format(file)
    # reading excel files
    read_data=pd.read_excel(file,"Production Output",usecols=["Date","Water Usage (L)"])
    df = pd.concat([df, read_data],verify_integrity=True,ignore_index=True)
  
  #saving dataframe as a csv file  
  df.to_csv('Water Usage.csv',encoding='utf-8', index=False)
        
water_usage(r"C:\Users\owner\Documents\Cycle 14")
