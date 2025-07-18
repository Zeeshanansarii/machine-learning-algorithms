'''
# Steps for EDA and Data Leakage

EDA steps::

step 1: Import neccessory data libraries

step 2: Import dataset using Pandas function

step 3: Checking dataset information -->
        df.info()

step 4: Checking null values present in dataset --> 
        df.isnull().sum().plot(kind = 'bar)

step 5: Segregate categorical and numerical columns -->
        categorical_col = df.select_dtypes(include = 'object')
        numerical_col = df.select_dtypes(exclude = 'object')


step 6: Use SimpleImputer technique or use fillna function to impute values in dataset.
        Note: 
            a. If the dataset is skew: use median as imputation strategy (skew is non normal distributed)
            b. If the dataset is non-skew: Use mean as imputation strategy
            c. If categorical column: Mode technique

steps *: use EDA part: a. Univariate analysis b. Bi variate analysis

step 7: Use Imbalance technique: for the classification problem
        1. Over sampling : SMOTE, SMOTEN, SMOTENC
        2. Under sampling : ClusterCentroid, AllKNN

        ** It is used only for classification problem (for categorical) not for regression problem(for numerical)

step 8: Split the dataset into X and y

step 9: Split dataset into X_train, X_test, y_train, y_test
        Use Encoding techniques (label encoder) into numerical

step 10: Use Scaling technique
        a. MinMaxScaler
           - Use when data is not normally distributed and you want features in a fixed range (0 to 1). Popular for algorithms sensitive to feature scale (e.g., KNN, neural networks).
        b. StandardScaler
           - Use when data is normally distributed. Scales features to have mean=0 and variance=1. Suitable for linear models, logistic regression, SVM, PCA.
        c. RobustScaler
           - Use when data contains outliers. Scales features using statistics that are robust to outliers (median and IQR). Useful for models sensitive to outliers or when data is non-normal and has extreme values.

step 11: Machine learning model building

step 12: Use pickle file and ready for deployment

'''

''' 
Data Leakage::

Step 1. Split dataset into X and y
        X : Independent columns
        y : Dependent columns / Target columns

Step 2. Split dataset into train and test
        X_train : Seen data : 70%
        X_test : Unseen data : 30%

        y_train : Seen data : 70%
        y_test : unseen data : 30%

Step 3. If you solving classification model / Recommendation model then use Imbalance techniques, Always work on training data only.
        A. Over Sampling: 1. Smote, 2. Smoten, 3. Smotenc

        B. Under sampling: 1. ClusterCentroid, 2. AllKnn

Step 4. Use proper scaling techniques on dataset

        1. MinMax Scaler = Always take range b/w 0 to 1. MinMax scaler is so popular when data the is non normal distributed.
        2. Standard Scaler = When a dataset is normally distributed.
        3. Robust Scaler = When dataset is non normal distributed and model is sensitive to outliers i.e. when model overfit.

Step 5. Model building

'''