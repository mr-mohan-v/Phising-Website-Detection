from flask import Flask, request, render_template
# from test import main
from train import train_me
import urllib
import requests
from urllib.request import urlopen

#tes

import joblib
import features_extraction
import sys
import numpy as np
import urllib.request
from features_extraction import LOCALHOST_PATH, DIRECTORY_NAME

def get_prediction_from_url(test_url):
    features_test = features_extraction.main(test_url)
    # Due to updates to scikit-learn, we now need a 2D array as a parameter to the predict function.
    features_test = np.array(features_test).reshape((1, -1))

    rf = joblib.load(r'C:\Users\Mohan\Downloads\Malicious-Web-Content-Detection-using-Random-Forest-master\Malicious-Web-Content-Detection-using-Random-Forest-master\classifier\random_forest.pkl')

    pred = rf.predict(features_test)
    return int(pred[0])

def main():
    
    url = check_url.url
    print(url)
    prediction = get_prediction_from_url(url)

    # Print the probability of prediction (if needed)
    # prob = clf.predict_proba(features_test)
    # print 'Features=', features_test, 'The predicted probability is - ', prob, 'The predicted label is - ', pred
    #    print "The probability of this site being a phishing website is ", features_test[0]*100, "%"

    if prediction == 1:
        print("The website is safe to browse")
        print("SAFE WEBSITE")
        return '<body style="background-color:green;"><center style="margin-top:300px; margin-bottom:50px; font-size:36px; color:white; font-weight:bold;">SAFE WEBSITE</center>' \
               '<div><center><button onclick="window.history.back();">Check Again</button></div></center></body>'
        
    elif prediction == -1:
        print ("The website has phishing features. DO NOT VISIT!")
        print("MALICIOUS WEBSITE")
        return '<body style="background-color:RED;"><center style="margin-top:300px; margin-bottom:50px; font-size:36px; color:white; font-weight:bold;">MALICIOUS WEBSITE</center>' \
               '<div><center><button onclick="window.history.back();">Check Again</button></div></center></body>'

        # print 'Error -', features_test

app = Flask(__name__ , template_folder="Extension")

@app.route("/")
def home():
    return render_template("popup.html")

@app.route("/check/", methods=['POST'])
def check_url():
    check_url.url=request.form.get("url")
    try:
        urllib.request.urlretrieve(check_url.url, "markup.txt")
    except Exception as e:
        print("malicious")
        print(e)
        return "Error occurred while scrapting web content: " + str(e)
    print("In Here")
    return main()
    # return render_template("predict.html",predict= prediction)
    
@app.route("/train/", methods=['GET'])
def train_model():
    return train_me()
    
if __name__ == "__main__":
    app.run(debug=True, port=8000)

