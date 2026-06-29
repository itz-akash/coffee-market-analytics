SELECT
    Country_Name,
    ISO3_CODE,
    Market_Year,
    Attribute_Description,
    SUM(Value) AS Total_Value,
    MAX(Population) AS Population
FROM coffee_market
GROUP BY
    Country_Name,
    ISO3_CODE,
    Market_Year,
    Attribute_Description
ORDER BY
    Country_Name,
    Market_Year;