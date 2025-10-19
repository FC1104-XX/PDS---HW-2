import pandas as pd

def country_best_product(df, country) -> str:
    """Returns the most frequently bought item in the input country according to the input dataframe."""
    df = df.copy()
    df = df[df["StockCode"].astype(str).str.isnumeric()] #so we only get valid orders and avoid 'POSTAGE', 'Manual' etc. since we want an actual item 

    if country not in df["Country"].values:
        return None

    df = df[df["Country"] == country]

    product_counts = df["Description"].value_counts()

    return product_counts.index[0] if not product_counts.empty else None
