"""estate queries"""

GET_ESTATE = """
SELECT 
    address,
    city, 
    price, 
    CASE description
        WHEN '' THEN 'sin descripción'
        ELSE description
    END AS descripcion,
    CASE status_id
        WHEN 3 THEN 'pre_venta'
        WHEN 4 THEN 'en_venta'
        WHEN 5 THEN 'vendido'
    END AS estado
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