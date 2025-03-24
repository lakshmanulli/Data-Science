import sys
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
sys.path.insert(0, 'src')
from preprocessing import load_data, preprocess_data
from predicting import train_model, evaluate_models, save_models
from config import file_path, target_column
from sklearn.model_selection import train_test_split
import logging

logging.basicConfig(filename='logs/project.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    df = load_data(file_path)
    df = preprocess_data(df)
    X = df.drop(target_column, axis=1)
    y = df[target_column]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    models = train_model(X_train, y_train)
    evaluate_models(models, X_test, y_test)
    save_models(models)

if __name__ == "__main__":
    main()