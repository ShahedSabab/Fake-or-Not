# Fake-or-Not
The dataset includes tweets about disaster e.g., earthquake, wildfire. The objective is to detect real news vs fake news. For training the model, pretrained BERT is used. 84.5% accuracy has been achieved while testing with holdout data.

• Tensorflow 2.0 is used.<br/>
• The model is trained in google colab.<br/>
• BERT-base is used for training.<br/>
• Dropout layer and L1 regularization have been applied to reduce overfitting.<br/>
• 84.5% accuracy is achieved.<br/>

# Preprocessing

The orginal data can be found in train.csv from which only texts have been extracted (in data_train.csv) using preprocess.py script.

# How to run

Please check fakeorNotfake_bert.ipynb script.

