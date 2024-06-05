import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    activity['login_rank'] = activity.groupby('player_id')['event_date'.rank(method='mean')]
    final_rank = activity[activity['login_rank'] == 1]
    final_rank = final_rank.rename(columns={'event_date': 'first_login'})
    return final_rank[['player_id','first_login']]