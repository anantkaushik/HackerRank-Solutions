/*
Problem Link: https://www.hackerrank.com/challenges/weather-observation-station-6/problem

Query the list of CITY names starting with vowels (i.e., a, e, i, o, or u) from STATION. Your result cannot contain duplicates.
*/
select DISTINCT CITY from STATION WHERE CITY REGEXP "^[aeiou].*";