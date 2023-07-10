WITH
    temp
    AS
    (
        SELECT city.id,
            COUNT(customer.id) AS num_customer
        FROM city
            JOIN country ON city.country_id = country.id
            JOIN customer ON city.id = customer.city_id
        GROUP BY city.id
    )

SELECT city.city_name, country.country_name, COUNT(customer.id) AS 
num_customer
FROM city
    JOIN country ON city.country_id = country.id
    JOIN customer ON city.id = customer.city_id
GROUP BY city.id
HAVING num_customer > (SELECT AVG(num_customer)
FROM temp)
ORDER BY country.country_name;

    select 'customer' as category, c.id as id, customer_name as name
    from customer c
        left join invoice i on c.id = i.customer_id
    where i.id is null

union

    select 'product' as category, p.id as id, product_name as name
    from product p
        left join invoice_item ii on p.id = ii.product_id
