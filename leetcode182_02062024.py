import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    counts = person.groupby('email').size().reset_index()
    counts.columns = ['email', 'count']
    duplicated_emails = counts[counts['count'] > 1]['email']
    return pd.DataFrame({'email': duplicated_emails})