import pandas as pd

def amount_spent_computer(df) -> pd.DataFrame:
    """Return the input dataframe with a new column 'amount_spent' by multiplying the 'Quantity' and 'UnitPrice' columns"""
    df = df.copy()

    df["amount_spent"] = df["Quantity"] * df["UnitPrice"]
    return df
