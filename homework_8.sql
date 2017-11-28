-- HOMEWORK 8 
-- Julie Richardson

use sakila;

-- 1A:
select first_name, last_name
from actor;

-- 1B:
alter table actor
add column `Actor Name` varchar(70);
UPDATE actor SET `Actor Name`= CONCAT(first_name, ' ', last_name);

-- 2A:
select first_name, last_name, actor_id from actor
where actor.first_name="Joe";

-- 2B:
select * from actor 
where last_name like "%gen%";

-- 2C:
select last_name, first_name from actor
where last_name like "%li%";

-- 2D:
select country_id, country from country
where country.country in ("Afghanistan", "Bangladesh", "China");

-- 3A:
alter table actor
add column middle_name varchar(50) not null after first_name;

-- 3B: This one still isn't working :(((
-- alter table actor
-- modify column last_name longblob;
-- alter table actor change column middle_name middle_name blob;

-- 3C:
alter table actor 
drop middle_name;

-- 4A and 4B:
select last_name, count(last_name) from actor
group by last_name
having count(last_name) >1; -- remove this statement for 4A!

-- 4C: 
update actor
set first_name="HARPO"
where first_name="groucho" and last_name="williams";

-- 4D: 
update actor
set first_name="GROUCHO"
where first_name="harpo" and last_name="williams";  -- the instructions here were kind of confusing, but I took them to mean change HARPO
								-- to GROUCHO and change the first names of the other two actors with the last name Williams to MUCHO GROUCHO

update actor
set first_name="MUCHO GROUCHO"
where last_name="Williams" and first_name<>"harpo" and first_name<>"groucho";


-- 5A: 
show create table address;


-- 6A:
select b.first_name, b.last_name, address
from address a
join staff b using(address_id);

-- 6B:
select sum(amount), staff_id, first_name, last_name
from payment a
join staff b using(staff_id)
where payment_date like "2005-08%"
group by staff_id;

-- select * from payment
-- where staff_id=2;

-- 6C:
select count(actor_id), b.title
from film_actor a
inner join film b using(film_id)
group by film_id;

-- 6D:
select * from inventory_count
where title="Hunchback Impossible";

-- 6E:
select sum(a.amount), a.customer_id, b.first_name, b.last_name
from payment a
join customer b using(customer_id)
group by customer_id
order by b.last_name;

-- 7A;
select * from film
where title like"q%" or title like "k%"; -- Note that you don't need to filter out movies by language because the movies in this database
										-- are all in English!! (I checked)
                                        
-- 7B:
select actors from film_list
where title="Alone Trip";

-- 7C;
select a.first_name, a.last_name, a.email, d.country
from customer a
join address b
	 using(address_id)
join city c
	using(city_id)
join country d
	using(country_id)
where d.country="canada";



-- 7D:
select title, category from film_list
where category="Family";

-- 7E:
select title, count(title)
from rental a
join inventory b
	 using(inventory_id)
join film c
	using(film_id)
group by title
order by count(title) desc;




-- 7F:
select * from sales_by_store; -- this question is literally answered by the view??

-- 7G:
select a.store_id, c.city, d.country
from store a
join address b
	 using(address_id)
join city c
	using(city_id)
join country d
	using(country_id); 
    

            
-- 7H: category, film_category, inventory, payment, and rental
select * from sales_by_film_category
limit 5;

-- 8A:
-- Hopefully if I'm an executive I'd notice that there's already a view to do this for me :)  [sales_by_film_category]  
-- But I guess I can make an even BETTER view!!!

CREATE VIEW top_five_genres AS
SELECT category, total_sales
FROM sales_by_film_category
LIMIT 5;

-- 8B:
select * from top_five_genres;

-- 8C:
drop view top_five_genres;




-- select * from payment;

-- select sum(amount), staff_id, first_name, last_name
-- from payment a
-- join staff b using(staff_id)
-- where payment_date like "2005-08%"
-- group by staff_id;







-- select * from actor;
