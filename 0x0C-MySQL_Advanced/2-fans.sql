-- SQL script that ranks country origins of bands ordered by # of fans
-- column names: origin and nb_fans
SELECT origin, SUM(fans) AS nb_fans FROM metal_bands GROUP BY origin
ORDER BY nb_fans DESC;
