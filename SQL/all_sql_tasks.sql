/*
 1.1 Write a SQL query to find the 15th player with the largest amount of "Trophies" earned
in-game from a Players table. Assume that there are hundreds of records in this table.
Explain your answer.
 */

SELECT PlayerName, Trophies
FROM Players
ORDER BY Trophies DESC
LIMIT 1 OFFSET 14;

/*
 Explanation:
After we have selected the PlayerName, Trophies columns from the Players table, we sort the Players table by the Trophies column to get the top players.
After that, we set the limit of players for withdrawal: LIMIT 1
and skip the first 14: OFFSET 14;
 */

/*
 1.2 Now consider a table Gamers with the following columns: PLAYER_ID, INSTALL_DATE,
GAME, COUNTRY, DEVICE, TOTAL_AMOUNT_SPENT.
(a) Write a query to display the last 3 records of the table (by using the INSTALL_DATE
 */

SELECT *
FROM Gamers
ORDER BY INSTALL_DATE DESC
LIMIT 3;
/*
 This query will retrieve the last 3 records based on the descending order of the INSTALL_DATE field.
 */

/*
 (b) Write a query that returns the top 3 spenders by country
 */
SELECT COUNTRY, SUM(TOTAL_AMOUNT_SPENT) AS TotalSpent
FROM Gamers
GROUP BY COUNTRY
ORDER BY TotalSpent DESC
LIMIT 3;
/*
 To return the top 3 spenders by country from the Gamers table,
 you can use the GROUP BY and ORDER BY clauses along with the LIMIT keyword
 */


/*
 1.3 You have been provided with two tables: "Employees" and "Projects." Your task is to
write SQL queries to extract specific information based on the given requirements.
Table: Employees
Columns:
• employee_id (integer, primary key)
• employee_name (text)
• department_id (integer
• department_id (integer)
• salary (numeric)
Table: Projects
Columns:
• project_id (integer, primary key)
• project_name (text)
• start_date (date)
• end_date (date)
(a) Write a query to retrieve the names of all employees who earn a salary higher than
the average salary of their respective departments.
 */

SELECT e.employee_name
FROM Employees e
WHERE e.salary > (SELECT AVG(e2.salary)
FROM Employees e2
WHERE e2.department_id = e.department_id);
/*
 In this query, the subquery calculates the average salary (AVG) for each department by
 filtering the Employees table based on the department_id.
 Then, the main query retrieves the employee_name from the Employees table
 and compares their salary with the respective department's average salary.
 Only the employees with a higher salary are returned in the result.
 */

/*
 (b) Write a query to retrieve the project names along with the number of employees
working on each project.
 */
SELECT p.project_name, COUNT(e.employee_id) AS num_employees
FROM Projects p
JOIN Employees e ON p.project_id = e.project_id
GROUP BY p.project_name;
/*
 In this query, the JOIN combines the Employees and Projects tables based on the project_id column.
 The GROUP BY clause groups the results by project_name.
 The COUNT function is used to count the number of employees (by counting the employee_id) for each project.
 The result will include the project_name along with the corresponding number of employees working on that project.
 */

/*
 (c) Write a query to calculate the total duration (in days) of each project.
 */
SELECT project_name, DATEDIFF(end_date, start_date) AS total_duration
FROM Projects;
/*
 In this query, the DATEDIFF function is used to calculate the difference in days
 between the end_date and start_date columns for each project.
 The result will include the project_name along with the corresponding total_duration in days for each project.
 */

/*
 (d) Write a query to retrieve the names of employees who are not assigned to any
project.
 */

SELECT employee_name
FROM Employees
LEFT JOIN Projects ON Employees.employee_id = Projects.employee_id
WHERE Projects.project_id IS NULL;

/*
 In this query, the LEFT JOIN combines the Employees and Projects tables based on the employee_id column.
 By checking for NULL in the project_id column of the Projects table,
 we can identify the employees who are not assigned to any project.
 The result will include the names of employees who meet this condition.
 */

/*
 (e) Write a query to retrieve the department name(s) with the highest average salary
 */

SELECT department_id
FROM Employees
GROUP BY department_id
HAVING AVG(salary) = (
    SELECT MAX(avg_salary)
    FROM (
        SELECT AVG(salary) AS avg_salary
        FROM Employees
        GROUP BY department_id
    ) AS avg_salaries
);
/*
 The condition says to find department name(s),
 but in the Employees table we don't have a department_name field, I used department_id to identify the department

 In this query, i group the employees by department_id and calculate the average salary for each department.
 The HAVING clause filters the groups based on the average salary,
 selecting only those groups where the average salary is equal to the maximum average salary calculated in the subquery.
 */

/*
1.4 You have been provided with a table named "Orders" that contains information about
customer orders. Your task is to write SQL queries using window functions to extract specific
information based on the given requirements.
Table: Orders
Columns:
• order_id (integer, primary key)
• customer_id (integer)
• order_date (date)
• total_amount (numeric)
(a) Write a query to retrieve the order_id, customer_id, and total_amount for each order,
along with the total_amount of the customer's highest order
 */

SELECT o.order_id, o.customer_id, o.total_amount, MAX(o.total_amount) OVER (PARTITION BY o.customer_id) AS highest_total_amount
FROM Orders o;

/*
 In this query, the MAX() window function is used with the OVER clause
 to calculate the highest total_amount for each customer.
 The PARTITION BY clause is used to partition the data by customer_id,
 so the maximum total_amount is calculated separately for each customer.
 The result includes the order_id, customer_id, total_amount for each order,
 and the highest_total_amount for each customer.
 */

 /*
  (b) Write a query to calculate the cumulative total_amount for each order, starting from
the earliest order_date to the latest.
  */
SELECT order_id, customer_id, order_date, total_amount, SUM(total_amount) OVER (ORDER BY order_date) AS cumulative_total
FROM Orders
ORDER BY order_date;

/*
 In this query, the SUM() window function is used with the OVER clause to calculate the cumulative total_amount.
 The ORDER BY clause is used to order the rows based on the order_date,
 ensuring that the cumulative total_amount is calculated in the desired order.
 The result includes the order_id, customer_id, order_date, total_amount for each order,
 and the cumulative_total representing the cumulative sum of total_amount.
 */

/*
 (c) Write a query to calculate the average total_amount for each customer, considering
only their orders placed within the last 30 days.
 */

SELECT order_id,
       customer_id,
       order_date,
       total_amount,
       AVG(total_amount) OVER (PARTITION BY customer_id ORDER BY order_date RANGE BETWEEN INTERVAL '30' DAY PRECEDING AND CURRENT ROW) AS average_amount
FROM Orders
ORDER BY customer_id, order_date;

/*
 In this query, the AVG() window function is used with the OVER
 clause to calculate the average total_amount for each customer.
 The PARTITION BY clause is used to partition the data by customer_id,
 and the ORDER BY clause is used to order the rows by order_date.
 The RANGE BETWEEN clause specifies the range of rows to consider,
 which is from 30 days preceding the current row to the current row.

 */

 /*
  (d) Write a query to retrieve the customer_id, order_date, and total_amount for the top 3
orders with the highest total_amount.
  */

SELECT customer_id, order_date, total_amount
FROM (
    SELECT customer_id, order_date, total_amount, ROW_NUMBER() OVER (ORDER BY total_amount DESC) AS row_num
    FROM Orders
) AS ranked_orders
WHERE row_num <= 3;

/*
 In this query, the inner subquery assigns a row number to each order based on the total_amount
 in descending order using the ROW_NUMBER() function and the ORDER BY clause. The outer query
 then selects the customer_id, order_date, and total_amount from the ranked_orders subquery,
 limiting the result to the top 3 orders (row_num <= 3) with the highest total_amount.
 */



/*
 1.5 You have access to a database with the following schema
 Session
- user_id: int
- event_date: datetime
- session_id: int
- last_session_length (ms): int
Match
- user_id: int
- event_date: datetime
- session_id: int
- match_won: bool
- match_length (ms): int

 Each row in the Session Table represents an event that is sent at the beginning of each
session.
Each row in the Match Table represents an event that is sent at the end of the match
The number of active days is a number for the distinct days played per user
Create a SQL Query that gives you the number of player per that played at least 1
active day (100%), at least 2 active days etc.... and its proportion
 */

--At first, I approached task 1.5 using a fairly simple approach as:

SELECT
    COUNT(DISTINCT DATE(event_date)) AS ActiveDays,
    COUNT(DISTINCT user_id) AS "Number of players",
    CONCAT(ROUND(COUNT(DISTINCT user_id) * 100.0 / COUNT(DISTINCT user_id), 2), '%') AS "Part of players"
FROM Session
GROUP BY ActiveDays
ORDER BY ActiveDays ASC;

-- However, very quickly during the experiment I realized that my approach is not correct and it will not be so easy...

-- Well, I decided to analyze the task more deeply and think more thoroughly about ways to solve it
-- Here is the result:

SELECT
    ActiveDays,
    COUNT(DISTINCT user_id) AS "Number of players",
    CONCAT(ROUND(COUNT(DISTINCT user_id) * 100.0 / (SELECT COUNT(DISTINCT user_id) FROM Session), 2), '%') AS "Part of players"
FROM (
    SELECT
        COUNT(DISTINCT DATE(event_date)) AS ActiveDays,
        user_id
    FROM Session
    GROUP BY user_id
) AS ActiveDaysCount
GROUP BY ActiveDays
ORDER BY ActiveDays ASC;

/*
 This SQL query effective returns the following table:
 (Test data was taken from test dataset which you can chak at the following link,
https://github.com/Luxiv/Gameloft_Data_Scientist_Test/blob/master/Data_and_Python/task_1_5.py
 where you can also see my version of task 1.5 using the Pandas library)

 | Active days            | Number of players  | Part of players |
---------------------------------------------------------------------
 |             1          | 4                | 66.67%            |
---------------------------------------------------------------------
 |             2          | 2                | 33.33%            |
---------------------------------------------------------------------
 */