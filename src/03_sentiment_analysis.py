from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import pandas as pd
import os
from glob import glob

print("Loading FinBERT model... (this takes 2-3 minutes first time)")
tokenizer = AutoTokenizer.from_pretrained("ProsusAI/finbert")
model = AutoModelForSequenceClassification.from_pretrained("ProsusAI/finbert")

def analyze_sentiment(text):
    """
    Analyze sentiment of financial text
    Returns: sentiment (positive/negative/neutral) and confidence score
    """
    # Tokenize (FinBERT has 512 token limit)
    inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=512)
    
    # Get prediction
    outputs = model(**inputs)
    predictions = torch.nn.functional.softmax(outputs.logits, dim=-1)
    
    # Get sentiment
    sentiment_scores = predictions[0].tolist()
    labels = ['positive', 'negative', 'neutral']
    sentiment = labels[sentiment_scores.index(max(sentiment_scores))]
    confidence = max(sentiment_scores)
    
    return sentiment, confidence, sentiment_scores

# Find all processed text files
text_files = glob('data/sec_filings/**/*_clean.txt', recursive=True)

results = []

for filepath in text_files:
    print(f"\nAnalyzing {os.path.basename(filepath)}...")
    
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()
    
    # Analyze first 512 tokens
    sentiment, confidence, scores = analyze_sentiment(text[:2000])
    
    results.append({
        'file': os.path.basename(filepath),
        'sentiment': sentiment,
        'confidence': confidence,
        'positive_score': scores[0],
        'negative_score': scores[1],
        'neutral_score': scores[2]
    })
    
    print(f"  Sentiment: {sentiment} ({confidence:.2%} confidence)")

# Save results
df = pd.DataFrame(results)
df.to_csv('data/processed/sentiment_results.csv', index=False)
print(f"\n✅ Results saved! Analyzed {len(results)} filings")
print(df)
