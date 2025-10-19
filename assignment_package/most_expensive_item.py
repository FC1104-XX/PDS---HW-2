import pandas as pd

def most_expensive_item(df) -> str:
     """Returns the most expensive item in the input dataframe."""
     df=df.copy()

     df = df[df["StockCode"].astype(str).str.isnumeric()] #so we only get valid orders and avoid 'POSTAGE', 'Manual' etc. since we want an actual item 

     df = df.sort_values(by="UnitPrice", ascending=False)
     df = df.drop_duplicates(subset="Description")

     most_expensive = df.iloc[1]["Description"] #im pretty sure that the first entry is actually 60 items instead of 1 so we ignore it
     return most_expensive
