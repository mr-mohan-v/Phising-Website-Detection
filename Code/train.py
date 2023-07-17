import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_curve, auc
from matplotlib.legend_handler import HandlerLine2D

def train_me():
    df = pd.read_csv(r'C:\\Users\\Mohan\\Downloads\\Malicious-Web-Content-Detection-using-Random-Forest-master\\Malicious-Web-Content-Detection-using-Random-Forest-master\\Training-Dataset.csv')
    X = df.drop(['SSL','non-standard_port','website_forwarding','statusbar_custom','disabling_right_click','popup_window','pagerank','number_of_links','target'], axis = 1)
    y = df['target']
    # from sklearn.model_selection import train_test_split
    # X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = 0.3,random_state = 0)
    
    # n_estimators = [1, 2, 4, 8, 16, 32, 64, 100, 200]
    # train_results = []
    # test_results =[]

    # for estimator in n_estimators:
    #     rf = RandomForestClassifier(n_estimators=estimator, n_jobs=-1)
    #     rf.fit(X_train, y_train)
    #     train_pred = rf.predict(X_train)
    #     false_positive_rate, true_positive_rate, thresholds = roc_curve(y_train, train_pred)
    #     roc_auc = auc(false_positive_rate, true_positive_rate)
    #     train_results.append(roc_auc)
    #     y_pred = rf.predict(X_test)
    #     false_positive_rate,true_positive_rate, thresholds = roc_curve(y_test, y_pred)
    #     roc_auc = auc(false_positive_rate, true_positive_rate)
    #     test_results.append(roc_auc)

    # line1, = plt.plot(n_estimators, train_results, "b",label="Train AUC")
    # # line2, = plt.plot(n_estimators, test_results, "r", label="Test AUC")
    # plt.legend(handler_map={line1: HandlerLine2D(numpoints=2)})
    # plt.ylabel("AUC score")
    # plt.xlabel("n_estimators")
    # plt.show()

    rf = RandomForestClassifier(n_estimators = 16, verbose= True)
    rf.fit(X, y)

    print("\n\n ""Random Forest Algorithm Results"" ")
    importances = rf.feature_importances_
    #std = np.std([tree.feature_importances_ for tree in rf.estimators_], axis=0)
    indices = np.argsort(importances)[::-1]
    # Print the feature ranking
    print("Feature ranking:")
    for f in range(X.shape[1]):
        print("%d. feature %d (%f)" % (f + 1, indices[f], importances[indices[f]]))

    joblib.dump(rf,r"C:\\Users\\Mohan\\Downloads\\Malicious-Web-Content-Detection-using-Random-Forest-master\\Malicious-Web-Content-Detection-using-Random-Forest-master\\classifier\random_forest.pkl", compress= 9 )
    return "Trained Success!!"


if __name__ == '__main__':
    train_me()
