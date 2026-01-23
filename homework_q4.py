import pandas as pd
trips = pd.read_parquet("green_tripdata_2025-11.parquet")
trips['lpep_pickup_datetime'] = pd.to_datetime(trips['lpep_pickup_datetime'])
trips_filtered = trips[trips['trip_distance'] < 100]
max_trip_row = trips_filtered.loc[trips_filtered['trip_distance'].idxmax()]
pickup_day = max_trip_row['lpep_pickup_datetime'].date()
print("Pick up day with the longest trip distance:", pickup_day)