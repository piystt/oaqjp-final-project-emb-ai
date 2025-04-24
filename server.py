"""
This module sets up a basic Flask application.
It imports the Flask class to create an app instance, the render_template function
to render HTML templates, and the request object to handle incoming HTTP requests.
"""
# Import Flask, render_template, request from the flask pramework package
from flask import Flask, render_template, request
# Import the sentiment_analyzer function from the package created
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emo_detector():
    ''' This is an Emotion Detector.
    '''
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')
    # Pass the text to the sentiment_analyzer function and store the response
    response = emotion_detector(text_to_analyze)
    # Extract the dominant emotion and score from the response
    dominant_emotion = response['dominant_emotion']

    # Error handling
    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    # Return a formatted string with system response and dominant emotion
    return (f"For the given statement, the system response is {response}. "
        f"The dominant emotion is {dominant_emotion}")

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
