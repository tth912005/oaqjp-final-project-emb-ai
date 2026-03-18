"""
Flask server cho ứng dụng Emotion Detection.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def sent_detector():
    """
    Route này nhận text từ giao diện web, gọi hàm phân tích cảm xúc
    và trả về chuỗi kết quả đã được định dạng.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    
    # Gọi hàm từ package bạn đã tạo
    response = emotion_detector(text_to_analyze)
    
    # Định dạng kết quả đầu ra theo yêu cầu của khóa học
    return (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, 'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, 'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )

@app.route("/")
def render_index_page():
    """
    Route này render giao diện chính của ứng dụng (file index.html).
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
