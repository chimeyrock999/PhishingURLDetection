#load data
import numpy as np
import pandas as pd
import sklearn
import pandas as pd
from feature_extractor import extract
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.model_selection import KFold
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import cross_validate
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn import svm , preprocessing
from sklearn.ensemble import AdaBoostClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.experimental import enable_hist_gradient_boosting
from sklearn.ensemble import HistGradientBoostingClassifier

#load benign dataset
benign_df=pd.read_csv("dataset_gender/benign_dataset.csv", header=0)
#print(benign_df)
#print(benign_df.describe())

#load phising dataset
phising_df=pd.read_csv("dataset_gender/phising_dataset.csv",header=0)
#print(phising_df)
#print(phising_df.describe())

#concat and 2 dataframe
frame=[benign_df, phising_df]
df=pd.concat(frame)
df=df.drop(['num_space_url','num_hashtag_url','num_underline_domain','num_bar_domain',
            'num_question_domain', 'num_equal_domain','num_asterisk_directory','num_atsign_domain',
            'num_ampersand_domain','num_exclamation_domain','num_space_domain','num_tilde_domain',
            'num_comma_domain','num_plus_domain','num_asterisk_domain','num_hashtag_domain',
            'num_dollar_domain','num_percent_domain','num_question_directory','num_space_directory','num_hashtag_directory',
            'num_bar_file','num_question_file','num_atsign_file','num_equal_file','num_ampersand_file','num_exclamation_file',
            'num_space_file','num_tilde_file','num_comma_file','num_asterisk_file','num_hashtag_file','num_dollar_file','num_space_params',
            'num_tilde_params','num_hashtag_params','url_index_on_google','domain_index_on_google'
            ],axis=1)
df = sklearn.utils.shuffle(df)
#print(df)

#Label Encoding
from sklearn.preprocessing import LabelEncoder
df = df.apply(LabelEncoder().fit_transform)
#print(df)
X = df.drop(['phising'],axis=1)
X = preprocessing.scale(X)
y=df['phising'].values
#print(X)
#print(y)

#train test split
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
#print(X_train)
#print(y_train)

scoring = {'accuracy': 'accuracy',
           'recall': 'recall',
           'precision': 'precision',
           'f1': 'f1'}
fold_count=10


def mean_score(scoring):
    return {i:j.mean() for i,j in scoring.items()}

dtree_clf=DecisionTreeClassifier()
cross_val_scores = cross_validate(dtree_clf, X, y, cv=fold_count, scoring=scoring)
dtree_score = mean_score(cross_val_scores)
print(['DecisionTreeClassifier:', dtree_score])


rforest_clf=RandomForestClassifier()
cross_val_scores = cross_validate(rforest_clf, X, y, cv=fold_count, scoring=scoring)
rforest_clf_score = mean_score(cross_val_scores)
print(['RandomForestClassifier:', rforest_clf_score])

adaboost_clf=AdaBoostClassifier()
cross_val_scores = cross_validate(adaboost_clf, X, y, cv=fold_count, scoring=scoring)
adaboost_clf_score = mean_score(cross_val_scores)
print(['AdaBoostClassifier:',adaboost_clf_score])

gradientBooster_clf=GradientBoostingClassifier()
cross_val_scores = cross_validate(gradientBooster_clf,X, y, cv=fold_count, scoring=scoring)
gradientBooster_clf_score= mean_score(cross_val_scores)
print(['GradientBoostingClassifier:',gradientBooster_clf_score])

histGradientBooster_clf = HistGradientBoostingClassifier()
cross_val_scores = cross_validate(histGradientBooster_clf,X, y, cv=fold_count, scoring=scoring)
histGradientBooster_clf_score= mean_score(cross_val_scores)
print('HistGradientBoostingClassifier:',histGradientBooster_clf_score)

KNeighbors_clf=KNeighborsClassifier(3)
cross_val_scores = cross_validate(KNeighbors_clf, X, y, cv=fold_count, scoring=scoring)
KNeighbors_clf_score = mean_score(cross_val_scores)
print(['KNeighborsClassifier(3):',KNeighbors_clf_score])

neural_clf=MLPClassifier(hidden_layer_sizes=(33,),max_iter=500)
cross_val_scores = cross_validate(neural_clf, X, y, cv=fold_count, scoring=scoring)
neural_clf_score = mean_score(cross_val_scores)
print(['MLPClassifier:', neural_clf_score])
