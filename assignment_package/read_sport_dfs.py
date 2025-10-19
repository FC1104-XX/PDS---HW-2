import pandas as pd
from typing import Tuple

def read_sport_dfs(teams_filepath: str, managers_filepath: str) -> Tuple[pd.DataFrame]:
    """Returns the teams and managers dataframes if the provided directory path to the csv is valid, otherwise it raises an error.
    - If using global Windows paths, prefix string with 'r'"""
    safepath_teams = teams_filepath.strip().replace("\\", "/") # to handle different types of filepaths and backspaces at the ends
    safepath_managers = managers_filepath.strip().replace("\\", "/") 
    try:
        teams = pd.read_csv(safepath_teams)
        managers = pd.read_csv(safepath_managers)
    except Exception as error_class:
        print(read_sport_dfs.__doc__) #to also get the Windows path warning with the error
        raise ValueError("Invalid input") from error_class

    return teams, managers
