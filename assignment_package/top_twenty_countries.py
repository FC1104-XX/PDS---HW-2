import pandas as pd
from typing import List

def top_twenty_countries(df) -> List[str]:
  """Returns the 20 countries with the highest number of orders from the input dataframe."""
  df=df.copy()

  grouped = (
    df.groupby("InvoiceNo", as_index=False)
      .agg({
          "Country": "first"
      })
    )

  country_counts = grouped["Country"].value_counts()

  return_list = [country for country in country_counts.head(20).index]
  return return_list
