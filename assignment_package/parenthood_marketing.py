import pandas as pd
from typing import List

def parenthood_marketing(df, customers) -> List[str]:
    """
    IF YOURE READING THIS, THIS ONE IS WRONG, YOUR VERSION is THE ONE WITH THE CORRECT JOIN TYPE.






    Returns the top 5 countries with customers who on average have more children according to the customer information and retail dataframes.   

    df = df.copy()
    customers = customers.copy()

    id_country = df[["CustomerID", "Country"]].drop_duplicates()
    merged = pd.merge(customers, id_country, on="CustomerID", how="left")

    parenthood_mean = (
        merged.groupby("Country")["NumChildren"]
        .mean()
        .sort_values(ascending=False)
    )

    return parenthood_mean.head(5).index.tolist()
    """
    pass
