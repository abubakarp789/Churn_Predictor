# save this as app.py
from flask import Flask, request, render_template, url_for, jsonify
from datetime import datetime
import numpy as np
import pandas as pd
import pickle
import os
from utils import preprocess_input

app = Flask(__name__, static_url_path='/static')

@app.context_processor
def inject_now():
    return {'now': datetime.utcnow()}

# Load the model
model = pickle.load(open('random_forest_model.pkl', 'rb'))

# Load the dataset
df = pd.read_csv('dataset/train.csv')

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/analysis')
def analysis():
    # Categorical features distribution
    cat_features = ['gender', 'region_category', 'membership_category', 'preferred_offer_types']
    cat_data = {}
    for feature in cat_features:
        cat_data[feature] = df[feature].value_counts().to_dict()

    # Churn risk score distribution
    churn_data = df['churn_risk_score'].value_counts().to_dict()

    # Feature importances
    feature_importances = dict(zip(model.feature_names_in_, model.feature_importances_))

    return render_template("analysis.html", 
                           cat_data=cat_data, 
                           churn_data=churn_data, 
                           feature_importances=feature_importances)

@app.route('/prediction', methods=['GET', 'POST'])
def prediction():
    if request.method == "POST":
        try:
            # Get form data
            form_data = {
                'age': request.form['age'],
                'days_since_last_login': request.form['last_login'],
                'avg_time_spent': request.form['avg_time_spent'],
                'avg_transaction_value': request.form['avg_transaction_value'],
                'points_in_wallet': request.form['points_in_wallet'],
                'joining_date': request.form['date'],
                'last_visit_time': request.form['time'],
                'gender': request.form['gender'],
                'region_category': request.form['region_category'],
                'membership_category': request.form['membership_category'],
                'joined_through_referral': request.form['joined_through_referral'],
                'preferred_offer_types': request.form['preferred_offer_types'],
                'medium_of_operation': request.form['medium_of_operation'],
                'internet_option': request.form['internet_option'],
                'used_special_discount': request.form['used_special_discount'],
                'offer_application_preference': request.form['offer_application_preference'],
                'past_complaint': request.form['past_complaint'],
                'feedback': request.form['feedback']
            }

            # Preprocess the input
            processed_df = preprocess_input(form_data)

            # Align columns with the model's training columns
            model_cols = model.feature_names_in_
            processed_df = processed_df.reindex(columns=model_cols, fill_value=0)

            # Make prediction
            prediction = model.predict(processed_df)

            return render_template("prediction.html", prediction_text=f"Churn Score is {prediction[0]}")
        except Exception as e:
            return render_template("prediction.html", prediction_text=f"Error: {e}")
    else:
        return render_template("prediction.html")

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
