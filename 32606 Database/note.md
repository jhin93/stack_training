
### SQL grammar

- Creating table with file

\i (file name).{file type};
<!-- 
\i pizza.txt; 
-->

- Retrieve every table

\d 


- Retrieve specific table

\d (table name);

<!-- 
\d menu; 
-->

- Display every data from speicific table

select * from (table name)

<!-- 
select * from menu;
 -->

- Filtering example 1

postgres=# select pizza, country, price from menu order by country, price;
   pizza    | country | price 
------------+---------+-------
 hawaiian   | hawaii  |   7.4
 margarita  | italy   |   6.2
 siciliano  | italy   |   7.4
 napolitana | italy   |   7.4
 cabanossi  | italy   |   7.4
 stagiony   | italy   |   7.8
 mexicano   | mexico  |   7.4
 americano  | usa     |   7.4
 garlic     |         |   3.5
 mushroom   |         |   7.3
 ham        |         |   7.3
 vegetarian |         |   7.4
 seafood    |         |   9.2
 special    |         |   9.9
(14 rows)

postgres=# 

