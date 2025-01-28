from transformers import pipeline

# Load sentiment analysis pipeline
sentiment_analyzer = pipeline("sentiment-analysis")

def analyze_text(text):
    result = sentiment_analyzer(text)[0]
    return {"label": result["label"], "score": result["score"]}

def hello(text):
    return {"label":"Helloo"}