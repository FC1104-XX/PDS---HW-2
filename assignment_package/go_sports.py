import pandas as pd

def go_sports(teams, managers) -> pd.DataFrame:
    """Returns a dataframe containing the team name, manager ID(s), yearID, wins and losses according to the teams and managers dataframes."""
    teams = teams.copy()
    managers = managers.copy()

    teams["yearID"] = pd.to_datetime(teams["yearID"], errors="coerce").dt.year
    managers["yearID"] = pd.to_numeric(managers["yearID"], errors="coerce").astype("Int64")

    managers["managerID"] = managers["managerID"].str.replace(" ", "", regex=False) #remove spaces

    managers = (
        managers.groupby(["teamID", "yearID", "managerID"], as_index=False)[["W", "L"]] #we have to do this to group the now cleaned managerIDs
        .sum())
    teams = teams[["teamID", "yearID", "name" ]]
    managers = managers[["teamID", "yearID", "managerID", "W", "L"]].drop_duplicates()

    final_df = pd.merge(
        teams,
        managers,   
        on=["teamID", "yearID"],
        how="inner"
    )
    final_df = final_df.sort_values(["teamID", "yearID", "managerID"])

    #to test: we should keep in mind a year of baseball has about 162 games, to check our answer we just had all games in a season and it seems to make sense
    return final_df[["name", "managerID", "yearID", "W", "L"]] 
