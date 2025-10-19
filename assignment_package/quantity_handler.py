import pandas as pd

def quantity_handler(df) -> pd.DataFrame:
    """Returns the input dataframe stripped of rows with negative or null values in the 'Quantity' column."""
    df = df.copy()

    df=df[df["Quantity"] > 0]
    return df
