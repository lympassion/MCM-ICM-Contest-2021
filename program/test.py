import pandas as pd
d=[[11,21,31,41],[52,62,72,82]]
index=["one","two"]
df=pd.DataFrame(d, index=index)
print("columns:", df.columns)
print("index:", df.index)
print(df)
print (df.loc["one"])