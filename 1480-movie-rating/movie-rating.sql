
(select users.name as results from movierating 
join users on movierating.user_id=users.user_id
group by movierating.user_id
order by count(*) desc ,users.name asc
limit 1)

union all

(select title as results from movierating 
join movies on movies.movie_id=movierating.movie_id
WHERE YEAR(movierating.created_at) = 2020 
  AND MONTH(movierating.created_at) = 2
  group by movierating.movie_id 
  order by avg(rating) desc ,title asc
  limit 1);




