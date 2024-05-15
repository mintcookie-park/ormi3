SELECT count(date_format(TIME, '%c')) as FISH_COUNT, cast(date_format(TIME, '%c') as unsigned) as MONTH
FROM FISH_INFO
group by 2
order by 2