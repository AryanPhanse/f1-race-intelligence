import fastf1
import os

# 1. Create a local cache directory to store data 
cache_dir = 'f1_cache'
if not os.path.exists(cache_dir):
    os.makedirs(cache_dir)

# 2. Enable FastF1 caching (prevents API rate limits and speeds up scripts)
fastf1.Cache.enable_cache(cache_dir)

# 3. Download the 2024 Monaco Grand Prix Race telemetry
print("Downloading Monaco 2024 race data... this may take a minute...")
session = fastf1.get_session(2024, 'Monaco', 'R')
session.load()

# 4. Print the top results
print("\n--- RACE RESULTS ---")
print(session.results[['DriverNumber', 'Abbreviation', 'ClassifiedPosition', 'Time']])