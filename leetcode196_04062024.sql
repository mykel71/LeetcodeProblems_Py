WITH emails as (
    SELECT
        id,
        email,
        RANK() OVER (PARTITION BY email ORDER BY id) as email_rank
        FROM person
)
DELETE FROM person
WHERE id IN (
    SELECT id FROM emails WHERE email_rank > 1
)