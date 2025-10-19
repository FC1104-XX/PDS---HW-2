import pandas as pd
from top_five_cust import top_five_cust

def average_age(df, customers) -> float:
    """Returns the average age of the top 5 customers according to the customer information and retail dataframes."""
    df = df.copy()
    customers = customers.copy()

    top_5 = top_five_cust(df)
    customers_top5_only = customers[customers["CustomerID"].isin(top_5)]

    return customers_top5_only["Age"].mean()

