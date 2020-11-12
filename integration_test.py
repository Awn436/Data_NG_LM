import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score
from sklearn.feature_extraction.text import CountVectorizer
from training_model import model_training
from data_preprocess import data_preprocessing

def good_bad(x):
    if x==4:
        print("Positive")
    if x==0:
        print("Negative")
    return 0

if __name__ == "__main__":

    df = pd.read_csv('training.1600000.processed.noemoticon.csv', encoding="ISO-8859-1", names=["target", "ids", "date", "flag", "user", "text"])
    df = data_preprocessing(df)
    model, acc, vec = model_training(df)
    a = model.predict(vec.transform(pd.Series('I am good')))
    b = model.predict(vec.transform(pd.Series('I am bad')))
    good_bad(a)
    good_bad(b)