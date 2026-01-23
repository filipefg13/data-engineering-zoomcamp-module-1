import pandas as pd
# Lê o dataset de viagens
trips = pd.read_parquet("green_tripdata_2025-11.parquet")

# Lê o dataset de zonas
zones = pd.read_csv("taxi_zone_lookup.csv")

# Converte a coluna de datetime
trips['lpep_pickup_datetime'] = pd.to_datetime(trips['lpep_pickup_datetime'])

# Filtra apenas o dia 18 de Novembro de 2025
trips_nov18 = trips[trips['lpep_pickup_datetime'].dt.date == pd.to_datetime('2025-11-18').date()]

# Agrupa por PULocationID e soma o total_amount
pickup_sums = trips_nov18.groupby('PULocationID')['total_amount'].sum()

# Encontra o PULocationID com maior total_amount
max_pickup_id = pickup_sums.idxmax()

# Recupera o nome da zona (Zone) correspondente
pickup_zone_name = zones.loc[zones['LocationID'] == max_pickup_id, 'Zone'].values[0]

# Imprime o resultado
print("Pickup Zone with largest total_amount on 18/11/2025:", pickup_zone_name)

# Question 6:
import pandas as pd
trips = pd.read_parquet("green_tripdata_2025-11.parquet")
zones = pd.read_csv("taxi_zone_lookup.csv")
trips['lpep_pickup_datetime'] = pd.to_datetime(trips['lpep_pickup_datetime'])
trips_nov = trips[(trips['lpep_pickup_datetime'].dt.month == 11) &
                  (trips['lpep_pickup_datetime'].dt.year == 2025)]
trips_nov = trips_nov.merge(zones[['LocationID', 'Zone']], left_on='PULocationID', right_on='LocationID', how='left')
trips_ehn = trips_nov[trips_nov['Zone'] == "East Harlem North"]
trips_ehn = trips_ehn.merge(zones[['LocationID', 'Zone']], left_on='DOLocationID', right_on='LocationID', how='left', suffixes=('_pickup', '_dropoff'))
max_tip_row = trips_ehn.loc[trips_ehn['tip_amount'].idxmax()]
print("Dropoff zone with largest tip:", max_tip_row['Zone_dropoff'])