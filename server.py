"""
Flask server cho ứng dụng Emotion Detection.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def sent_detector():
    """
    Nhận text, gọi hàm phân tích cảm xúc và trả về kết quả.
    Đã bổ sung xử lý lỗi đầu vào rỗng (Blank input).
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    
    # Task 7: Kiểm tra nếu dominant_emotion là None thì báo lỗi
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"
    
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
    Render giao diện chính (index.html).
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
