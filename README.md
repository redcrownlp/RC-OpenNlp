# Arabic NLP Project
     
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
- pyarabic

## How to Clone the Project?

This repositery used Git Large File Storage (git-lfs). Therefore, you need to [install Git-lfs](https://github.com/git-lfs/git-lfs/wiki/Installation) to be able to used the ready models in this project.


## How to run the NLP project?
The project contains the follwoing four folders:

1. Preprocessing Stage Folder:
You can apply preprocessing stage in your dataset as following:
- Go to "Preprocessing Stage" Folder.
- Save your dataset that contains Arabic text in "Dataset_before_Preprocessing.xls" file.
- Run the main.py file using the following command: 
> python2.7 main.py
- The cleaned dataset will store in "Dataset_after_Preprocessing.xlsx" file.

2. Features Extraction Stage Folder:
Extract features from your dataset as following:
- Go to "Features Extraction Stage" Folder.
- Run the main.py file using the following command: 
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
This folder contains NLP training models which are ready to used. The models take the features vector and the testing dataset as input and return back the dialects probability results to the user.
</br>The folder contains two subfolders that represent two machine learning classifiers:
- Logistic Regression classifier: 
</br>To run the Logistic Regression Classifier, go to "Examples/Logistic Regression Classifier" folder and run the "main.py" file using the following command: 
> python2.7 main.py
- MLP classifier: 
</br>To run the MLP Classifier, go to "Examples/MLPClassifier" folder and run the "main.py" file using the following command: 
> python2.7 main.py