import numpy as np
import pandas as pd
import pandas as pd
from .feature_extractor import extract
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import preprocessing

def predict_new_url(url):
    #load benign dataset
    benign_df=pd.read_csv("app/dataset_gender/benign_dataset.csv", header=0)
    #print(benign_df)
    #print(benign_df.describe())

    #load phising dataset
    phising_df=pd.read_csv("app/dataset_gender/phising_dataset.csv",header=0)
    #print(phising_df)
    #print(phising_df.describe())

    extract.extract_new_url(url,'app/dataset_gender/predict.csv')

    predict=pd.read_csv('app/dataset_gender/predict.csv', header=0)

    #concat and 2 dataframe
    frame=[benign_df, phising_df]
    train_df=pd.concat(frame)
    #train_df= sklearn.utils.shuffle(train_df)
    full_frame=[train_df, predict]
    df=pd.concat(full_frame)
    df=df.drop(['num_space_url','num_hashtag_url','num_underline_domain','num_bar_domain',
                'num_question_domain', 'num_equal_domain','num_asterisk_directory','num_atsign_domain',
                'num_ampersand_domain','num_exclamation_domain','num_space_domain','num_tilde_domain',
                'num_comma_domain','num_plus_domain','num_asterisk_domain','num_hashtag_domain',
                'num_dollar_domain','num_percent_domain','num_question_directory','num_space_directory','num_hashtag_directory',
                'num_bar_file','num_question_file','num_atsign_file','num_equal_file','num_ampersand_file','num_exclamation_file',
                'num_space_file','num_tilde_file','num_comma_file','num_asterisk_file','num_hashtag_file','num_dollar_file','num_space_params',
                'num_tilde_params','num_hashtag_params','url_index_on_google','domain_index_on_google'
                ],axis=1)
    #print(df)

    #Label Encoding
    from sklearn.preprocessing import LabelEncoder
    try:
        df = df.apply(LabelEncoder().fit_transform)
    except(Exception):
        return -1
    #print(df)
    #detach predict
    X_predict = df[df['phising']==2]
    X_predict = X_predict.drop(['phising'],axis=1)
    print(X_predict)
    df=df.drop(df[df['phising']==2].index)
    #print(df)
    #X = preprocessing.scale(X)
    X = df.drop(['phising'],axis=1)
    y=df['phising'].values
    #print(X)
    #print(y)

    #train test split
    from sklearn.model_selection import train_test_split

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
    #print(X_train)
    #print(y_train)

    clf = RandomForestClassifier(n_estimators = 100)  

    # Training the model on the training dataset
    # fit function is used to train the model using the training sets as parameters
    clf.fit(X_train, y_train)

    # performing predictions on the test dataset
    y_pred = clf.predict(X_test)

    # metrics are used to find accuracy or error
    from sklearn import metrics  
    print()

    # using metrics module for accuracy calculation
    # print("ACCURACY OF THE MODEL: ", metrics.accuracy_score(y_test, y_pred))
    result=clf.predict(X_predict)
    print(result)
    return result