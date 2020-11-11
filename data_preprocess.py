import string
import pandas as pd

def data_preprocessing(df):
    
    df = df.drop(['ids', 'date', 'flag', 'user'], axis = 'columns')

    df['text_processed'] = df['text'].str.replace(r'@\S+', '')
    df['text_processed'] = df['text_processed'].str.replace(r'http\S+','')
    df['text_processed'] = df['text_processed'].str.replace('[^a-zA-Z]',' ')
    df['text_processed'] = df['text_processed'].str.lower()
    df['text_processed'] = df['text_processed'].apply(lambda x: ' '.join([w for w in x.split() if len(w)>1]))
    
    return df