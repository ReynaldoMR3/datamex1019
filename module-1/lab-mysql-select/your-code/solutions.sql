Challenge # 1

select sec.author_ID, sec.last_name, sec.first_name, sec.titles, pub.pub_name as publishers
from
(select prim.author_ID, prim.last_name, prim.first_name, t.title as titles, t.pub_id
from
(select au.au_id as author_ID, au.au_lname as last_name, au.au_fname as first_name, tau.title_id as title_id
from authors as au
left join titleauthor as tau
on au.au_id = tau.au_id) as prim
left join titles as t
on prim.title_id = t.title_id) as sec
left join publishers as pub
on sec.pub_id = pub.pub_id
;

Challenge # 2
select AUTHORID, LASTNAME, FIRSTNAME, PUBLISHERS, count(title) as Count_Titles from(
SELECT au.au_id as AUTHORID, au.au_lname as LASTNAME, au.au_fname as FIRSTNAME, t.title as TITLE, 
p.pub_name as PUBLISHERS
from 
authors as au
left join titleauthor as tau
on au.au_id = tau.au_id
inner join titles t
on tau.title_id=t.title_id
inner join publishers p
on t.pub_id= p.pub_id) PRIMERA
group by AUTHORID, PUBLISHERS;

Challenge 3 - Best Selling Authors
select au.au_id as AUTHORID, au.au_lname as LASTNAME, au.au_fname as FIRSTNAME, sum(sal.qty) as TOTAL
from authors au
inner join titleauthor as tau
on au.au_id = tau.au_id
inner join sales as sal
on tau.title_id = sal.title_id
group by AUTHORID
order by TOTAL desc
limit 3 
;

Challenge 4 - Best Selling Authors Ranking
select au.au_id as AUTHORID, au.au_lname as LASTNAME, au.au_fname as FIRSTNAME, COALESCE(sum(sal.qty),0) as TOTAL
from authors au
left join titleauthor as tau
on au.au_id = tau.au_id
left join sales as sal
on tau.title_id = sal.title_id
group by AUTHORID
order by TOTAL desc
;