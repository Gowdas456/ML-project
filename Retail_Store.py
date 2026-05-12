import pandas as pd
import joblib
from sklearn.ensemble import RandomForestRegressor

def train():
    df = pd.read_csv('retail_locations.csv')
    X = df[['Population_Density', 'Average_Income', 'Competitor_Count', 'Foot_Traffic', 'Rent_Cost']]
    y = df['Success_Score']
    
    model = RandomForestRegressor(n_estimators=100)
    model.fit(X, y)
    joblib.dump(model, 'RandomForest_model.pkl')
    print("✅ RandomForest_model.pkl saved.")

if __name__ == "__main__":
    train()