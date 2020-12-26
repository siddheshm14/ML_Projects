import pandas as pd
from sklearn.model_selection import train_test_split
import catboost
from catboost import CatBoostClassifier


def classification():

    data=pd.read_csv('D:\\Semester_3\\Marketing_Analytics\\Final_exam\\Final_PROJECT_group_7\\Churn_Modelling.csv')

    y=data[data.columns[-1]]
    X=data.drop(data.columns[-1],axis=1)
    X=X.drop(X.columns[:3],axis=1)
    X_train,X_test,y_train,y_test=train_test_split(X,y,random_state=50,stratify=y)


    cat_features=["Geography","Gender"]

    cat=CatBoostClassifier(learning_rate=0.1,n_estimators=47,max_depth=4,cat_features=cat_features)
    cat.fit(X_train,y_train)
    test_acc=cat.score(X_test,y_test)
    train_acc=cat.score(X_train,y_train)
    print("Test Score {:.2f} %".format(test_acc*100))
    print("Train Score {:.2f} %".format(train_acc*100))
    return test_acc,train_acc


#test_acc,train_acc=classification()
#print("Test",test_acc)
#print("Train",train_acc)