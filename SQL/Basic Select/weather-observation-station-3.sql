/*
Problem Link: https://www.hackerrank.com/challenges/weather-observation-station-3/problem

Query a list of CITY names from STATION with even ID numbers only. You may print the results in any order, 
but must exclude duplicates from your answer.
*/
select distinct CITY from STATION where ID % 2 = 0;