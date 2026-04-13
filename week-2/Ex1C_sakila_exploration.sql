/*
a) You have actor_id, first_name, last_name, last_update.
b) In this table we information of film, rental, rating and any updates date format.
c) The film_actor columns has actor_id and film_id.
d) In the rental table you have a record of who rented, what movie was rented, how long the movie was rented for, what associate did the trnasaction and when was the last update date format. This info is okay if the columns didn't have titles it would for sure be hard to understand what is going on.
e) The inventory table has iventory, store and film id as well as last update date format.
f) I would need to use the film, rental, and inventory columns table. This table has file_id and movie titles. The tables all connect, in film you can use the film_id for inventory in iventory_id, then you can use the inventory_id in the rental table.
*/

SELECT film_id, title FROM film;
SELECT inventory_id, film_id FROM inventory;
SELECT rental_date, inventory_id FROM rental;
