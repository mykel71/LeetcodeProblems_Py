import pandas as pd

def employee_bonus(employee: pd.DataFrame, bonus: pd.DataFrame) -> pd.DataFrame:
    employee_bonus = pd.merge(employee, bonus, on='empId', how='left')
    employee_bonus_filtered = employee_bonus[(employee_bonus['bonus'] < 1000) | (employee_bonus['bonus'].isna)]
    return employee_bonus_filtered[['name', 'bonus']]