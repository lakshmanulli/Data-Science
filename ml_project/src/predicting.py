import logging
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, AdaBoostClassifier
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score

def train_model(X_train, y_train):
    try:
        logging.info("Training models...")
        models = {
            "RandomForest": RandomForestClassifier(n_estimators=100, random_state=42),
            "GradientBoosting": GradientBoostingClassifier(n_estimators=100, random_state=42),
            "AdaBoost": AdaBoostClassifier(n_estimators=100, random_state=42),
            "XGBoost": XGBClassifier(use_label_encoder=False, eval_metric='logloss')
        }
        trained_models = {}
        for name, model in models.items():
            model.fit(X_train, y_train)
            trained_models[name] = model
            logging.info(f"{name} model trained successfully.")
        return trained_models
    except Exception as e:
        logging.error(f"Error training models: {e}")
        raise

def evaluate_models(models, X_test, y_test):
    try:
        logging.info("Evaluating models...")
        for name, model in models.items():
            y_pred = model.predict(X_test)
            acc = accuracy_score(y_test, y_pred)
            logging.info(f"{name} Accuracy: {acc:.2f}")
    except Exception as e:
        logging.error(f"Error evaluating models: {e}")
        raise

def save_models(models):
    try:
        logging.info("Saving models...")
        import pickle
        for name, model in models.items():
            with open(f"models/{name}.pkl", "wb") as f:
                pickle.dump(model, f)
        logging.info("Models saved successfully.")
    except Exception as e:
        logging.error(f"Error saving models: {e}")
        raise