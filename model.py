from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

def preprocessing_rf(df):
    drop_cols = ['Unnamed: 0', 'Order ID', 'Order Date', 'Bulan', 'Last Visit Date', 'Customer ID', 'Monthly Spending (IDR)', 'Monthly Visit Count']
    df.drop(columns=[col for col in drop_cols if col in df.columns], inplace=True)
    
    encoders = {}
    if 'Churn' in df.columns:
        le = LabelEncoder()
        df['Churn'] = le.fit_transform(df['Churn'])

    for col in ['Category', 'Payment Method', 'Item']:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])
    
    return df

def split_data(df):
    # Pisahkan fitur dan target
    X = df.drop(columns='Churn')
    y = df['Churn'].astype(int)

    # Bagi data menjadi data train dan test
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    return X_train, X_test, y_train, y_test

def rf_model(X_train, X_test, y_train):
    from sklearn.model_selection import GridSearchCV
    rf = RandomForestClassifier(random_state=42, class_weight='balanced')

    param_grid = {
        'n_estimators': [100, 200, 300],
        'max_depth': [None, 10, 20, 30],
        'min_samples_split': [2, 5, 10],
        'min_samples_leaf': [1, 2, 4]
    }

    grid_search = GridSearchCV(
        estimator=rf,
        param_grid=param_grid,
        cv=5,  # 5-fold cross validation
        n_jobs=-1,
        verbose=1,
        scoring='f1_weighted'
    )

    # Jalankan grid search
    grid_search.fit(X_train, y_train)

    # Evaluasi model terbaik di test set
    best_model = grid_search.best_estimator_
    y_pred = best_model.predict(X_test)

    return best_model
