import pandas as pd

def date_handler(df) -> pd.DataFrame:
    """Returns the input dataframe without any invoices from the year 2011."""
    df=df.copy()

    df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"], errors="coerce")

    invalid = df[df["InvoiceDate"].isna()] #check if any date rows couldn't be parsed and were converted to NaT
    if not invalid.empty:
        print("Some rows could not be converted to datetime:")
        print(invalid)

    df = df[df["InvoiceDate"].dt.year != 2011]
    return df
