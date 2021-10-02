from flask import Flask, render_template, request
import sklearn
from sklearn.preprocessing import StandardScaler
from sklearn.feature_extraction.text import CountVectorizer
from flask import escape
import jsonify
import requests
import pickle
import numpy as np
import random
import re
import nltk
import random
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

ps = PorterStemmer()
app = Flask(__name__)
classifier = pickle.load(open('model/classifier.pkl', 'rb'))
tfidf_v = pickle.load(open("model/tfidfvect2.pkl", 'rb'))
MESSAGE_LISTS = {
    'fact': {
        'label': 'This news is Fact!, The purpose of the news itself is to inform and to educate you as readers, listeners or viewers.',
        'img': '../static/img/facts.png',
    },
    'fake': {
        'label': 'This news is Fake, It often has the aim of damaging the reputation of a person or entity, or making money through advertising revenue.',
        'img': '../static/img/fake.png',
    }
}


@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html',
                           message_label="Fake news and hoaxes have been there since before the advent of the Internet. The widely accepted definition of Internet fake news is: fictitious articles deliberately fabricated to deceive readers”.",
                           img_label_path="../static/img/img_intro.png",
                           to_reset=False,
                           phrase_val=""
                           )
@app.route('/predict',methods=['POST'])
def predict():
    label = 1
    message_label = ""
    img_label_path = ""
    phrase = request.form['phrase']

    try:
        review = re.sub('[^a-zA-Z]', ' ', phrase)
        review = review.lower()
        review = review.split()
        review = [ps.stem(word) for word in review if not word in stopwords.words('english')]
        review = ' '.join(review)
        val = tfidf_v.transform([review]).toarray()
        label = classifier.predict(val)[0]
    except Exception as e:
        print('Theres something wrong....')
        print(e)
    print(label)
    if label == 0:
        message_label = MESSAGE_LISTS['fact']['label']
        img_label_path = MESSAGE_LISTS['fact']['img']
    elif label == 1:
        message_label = MESSAGE_LISTS['fake']['label']
        img_label_path = MESSAGE_LISTS['fake']['img']

    return render_template('index.html',
                           message_label = message_label,
                           img_label_path = img_label_path,
                           to_reset=True,
                           phrase_val=phrase
                           )


if __name__ == '__main__':
    app.run(host='0.0.0.0',port='3000',debug=True)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
