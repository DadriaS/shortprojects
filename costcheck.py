"""This file is used to get the costs periodally whcich ae enterd by the data entry clerk. I use to as a way of check the completness of the information entered. """

def costcheck(filepath):
    import pandas as pd
    import os
    import glob
    from openpyxl import load_workbook

    df = pd.DataFrame()
    filepath = glob.glob(filepath + "\*.xlsx")

    for file in filepath:
        file=r"{}".format(file)
        try:
            pd.read_excel(file,"Production Output")
            print(f"Found sheet in {file}")
        except ValueError:
            print(f"No sheet found in {file} with that name.")
    print ("Done")
    

    
    #check each file for costs total (use if/in)
    for file in filepath:
        data=pd.read_excel(file,"Production Output")
        file=r"{}".format(file)
        print(f"""Reading the cost in {file}
        
        """)
        for col in data.columns:
            if "cost" in col.lower() or "energy" in col.lower() or "in litres" in col.lower():
                col=pd.read_excel(file,"Production Output",usecols=[col])
                #entire column is parsed one by one. Ensure columns consistency is in files. Delete summation rows
                sumcol=col.sum(axis=0)
                print(f"The sum of {col.columns} on {file} is {sumcol}") 
                    
    print ("Done")
