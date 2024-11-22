# Write your MySQL query statement below
SELECT V.customer_id, COUNT(T.transaction_id is NULL) AS count_no_trans
FROM Visits V
LEFT OUTER JOIN Transactions T ON T.visit_id = V.visit_id
WHERE t.transaction_id IS NULL
GROUP BY V.customer_id;
