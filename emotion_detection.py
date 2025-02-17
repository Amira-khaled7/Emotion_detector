# import packagest 
import requests
import json 

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyze } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = myobj, headers = header )
    
    formatted_response = json.loads(response)
    emotions = formatted_response['emotionPredictions'][0]
    anger_score = emotions['emotion']['anger']
    disgust_score = emotions['emotion']['disgust']
    fear_score = emotions['emotion']['fear']
    joy_score = emotions['emotion']['joy']
    sadness_score = emotions['emotion']['sadness']
    dominate
    return response.text
