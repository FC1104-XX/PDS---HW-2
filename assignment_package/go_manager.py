import pandas as pd
from go_sports import go_sports

def go_manager(teams, managers) -> str:
   """Returns the managerID of the manager with the most winds across his career according to the input dataframes."""
   # Step 1: Build the sports DataFrame
   sports = go_sports(teams, managers)
   sports["managerID"] = sports["managerID"].astype(str)

   grouped_managers = sports.groupby("managerID", as_index=False)
   manager_wins = grouped_managers["W"].sum()
   best = manager_wins.sort_values("W", ascending=False).iloc[0]["managerID"]

   return best


