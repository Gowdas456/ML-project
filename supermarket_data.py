import pandas as pd
import numpy as np

def generate_data():
    np.random.seed(42)
    data = {
        'Population_Density': np.random.randint(500, 10000, 500),
        'Average_Income': np.random.randint(20000, 120000, 500),
        'Competitor_Count': np.random.randint(0, 10, 500),
        'Foot_Traffic': np.random.randint(100, 5000, 500),
        'Rent_Cost': np.random.randint(1000, 15000, 500)
    }
    df = pd.DataFrame(data)
    # Success formula for the model to learn
    df['Success_Score'] = (df['Average_Income']*0.005 + df['Foot_Traffic']*0.01) - (df['Competitor_Count']*10 + df['Rent_Cost']*0.02)
    df.to_csv('retail_locations.csv', index=False)
    print("✅ retail_locations.csv created.")

if __name__ == "__main__":
    generate_data()