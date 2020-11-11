import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score
from sklearn.feature_extraction.text import CountVectorizer
from training_model import model_training
from data_preprocess import data_preprocessing

df = pd.read_csv('training.1600000.processed.noemoticon.csv', encoding="ISO-8859-1", names=["target", "ids", "date", "flag", "user", "text"])
data_preprocessing(df)
model_training(df)
a = model.predict(vec.transform(pd.Series('I am good')))
b = model.predict(vec.transform(pd.Series('I am bad')))

def good_bad(x):
    if x==4:
        print("this is good")
    if x==0:
        print("this is bad")
    return 0

good_bad(a)
good_bad(b)