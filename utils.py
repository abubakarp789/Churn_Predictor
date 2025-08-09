import pandas as pd

def preprocess_input(data):
    """
    Preprocesses the input data from the form.
    """
    # Convert to DataFrame
    df = pd.DataFrame([data])

    # Convert data types
    df['age'] = pd.to_numeric(df['age'])
    df['days_since_last_login'] = pd.to_numeric(df['days_since_last_login'])
    df['avg_time_spent'] = pd.to_numeric(df['avg_time_spent'])
    df['avg_transaction_value'] = pd.to_numeric(df['avg_transaction_value'])
    df['points_in_wallet'] = pd.to_numeric(df['points_in_wallet'])

    # Feature Engineering for dates and times
    df['joining_day'] = pd.to_datetime(df['joining_date']).dt.day
    df['joining_month'] = pd.to_datetime(df['joining_date']).dt.month
    df['joining_year'] = pd.to_datetime(df['joining_date']).dt.year
    df['last_visit_time_hour'] = pd.to_datetime(df['last_visit_time']).dt.hour
    df['last_visit_time_minutes'] = pd.to_datetime(df['last_visit_time']).dt.minute
    df['last_visit_time_seconds'] = pd.to_datetime(df['last_visit_time']).dt.second

    # Drop original date/time columns
    df = df.drop(['joining_date', 'last_visit_time'], axis=1)

    # One-hot encode categorical features
    categorical_cols = [
        'gender', 'region_category', 'membership_category',
        'joined_through_referral', 'preferred_offer_types',
        'medium_of_operation', 'internet_option', 'used_special_discount',
        'offer_application_preference', 'past_complaint', 'feedback'
    ]
    df = pd.get_dummies(df, columns=categorical_cols, drop_first=False)

    return df
