import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {
        "Content-Type": "application/json",
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    payload = {
        "raw_document": {
            "text": text_to_analyze
        }
    }
    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()
    result = json.loads(response.text)
    emotions = result['emotionPredictions'][0]['emotion']
    required_emotions = ['anger', 'disgust', 'fear', 'joy', 'sadness']
    output = {emotion: emotions[emotion] for emotion in required_emotions}
    dominant_emotion = max(output, key=output.get)
    output['dominant_emotion'] = dominant_emotion
    return output
