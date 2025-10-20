import pandas as pd
from typing import List

def most_active(customers) -> List[str]:
    """Returns a list of the customers who have been active for the longest according to the customers dataframe."""
    customers = customers.copy()

    most_active_customers = customers[customers["YearsActive"] == customers["YearsActive"].max()]

    return most_active_customers["Email"].sort_values().tolist() #sorted so me and my assignment partner can compare values
