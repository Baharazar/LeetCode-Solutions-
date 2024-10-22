# Write your MySQL query statement below
select V.customer_id , count(v.visit_id) as count_no_trans 
from Visits V left join transactions T on V.visit_id = T.visit_id
where T.transaction_id is Null
group by v.customer_id