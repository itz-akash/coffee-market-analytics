SELECT
    "Market_Year",
    SUM("Value") AS total_consumption
FROM coffee_market
WHERE "Attribute_Description" = 'Domestic Consumption'
GROUP BY "Market_Year"
ORDER BY "Market_Year";