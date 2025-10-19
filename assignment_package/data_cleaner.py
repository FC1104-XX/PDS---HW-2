import pandas as pd
from missing_values_cleaner import missing_values_cleaner
from quantity_handler import quantity_handler
from amount_spent_computer import amount_spent_computer
from date_handler import date_handler

def data_cleaner(df) -> pd.DataFrame:

    """

    This function receives a Pandas DataFrame as input.

    First, pass the input DataFrame `df` to the `missing_values_cleaner`
    function, and store its output in a new variable called `clean`.
    Then, pass `clean` to the `quantity_handler` function and store its
    output (you may reuse the variable name `clean`).

    Next, pass the resulting DataFrame to the `amount_spent_computer`
    function, and then to the `date_handler` function. Finally, return
    the fully cleaned DataFrame.

    """
    df=df.copy()

    clean = missing_values_cleaner(df)
    no_negative_quantities = quantity_handler(clean)
    df_amount_spent = amount_spent_computer(no_negative_quantities)
    no_2011 = date_handler(df_amount_spent)

    return no_2011
