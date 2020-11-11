import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score
from sklearn.feature_extraction.text import CountVectorizer

def model_training(df):
    
    X = df['text_processed']
    y = df['target']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=0)
    
    vec = CountVectorizer()
    X_train_transformed = vec.fit_transform(X_train)
    X_test_transformed = vec.transform(X_test)
    
    model = LinearSVC()
    model.fit(X_train_transformed, y_train)
    
    y_pred = model.predict(X_test_transformed)
    accuracy = accuracy_score(y_test, y_pred)
    
    return model, accuracy, vec