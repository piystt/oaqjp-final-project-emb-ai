import requests
import json

#Define a function that takes a string input (text_to_analyse)
def emotion_detector(text_to_analyse):
# URL of the emotion detector service
	url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
# Constructing the request payload in the expected format
	myobj = { "raw_document": { "text": text_to_analyse } }
# Custom header specifying the model ID for the sentiment analysis service
	header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
# Sending a POST request to the emotion detection API
	response = requests.post(url, json=myobj,headers=header)
# Parsing the JSON response from the API
	formatted_response=json.loads(response.text)
# Find the dominant emotion
    dominant_emotion=max(formatted_response,key=formatted_response.get)
# Add the dominant emotion to the dictionary
    response.text['dominant_emotion']=dominant_emotion
# Return the text
	return response.text