import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler

def load_data(file_path):
    try:
        df = pd.read_csv(file_path, sep=';')
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        raise

def preprocess_data(df):
    try:
        # Convert categorical columns into numerical form
        categorical_columns = ['job', 'marital', 'education', 'default', 'housing', 'loan', 'contact', 'month', 'poutcome']
        for col in categorical_columns:
            le = LabelEncoder()
            df[col] = le.fit_transform(df[col])
        
        # Map y (target) as {yes:1, no:0}
        df['y'] = df['y'].map({'yes': 1, 'no': 0})
        
        # Normalize numeric columns
        numeric_columns = ['age', 'balance', 'duration', 'campaign', 'pdays', 'previous', 'day']
        scaler = StandardScaler()
        df[numeric_columns] = scaler.fit_transform(df[numeric_columns])
        
        return df
    except Exception as e:
        print(f"Error in preprocessing: {e}")
        raise