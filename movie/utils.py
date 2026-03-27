from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


analyzer = SentimentIntensityAnalyzer()
def analyze_opinion(movie_review):
    score = analyzer.polarity_scores(movie_review)
    print("The score is", score)
    
    compound = score['compound']
   
    if compound >= 0.05:
        return "POSTIVE"
    elif compound <0.05:
        return "NEGATIVE"
    else:
        return "NEUTRAL"
        