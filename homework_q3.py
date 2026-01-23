import pandas as pd
trips = pd.read_parquet("green_tripdata_2025-11.parquet")
trips['lpep_pickup_datetime'] = pd.to_datetime(trips['lpep_pickup_datetime'])
trips_nov = trips[(trips['lpep_pickup_datetime'] >= '2025-11-01') &
                  (trips['lpep_pickup_datetime'] < '2025-12-01')]
short_trips = trips_nov[trips_nov['trip_distance'] <= 1]
num_short_trips = len(short_trips)
print("Number of trips with trip_distance <= 1 mile in Nov 2025:", num_short_trips)