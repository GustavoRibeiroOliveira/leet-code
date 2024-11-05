-- 1757. Recyclable and Low Fat Products
SELECT product_id FROM Products WHERE low_fats = 'Y' AND recyclable = 'Y';

-- 584. Find Customer Referee
SELECT name FROM Customer WHERE (referee_id != '2' OR referee_id IS NULL);

-- 595. Big Countries
SELECT name, population, area FROM World WHERE area >= 3000000 OR population >= 25000000;

-- 1148. Article Views I
SELECT DISTINCT author_id as id FROM Views WHERE author_id = viewer_id ORDER BY id ASC;

-- 1683. Invalid Tweets
SELECT tweet_id FROM Tweets WHERE LENGTH(content) > 15

-- 1378. Replace Employee ID With The Unique Identifier
SELECT IFNULL(uni.unique_id, NULL) as unique_id, name from Employees as e LEFT JOIN EmployeeUNI as uni on e.id = uni.id

-- 1068. Product Sales Analysis I
SELECT p.product_name, s.year, s.price FROM Sales as s INNER JOIN Product as p on p.product_id = s.product_id

-- 1581. Customer Who Visited but Did Not Make Any Transactions
SELECT v.customer_id, count(v.visit_id) as count_no_trans FROM Visits as v LEFT JOIN Transactions as t on
    v.visit_id = t.visit_id WHERE t.transaction_id IS NULL GROUP BY v.customer_id

-- 197. Rising Temperature
SELECT today.id as Id FROM Weather as yesterday CROSS JOIN Weather as today WHERE
    DATEDIFF(today.recordDate,yesterday.recordDate) = 1 AND today.temperature > yesterday.temperature

-- 1661. Average Time of Process per Machine
SELECT  A.machine_id, ROUND(AVG(B.timestamp - A.timestamp), 3) AS processing_time FROM Activity A JOIN Activity B
    ON A.machine_id = B.machine_id AND A.process_id = B.process_id AND A.activity_type != B.activity_type
    WHERE A.activity_type = 'start' GROUP BY A.machine_id;