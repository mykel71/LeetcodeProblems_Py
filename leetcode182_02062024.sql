
with tot_emails as (
    SELECT
        email, COUNT(*) as email_count
    FROM Person
    GROUP BY email
)
SELECT email
FROM tot_emails
WHERE email_count > 1;