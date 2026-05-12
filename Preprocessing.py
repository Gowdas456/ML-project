import pandas as pd

def merge_data():
    df1 = pd.read_csv('retail_locations.csv')
    df2 = pd.read_csv('newzz_serpapi.csv')
    
    # Merging logic (Example: combining simulated stats with real locations)
    merged = pd.concat([df1.head(len(df2)), df2], axis=1)
    merged.to_csv('merged_dataset.csv', index=False)
    print("✅ Created merged_dataset.csv")

if __name__ == "__main__":
    merge_data()