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

 url = "https://www.google.com"
 print(url)

 # f = open("markup.txt",'w',encoding='utf-8')
 # hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
 #    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
 #    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
 #    'Accept-Encoding': 'none',
 #    'Accept-Language': 'en-US,en;q=0.8',
 #    'Connection': 'keep-alive'}

 # request = urllib.request.Request(url,None,headers=hdr)
 # web = urllib.request.urlopen(request)

 # data = str(web.read())
 # f.write(data)
 # f.close()

 prediction = get_prediction_from_url(url)

 # Print the probability of prediction (if needed)
 # prob = clf.predict_proba(features_test)
 # print 'Features=', features_test, 'The predicted probability is - ', prob, 'The predicted label is - ', pred
 #    print "The probability of this site being a phishing website is ", features_test[0]*100, "%"

 if prediction == 1:
     # print "The website is safe to browse"
     print("SAFE")
     return 'SAFE'
 elif prediction == -1:
     # print "The website has phishing features. DO NOT VISIT!"
     print("MALICIOUS WEBSITE")
     return 'MALICIOUS WEBSITE'

     # print 'Error -', features_test

if __name__ == "__main__":
 main()
