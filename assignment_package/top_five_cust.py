import pandas as pd

def top_five_cust(df) -> list:
  """Returns the top 4 customer who have placed the highest number of orders from the input dataframe."""

  df = df.copy()

  grouped = (
    df.groupby("InvoiceNo", as_index=False)
      .agg({
          "CustomerID": "first",
          "InvoiceDate": "first",
          "Description": lambda x: list(x),
          "Country": "first",
          "Quantity": "sum",
          "amount_spent": "sum"
      })
    )

  orders_per_customer = grouped["CustomerID"].value_counts() #value_counts autmoatically counts and SORTS in descending order so we can just grab the head

  return_list = [customer for customer in orders_per_customer.head(5).index]

  return return_list


