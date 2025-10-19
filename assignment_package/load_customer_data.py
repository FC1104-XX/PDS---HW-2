import pandas as pd

def load_customer_data(filepath: str) -> pd.DataFrame:
    """Returns the customer info dataframe if the provided directory path to the csv is valid, otherwise it raises an error.
    - If using global Windows paths, prefix string with 'r'"""
    safepath = filepath.strip().replace("\\", "/") # to handle different types of filepaths and backspaces at the ends
    try:

        return pd.read_csv(safepath)
    except Exception as error_class:
        print(load_customer_data.__doc__) #to also get the Windows path warning with the error
        raise ValueError("Invalid input") from error_class
