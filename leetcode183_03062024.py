import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    customerorders = pd.merge(customers, orders, left_on='id', right_on='customerId', how='left')
    no_orders = customerorders[customerorders['id_y'].isnull()]
    no_orders = no_orders.rename(columns={'name': 'Customers'})
    return no_orders[['Customers']]