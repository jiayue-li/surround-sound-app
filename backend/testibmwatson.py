import json
from watson_developer_cloud import NaturalLanguageClassifierV1

natural_language_classifier = NaturalLanguageClassifierV1(
  username='YOUR SERVICE USERNAME',
  password='YOUR SERVICE PASSWORD')

with open('../resources/weather_data_train.csv', 'rb') as training_data:
  classifier = natural_language_classifier.create(
    training_data=training_data,
    name='My Classfier',
    language='en'
  )
print(json.dumps(classifier, indent=2))
