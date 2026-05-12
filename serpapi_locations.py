from serpapi import GoogleSearch
import pandas as pd

def fetch_locations():
    # PASTE YOUR API KEY HERE
    API_KEY = "6c0e137398f6e33809f8cf53ef38e07b0f4bd50a47bfe9963df4e8876e070760" 

    params = {
        "engine": "google_maps",
        "q": "supermarkets",
        "ll": "@40.7128,-74.0060,14z", # Searches near New York City
        "api_key": API_KEY
    }

    search = GoogleSearch(params)
    results = search.get_dict()
    
    # Extract real locations from the API results
    stores = []
    for place in results.get("local_results", []):
        stores.append({
            "Name": place.get("title"),
            "Latitude": place.get("gps_coordinates", {}).get("latitude"),
            "Longitude": place.get("gps_coordinates", {}).get("longitude"),
            "Rating": place.get("rating", 0)
        })
    
    df = pd.DataFrame(stores)
    df.to_csv('newzz_serpapi.csv', index=False)
    print("✅ newzz_serpapi.csv created with REAL API data.")

if __name__ == "__main__":
    fetch_locations()