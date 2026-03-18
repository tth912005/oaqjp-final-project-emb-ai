import requests
import json

def emotion_detector(text_to_analyse):
    # Kiểm tra đầu vào rỗng (Dành cho Task 7)
    if not text_to_analyse.strip():
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }
    
    response = requests.post(url, json=myobj, headers=headers)
    
    # Nếu API trả về lỗi (VD: 400 Bad Request)
    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
        
    formatted_response = json.loads(response.text)
    
    # Trích xuất điểm số của các cảm xúc
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    
    # Tìm cảm xúc có điểm số cao nhất
    dominant_emotion = max(emotions, key=emotions.get)
    
    # Trả về kết quả theo format yêu cầu của Task 3
    return {
        'anger': emotions['anger'],
        'disgust': emotions['disgust'],
        'fear': emotions['fear'],
        'joy': emotions['joy'],
        'sadness': emotions['sadness'],
        'dominant_emotion': dominant_emotion
    }
