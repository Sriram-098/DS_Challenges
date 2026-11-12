select round(sum(
    case
       when datediff(a2.event_date,a1.event_date)=1 then 1
       else 0
    end 
)/(select count(distinct player_id) from activity), 2) as fraction

from activity a1
join activity a2 on a1.player_id=a2.player_id
where a1.event_date = (select min(a3.event_date) from activity a3
               where a3.player_id=a1.player_id

);
