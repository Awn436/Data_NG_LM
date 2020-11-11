import unittest
import pandas as pd
from data_preprocess import data_preprocessing

class TestProcessing(unittest.TestCase):

    def test_type(self):
        a = data_preprocessing(pd.DataFrame(data = [[0,"","","","",""]], columns = ['target', 'ids', 'date', 'flag', 'user', 'text']))
        self.assertEqual(type(a['text_processed'][0]),type(''))

    #Testing if usernames are deleted
    def test_format1(self):
        a = data_preprocessing(pd.DataFrame(data = [[0,"","","","","@test"]], columns = ['target', 'ids', 'date', 'flag', 'user', 'text']))
        self.assertEqual(a['text_processed'][0], '')

    #Testing if URLs are deleted
    def test_format2(self):
        a = data_preprocessing(pd.DataFrame(data = [[0,"","","","","https://www.youtube.com"]], columns = ['target', 'ids', 'date', 'flag', 'user', 'text']))
        self.assertEqual(a['text_processed'][0], '')
    
    #Testing if non-alphanumeric characters are deleted
    def test_format3(self):
        a = data_preprocessing(pd.DataFrame(data = [[0,"","","","","| / {*"]], columns = ['target', 'ids', 'date', 'flag', 'user', 'text']))
        self.assertEqual(a['text_processed'][0], '')
    
    #Testing if the text is correctly lowercased
    def test_format4(self):
        a = data_preprocessing(pd.DataFrame(data = [[0,"","","","","ABC DEFG"]], columns = ['target', 'ids', 'date', 'flag', 'user', 'text']))
        self.assertEqual(a['text_processed'][0], 'abc defg')
    
    #Testing if single letters are deleted
    def test_format5(self):
        a = data_preprocessing(pd.DataFrame(data = [[0,"","","","","a b c"]], columns = ['target', 'ids', 'date', 'flag', 'user', 'text']))
        self.assertEqual(a['text_processed'][0], '')

