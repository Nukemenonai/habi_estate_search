GET_ESTATE = """
SELECT 
    address,
    city, 
    price, 
    description, year,
    property_id,
    status_id,
    update_date
FROM `habi_db`.`property` as p
INNER JOIN `habi_db`.`status_history` as s
ON p.id = s.property_id
WHERE status_id NOT IN (1, 2)
AND (property_id, status_id) in (
    SELECT property_id, MAX(status_id)
    FROM `habi_db`.`status_history`
    GROUP BY property_id
)
"""