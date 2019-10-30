Step 1: Calculate the royalties of each sales for each author
select tau.title_id as TITLEID, tau.au_id as AUTHORID, (titles.price * sales.qty * titles.royalty / 100 * tau.royaltyper / 100) as Royalty
from titleauthor as tau
join titles
on tau.title_id = titles.title_id
join sales
on sales.title_id = titles.title_id
;

Step 2: Aggregate the total royalties for each title for each author
select TITLEID, AUTHORID, sum(Royalty) as AGGREGATED
from
(select tau.title_id as TITLEID, tau.au_id as AUTHORID, (titles.price * sales.qty * titles.royalty / 100 * tau.royaltyper / 100) as Royalty
from titleauthor as tau
join titles
on tau.title_id = titles.title_id
join sales
on sales.title_id = titles.title_id) as STEPU
group by TITLEID, AUTHORID
;

Step 3: Calculate the total profits of each author
select TITLEID, AUTHORID, COALESCE(sum(ROYALTY),0) as AGGREGATED
from
(select tau.title_id as TITLEID, tau.au_id as AUTHORID, (titles.price * sales.qty * titles.royalty / 100 * tau.royaltyper / 100) as ROYALTY
from titleauthor as tau
left join titles
on tau.title_id = titles.title_id
left join sales
on sales.title_id = titles.title_id) as STEPU
group by AUTHORID, TITLEID
;

Challenge 2;

create temporary table PROFIT_AUTHORS
select tau.title_id as TITLEID, tau.au_id as AUTHORID, (titles.price * sales.qty * titles.royalty / 100 * tau.royaltyper / 100) as ROYALTY, titles.advance as ADVANCE
from titleauthor as tau
left join titles
on tau.title_id = titles.title_id
left join sales
on sales.title_id = titles.title_id
;

Challenge 3
select AUTHORID, AGGREGATED as PROFTIS
from
(select TITLEID, AUTHORID, COALESCE(sum(ROYALTY+ADVANCE),0) as AGGREGATED
from
(select tau.title_id as TITLEID, tau.au_id as AUTHORID, (titles.price * sales.qty * titles.royalty / 100 * tau.royaltyper / 100) as ROYALTY, titles.advance as ADVANCE
from titleauthor as tau
left join titles
on tau.title_id = titles.title_id
left join sales
on sales.title_id = titles.title_id) as STEPU
group by AUTHORID, TITLEID) as STEPTWO
;