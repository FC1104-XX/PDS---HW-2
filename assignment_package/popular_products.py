import pandas as pd
from typing import List

def popular_products(df) -> List[str]:
    """Return the top 5 most frequently bought items from the input dataframe."""
    df = df.copy()
    df = df[df["StockCode"].astype(str).str.isnumeric()] #so we only get valid orders and avoid 'POSTAGE', 'Manual' etc. since we want an actual item 

    description_counts = df["Description"].value_counts()

    return description_counts.head(5).index.tolist()
