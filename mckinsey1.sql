WITH temp AS (SELECT city.id, 
COUNT(customer.id) AS num_customer
FROM city
JOIN country ON city.country_id = country.id
JOIN customer ON city.id = customer.city_id
GROUP BY city.id)

SELECT city.city_name, country.country_name, COUNT(customer.id) AS 
num_customer
FROM city
JOIN country ON city.country_id = country.id
JOIN customer ON city.id = customer.city_id
GROUP BY city.id
HAVING num_customer > (SELECT AVG(num_customer) FROM temp)
ORDER BY country.country_name;