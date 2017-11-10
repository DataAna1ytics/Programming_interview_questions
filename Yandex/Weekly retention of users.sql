#server creation
use sql2197771; #using of a database

CREATE TABLE YourTable
(
  user_id INT NOT NULL,
  order_datetime DATETIME NOT NULL,
  order_id INT NOT NULL
);
INSERT INTO YourTable VALUES
  (123, '2017-09-01 090000', 987),
  (131, '2017-09-01 093000', 989),
  (231, '2017-09-02 100000', 998),
  (123, '2017-09-02 090000', 997),
  (123, '2017-09-03 103000', 978),
  (122, '2017-09-03 110000', 999),
  (133, '2017-09-04 120000', 887),
  (132, '2017-09-05 123000', 777),
  (231, '2017-09-06 130000', 887),
  (313, '2017-09-07 133000', 897),
  (233, '2017-09-08 140000', 879),
  (233, '2017-09-09 143000', 888);  

#weekly retention of users
SELECT user_id, count(user_id) FROM YourTable
WHERE order_datetime BETWEEN '2017-09-01 000000' AND '2017-09-07 235959'
GROUP BY user_id HAVING count()1;