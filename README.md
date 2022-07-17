# earthquake_ML
Data science/ML project analysing earthquakes from the last 4000 years. The aim is to predict the number of deaths caused by an earthquake.
 
Data is from the National Centers for Environmental Information (NCEI) which stores historical earthquake data (from 2000BC to present) available for public use. It can be extracted using their API.

Project outline and summary:
- Extraction of data using NCEI API.
- Exploratory data analysis (understanding the features and their properties, dealing with missing data...).
- Feature engineering (using an independent population density dataset from another source to add features to the earthquake dataset).
- PCA.
- Regression to predict the number of deaths (linear, random forest, knn with hyperparameter optimisation).
- Classification to classify the earthquakes into binned numbers of deaths (logistic regression, random forest as well as hyperparameter optimisation and SMOTE).
- Concluding remarks and possible improvements that could be made.
