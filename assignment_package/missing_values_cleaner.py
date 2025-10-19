import pandas as pd

def missing_values_cleaner(df) -> pd.DataFrame:
    """Returns the input dataframe with all rows corresponding to a null 'CustomerID' or 'Description' value removed."""
    df = df.copy()

    mask = ~(df["CustomerID"].isna() | df["Description"].isna()) #creates True or False mask for our condition
    df = df[mask] #keeps only True, thats why we use the NOT operator previously

    return df

