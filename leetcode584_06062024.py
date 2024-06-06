import pandas as pd

def find_customer_referee(customer: pd.DataFrame) -> pd.DataFrame:
    customer_final = customer[(customer['referee_id'] != 2) |(customer['referee_id'].isnull())]
    return customer_final[['name']]