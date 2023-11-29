# DataFrames not posible with singlwe dimentional array  
import pandas as pd 
import numpy as np

numarray = np.array([[1,2,3,4],[5,6,7,8]])
dfobj = pd.DataFrame(numarray,index=[1,2],columns=["column1","column2","column3","column4"])
print("the df object \n",dfobj)

array1 = np.array(["nani","vijju","sowji","pawan"])
array2 = np.array([11,12,13,14])

stdfobj = pd.DataFrame((array1,array2),index=[1,2],columns=["st1","st2","st3","st4"])
print("the DataFrame create string array : \n",stdfobj)

# =================================================================================================
import pandas as pd

# Creating a Series
s = pd.Series([1, 3, 5, np.nan, 6, 8])
print("Series:")
print(s)
print("\n")

# Creating a DataFrame with dict
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emily'],
    'Age': [25, 30, 35, 22, 28],
    'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago', 'Boston']
}

df = pd.DataFrame(data)
print("DataFrame:")
print(df)
