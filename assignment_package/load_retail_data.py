import pandas as pd

def load_retail_data(filepath: str) -> pd.DataFrame:
    """Returns the onlineretail dataframe if the provided directory path to the csv is valid, otherwise it raises an error.
    - If using global Windows paths, prefix string with 'r'"""
    try:
        safepath = filepath.strip().replace("\\", "/") # to handle different types of filepaths and backspaces at the ends
        return pd.read_csv(safepath, encoding="latin-1")
    except Exception as error_class:
        print(load_retail_data.__doc__) #to also get the Windows path warning with the error
        raise ValueError("Invalid input") from error_class

