# Fake News Classifier (Philippines Fake News Datasets Corpus) 

The objective of this web application was to develop a prediction tool for classifying news articles. In today's digital age, social media platforms like Facebook, Twitter, and Reddit are notorious for spreading misinformation, commonly known as fake news. This misinformation can quickly circulate globally, deceiving individuals who lack accurate information. Fake news, often fabricated to mislead and tarnish reputations, poses significant risks by disseminating false information. In this project, the Naive Bayes Classifier algorithm was employed to train the model for accurate news classification and combat the spread of misinformation.

[![N|Solid](https://github.com/Senpaixyz/FakeNewsClassifier/blob/master/images/landingpage.PNG?raw=true)](https://github.com/Senpaixyz/FakeNewsClassifier/blob/master/images/landingpage.PNG)

## Fake News Characteristics

- The source of the news are not genuine/ trusted.
- There are some error regarding of phrase.
- Seek for attention words.
- Goood to be True.


## Features

- User Friendly Graphical User Interface.
- Responsive web application user interface.
- This Fake News Predictor WebApp used Naive Bayes Classifier algorithm for prediction and Philippines corpus datasets.
- The model has 94% accuracy from the trained datasets
- It can be deployed in realtime or be use as API.

## Instruction

- The input box only accept English phrases. It may result to wrong prediction if the user input different types of language.
- All news are dated from January 1, 2016 to October 31, 2018.


### Datasets

That datasets contains 14,802 'Credible' news and 7,666 'Not Credible' news. You can download [datasets](https://github.com/aaroncarlfernandez/Philippine-Fake-News-Corpus) from this Aaron Carl Fernandez github reporsitory. Below is the table that contains both Credible and Not Credible news dated from January 1, 2016 to October 31, 2018.

[![N|Datasets](https://github.com/Senpaixyz/FakeNewsClassifier/blob/master/images/datasets.PNG?raw=true)](https://github.com/Senpaixyz/FakeNewsClassifier/blob/master/images/datasets.PNG)

### Model Prediction
##### Facts News Prediction
The sample figure below shows the prediction of the model from the given phrase in the input box. The predicted news phrase was Facts News meaning the news that came from that source was legitamate truth.

[![N|Facts News](https://github.com/Senpaixyz/FakeNewsClassifier/blob/master/images/facts_news.PNG?raw=true)](https://github.com/Senpaixyz/FakeNewsClassifier/blob/master/images/facts_news.PNG)

##### Fake News Prediction
The predicted news phrase was Fake News meaning the news that came from that source was not legitamate and it is very indimidating since most of the Pilipino believe on the Fake News easily without proper doing some research.

[![N|Fake News](https://github.com/Senpaixyz/FakeNewsClassifier/blob/master/images/fake_news.PNG?raw=true)](https://github.com/Senpaixyz/FakeNewsClassifier/blob/master/images/fake_news.PNG)

## Packages
Additional Packages
| Package | URL |
| ------ | ------ |
| TFIDFVECT2 | [TFIDFVECT2](https://github.com/Senpaixyz/FakeNewsClassifier/blob/master/model/tfidfvect2.pkl)|
| NLTK | [NLTK](https://www.nltk.org/data.html) |
| Classifier | [Classifier PKL](https://github.com/Senpaixyz/FakeNewsClassifier/blob/master/model/classifier.pkl) |

## Installation

For first time use please download all the packages needed in this web application, please create virtual environment from the Pycharm IDE. Then open the terminal and run:

```sh
pip install -r requirements.txt
```
After use install all the dependency that needed in this web application. just simply type in the terminal:

```sh
python app.py
```
Verify the deployment by navigating to your server address in
your preferred browser.

```sh
http://127.0.0.1:5000/
```
This web application was supported by ngrok api. Uncomment this in the app.py to use it and shared this web application from another devices and via internet.

`//run_with_ngrok(app)`

## License

MIT

**Free Web Application Developed by Jheno Cerbito**
