SELECT
    "Country_Name",
    SUM("Value") AS total_consumption,
    MAX("Population") AS population
FROM coffee_market
WHERE "Attribute_Description" = 'Domestic Consumption'
AND "Country_Name" <> 'European Union'
GROUP BY "Country_Name"
HAVING MAX("Population") IS NOT NULL
ORDER BY total_consumption DESC
LIMIT 10;