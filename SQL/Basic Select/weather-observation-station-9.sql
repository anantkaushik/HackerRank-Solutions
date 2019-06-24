/*
Problem Link: https://www.hackerrank.com/challenges/weather-observation-station-9/problem

Query the list of CITY names from STATION that do not start with vowels. Your result cannot contain duplicates.
*/
select distinct CITY from STATION where left(CITY,1) not in ('a','e','i','o','u');