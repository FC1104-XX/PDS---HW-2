import pandas as pd
from go_sports import go_sports

def go_manager(teams, managers) -> str:

   # Step 1: Build the sports DataFrame
    sports = go_sports(teams, managers)


