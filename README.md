# surfs_up

## Purpose
The purpose of this repository is to examine the weather data for Oahu, Hawaii, to better determine the likelihood of success for a new Surf and Shake shop.  Requested was a comparison of temperatures over time for the months of June and December to determine sustainability over the whole year.

## Results

![June_Temps](https://user-images.githubusercontent.com/102555125/183269496-c421c673-9735-4021-a019-1b7b8d140c4a.png)   ![Dec_Temps](https://user-images.githubusercontent.com/102555125/183269500-2fc04ce1-79ce-4136-8bd9-43c6b00c56d3.png)

- Average temperatures between June and December remain consistent with June at 75 degrees and December at 71 degrees.  This small of an average temperature change is not likely to be the cause of decreased business due to season.

- Minimum temperatures vary more than the averages.  June's minimum of 64 degrees is not likely to cause too much of an issue, but December's minimum of 56 degrees will likely affect business on those days. Given the average mentioned above, December's minimum does not seem like it is the norm, more like the exception.

- The maximum temperatures between June and December are also consistent.  Given that they are 85 degrees and 83 degrees respectively, this would likely increase business on those days rather than affect it negatively, as warm days drive people to water sports and cold snacks.

## Summary
Oahu's consistent temperature year-round would not likely affect sustainability.  While the minimum temperatures would likely affect business on those particular days, they don't appear to be frequently occuring, thus would not be enough to be concerned over.  


### Additional Queries
Given investor concerns over excessive rainfall having a negative effect on previous surf business ventures, I chose to base my additional queries on precipitation for June and December.  Given the chance, I would also like to examine the rainfall data from the previous failed venture's location to compare the two, as this would give a much better indication of possible success for the new Surf and Shake shop.

#### June
```
# Write a query that filters the Measurement table to retrieve the precipitation for the month of June.  Convert to DataFrame. 
prcp6_date_str = "06"
june_prcp_results = []
june_prcp_results = session.query(Measurement.date, Measurement.prcp). \
    filter(func.strftime("%m", Measurement.date) == prcp6_date_str).all()
june_prcp = pd.DataFrame(june_prcp_results, columns=['date', 'June_Prcp'])
```

```
# Group by day of the month and average rainfall for each day.
june_prcp.set_index(june_prcp['date'], inplace=True)
prcp_by_date = june_prcp.groupby(pd.to_datetime(june_prcp.index).strftime('%b-%d'))['June_Prcp'].mean()
```

The first query pulls the date and precipitation from the data set and creates a DataFrame.  It then converts the date column to datetime format and sets it to the index.  It then groups the dates by day of the month and averages the rainfall for each of those days.  This gives a picture over time of what days during the month have seen more rain.  This is captured in the line graph below.  

![June_daily_rainfall](https://user-images.githubusercontent.com/102555125/183270115-3a5f9d7a-3a19-4365-b323-cc9be39c0788.png)


#### December
```
# Find December precipitation for each date and convert to a DataFrame
dec_date_str = "12"
dec_prcp_results = []
dec_prcp_results = session.query(Measurement.date, Measurement.prcp). \
    filter(func.strftime("%m", Measurement.date) == dec_date_str).all()
dec_prcp = pd.DataFrame(dec_prcp_results, columns=['date', 'Dec_Prcp'])
```

```
# Group and average precipiation by day of the month
dec_prcp.set_index(dec_prcp['date'], inplace=True)
prcp_by_date2 = dec_prcp.groupby(pd.to_datetime(dec_prcp.index).strftime('%b-%d'))['Dec_Prcp'].mean()
```

This code refactors June's code to make a consistent comparison between rainfall for both months.  The results of this are shown in the graph below.

![Dec_daily_rainfall](https://user-images.githubusercontent.com/102555125/183270233-75cefd53-d844-4b44-89ae-15fde7deab5a.png)

#### Additional Query Thoughts
While these graphs do not determine whether or not the business will fail due to rainfall, they do give warning on when to expect more rain.  With this data, the business can better prepare for those rainy times and innovate on how to increase business during wet weather.

