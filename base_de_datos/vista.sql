-- CREANDO UNA VISTA CON SQL
-- Flores Ledezma Fabricio Lennart

-- Para este proyecto necesitamos crear una vista especial que incluya todas las
-- transformaciones necesarias para visualizar los datos de mejor manera.

-- La columna iso_codes se ve así 
SELECT iso_codes FROM countries;

-- La columna gdp_$usd se ve así

SELECT gdp_$usd FROM countries;

-- Creando una vista con los cambios realizados
CREATE VIEW country_data AS 
SELECT country,
       country_code,
       substr(gdp_$usd, 1, 6) AS gdp,
       population,
       area_km2,
       substr(iso_codes, length(iso_codes) - 3) AS iso_codes 
FROM countries;

-- Verificando si la vista se creó con éxito
SELECT * FROM country_data;