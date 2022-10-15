import pandas as pd
import numpy as np

# reading csv file
# fd = pd.read_csv('sample4.csv', index_col=0)

# reading excel file
fd = pd.read_excel('sample2.xlsx', index_col=0)

# reading top 5 rows
print(fd.head(5))

# checking datatype
# print(type(fd))

# checking datatype of each column
# print(fd.dtypes)

# counting datatypes in file
# print(fd.dtypes.count())

# printing selected columns
# print(fd.select_dtypes(include=['float64']).head(5))

# printing column info
# print(fd.info())

# printing unqiue elements of column
# print(np.unique(fd['Creator']))
