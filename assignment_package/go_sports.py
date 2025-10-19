import pandas as pd

def go_sports(teams, managers) -> pd.DataFrame:
    """Returns a dataframe containing the team name, manager ID(s), yearID, wins and losses according to the teams and managers dataframes."""
    teams = teams.copy()
    managers = managers.copy()

    teams["yearID"] = pd.to_datetime(teams["yearID"], errors="coerce").dt.year
    managers["yearID"] = pd.to_datetime(managers["yearID"], errors="coerce").dt.year
    managers["managerID"] = managers["managerID"].str.replace(" ", "", regex=False)

    managers_clean = (
        managers.sort_values(["teamID", "yearID", "W"], ascending=[True, True, False])
        .drop_duplicates(subset=["teamID", "yearID", "managerID"])
    )

    final_df = pd.merge(
        teams[["teamID", "yearID", "name"]],
        managers[["teamID", "managerID", "yearID", "W", "L"]],
        on=["teamID", "yearID"],
        how="inner"
    )

    return final_df
