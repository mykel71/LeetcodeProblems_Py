
WITH rank_login as (
    SELECT 
    player_id
    ,event_date
    ,RANK () OVER (PARTITION BY player_id ORDER BY event_date) as login_rank
FROM Activity
)
SELECT
    player_id,
    event_date as first_login
FROM rank_login
WHERE login_rank = 1