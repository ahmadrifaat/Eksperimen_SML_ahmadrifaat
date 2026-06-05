import os
import pandas as pd
import numpy as np

def generate_mock_data(num_samples=100):
    np.random.seed(42)
    data = {
        'customer_id': range(1001, 1001 + num_samples),
        'age': np.random.randint(20, 65, size=num_samples),
        'income': np.random.randint(3000000, 30000000, size=num_samples),
        'loan_amount': np.random.randint(5000000, 50000000, size=num_samples),
        'credit_score': np.random.randint(300, 850, size=num_samples),
        'employment_type': np.random.choice(['Full-Time', 'Part-Time', 'Self-Employed', 'Unemployed'], size=num_samples),
        'risk_rating': np.random.choice([0, 1], size=num_samples, p=[0.7, 0.3])
    }
    
    df = pd.DataFrame(data)
    
    # Menambahkan missing value & duplikat untuk simulasi
    df.loc[df.sample(frac=0.05).index, 'income'] = np.nan
    df.loc[df.sample(frac=0.03).index, 'credit_score'] = np.nan
    
    duplicate_rows = df.sample(n=5, random_state=42)
    df = pd.concat([df, duplicate_rows], ignore_index=True)
    
    os.makedirs('namadataset_raw', exist_ok=True)
    raw_data_path = os.path.join('namadataset_raw', 'credit_data.csv')
    df.to_csv(raw_data_path, index=False)
    print(f"Sukses menggenerasi data mentah di: {raw_data_path}")

if __name__ == "__main__":
    generate_mock_data()