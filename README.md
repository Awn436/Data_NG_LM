# How to use

1. Use -git clone https://github.com/mams07/Data_NG_LM.git

2. Go in .../Data_NG_LM

3. Use python app.py

4. Go to localhost:80/ and use the app

# How to use it as a Docker Image

1. Use -docker build "name_of_img"

2. Use -docker run -p 80:80 "name_of_img"

3. Go to localhost:80/ and use the app

# How to compute tests

First, download the dataset from https://www.kaggle.com/kazanova/sentiment140
Place in the project folder (should be .../Data_NG_LM/training.1600000.processed.noemoticon.csv)

### 1. Unit tests
-python -m unittest

### 2. Integration test
-python integration_test.py
