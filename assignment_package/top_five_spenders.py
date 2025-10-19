import pandas as pd

def top_five_spenders(df) -> list:
    """Returns the tiop 5 custoemrs who spent the most money according to the input dataframe."""
    df = df.copy()

    grouped = df.groupby("CustomerID", as_index=False).agg({"amount_spent" :"sum"})
    sorted_spenders = grouped.sort_values(by="amount_spent", ascending=False)

    return sorted_spenders[:5]["CustomerID"].tolist()

