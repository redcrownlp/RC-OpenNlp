# Arabic NLP Project

## About Project:
Arabic NLP Project distinct between five Arabic language dialects which are: Gulf, Iraqi, Levant, Egyptian and Maghreb dialects. In general, the project divided into Five stages which are data collection, data preprocessing, data labeling, feature extraction, and classification.

1. **Data Collection Stage**: <br/><br/>We collected around 200 thousands tweets that contain records for all dialects (around 50 thousands for each dialect).

2. **Data Preprocessing Stage**: <br/>We applied preprocessing stage on our dataset, to prepare it for labeling stage. The preprocessing stage includes removing non-Arabic characters and removing redundancy in the dataset. 
<br/>To remove redundancy we apply to find similarity algorithm which finds the similarity between the tweets and remove the tweets with similarity larger than 80%. 
<br/>After the preprocessing stage, The dataset is reduced to around 100 thousand, and this dataset is ready for labeling stage.

3. **Labeling Data Stage**.

4. **Feature Extraction Stage**:<br/>
   In order to build models using machine learning algorithms, we need to extract represented features from our datasets. based on top researchers in NLP area, the common methods used are: 
   Character n-grams:1-8 grams and word n-gram:1:5. We used the following features in our system:
     - Word n-grams:
                  1-grams, 2-grams and 3-grams.
     - Character n-grams:
                  6-grams, 7-grams and 8-grams. 
<br/> We extract around 28k features.
5. **Classification Stage**: <br/>We divide the dataset to training dataset and testing dataset. 60% for training and 40% for testing.
   - Training the model:
     We training our model using Logistic Regression classifier.
   - Testing the model:
     We testing the model and got **accuracy of 98%** for training dataset.
     
## Project Requirements: 

Install the following packages in your Linux operating system:
- python2.7

Install **python-pip** and use it to download the following packages:
- xlrd
- xlwt
- regex
- openpyxl
- nltk
- sklearn


## How to run the NLP project?
The project contains the follwoing four folders:

1. Preprocessing Stage Folder:
You can apply preprocessing stage in your dataset as following:
- Go to "Preprocessing Stage" Folder.
- Save your dataset that contains Arabic text in "Dataset_before_Preprocessing.xls" file.
- Run the main.py file using the following commands: 
> python2.7 main.py
- The cleaned dataset will store in "Dataset_after_Preprocessing.xlsx" file.

2. Features Extraction Stage Folder:
Extract features from your dataset as following:
- Go to "Features Extraction Stage" Folder.
- Run the main.py file using the following commands: 
> python2.7 main.py
- The Features will store in "Features.xlsx" file.

3. Classification Stage Folder:
<br/>Training your model and testing it as following:
<br/>Training your model: 
<br/>- Go to "Classification Stage" Folder.
<br/>- Run the Training_LogisticRegression_Classifier.py file using the following commands: 
> python2.7 Training_LogisticRegression_Classifier.py
- The training model will store in "OurModel.pkl" file.
<br/>Testing Model:
- Go to "Classification Stage" Folder.
- Run the Testing_LogisticRegression_Classifier.py file using the following commands: 
> python2.7 Testing_LogisticRegression_Classifier.py
- The Accuracy Result will print in the screen.
4. Examples Folder:<br/>
This folder contains NLP training model which is ready to used. The model take the features vector and the testing dataset as input. 
