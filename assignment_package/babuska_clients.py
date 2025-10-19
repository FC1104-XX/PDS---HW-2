import pandas as pd

def babuska_clients(df, customers) -> float:
    """Returns average age of the customers who bought a 'HAND WARMER BABUSHKA DESIGN' according to the customer information and retail dataframes."""
    df = df.copy()
    customers = customers.copy()

    babuska = df[df["Description"] == "HAND WARMER BABUSHKA DESIGN"]
    ids = babuska[["CustomerID", "InvoiceNo"]].drop_duplicates()
    babuska_customers = customers[customers["CustomerID"].isin(ids["CustomerID"])]
    avg_age = babuska_customers["Age"].mean()

    return avg_age



