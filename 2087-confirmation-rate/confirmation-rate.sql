# Write your MySQL query statement below
select signups.user_id ,round(ifnull(sum(confirmations.action="confirmed")/count(confirmations.action),0),2) as confirmation_rate from signups
left join confirmations on signups.user_id =confirmations.user_id
group by user_id;
