"""
Amazon Beauty Reviews Sentiment Analysis

This module provides sentiment analysis functionality for Amazon review data.
"""

import pandas as pd
import numpy as np
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from typing import List, Dict, Any
import gc


class SentimentAnalyzer:
    """
    A sentiment analysis class for processing Amazon reviews using VADER.
    
    This class handles large-scale sentiment analysis with memory optimization
    and provides comprehensive validation capabilities.
    """
    
    def __init__(self, batch_size: int = 10000):
        """
        Initialize the sentiment analyzer.
        
        Args:
            batch_size (int): Number of reviews to process in each batch
        """
        self.analyzer = SentimentIntensityAnalyzer()
        self.batch_size = batch_size
        self.results = {}
        
    def analyze_reviews(self, reviews: List[str]) -> List[float]:
        """
        Analyze sentiment for a list of reviews.
        
        Args:
            reviews (List[str]): List of review texts
            
        Returns:
            List[float]: List of compound sentiment scores
        """
        sentiments = []
        
        # Process in batches to manage memory
        for i in range(0, len(reviews), self.batch_size):
            batch = reviews[i:i + self.batch_size]
            batch_sentiments = [
                self.analyzer.polarity_scores(text)['compound'] 
                for text in batch
            ]
            sentiments.extend(batch_sentiments)
            
            # Progress reporting
            if i % (self.batch_size * 10) == 0:
                print(f"Processed {min(i + self.batch_size, len(reviews))}/{len(reviews)} reviews")
            
            # Memory management
            del batch, batch_sentiments
            if i % (self.batch_size * 50) == 0:
                gc.collect()
        
        return sentiments
    
    def analyze_dataframe(self, df: pd.DataFrame, text_column: str = 'text') -> pd.DataFrame:
        """
        Analyze sentiment for a pandas DataFrame.
        
        Args:
            df (pd.DataFrame): DataFrame containing review data
            text_column (str): Name of the column containing review text
            
        Returns:
            pd.DataFrame: DataFrame with added sentiment column
        """
        print(f"Analyzing sentiment for {len(df)} reviews...")
        
        # Extract text and analyze
        review_texts = df[text_column].tolist()
        sentiments = self.analyze_reviews(review_texts)
        
        # Add sentiment to dataframe
        df_result = df.copy()
        df_result['sentiment'] = sentiments
        
        print("Sentiment analysis completed!")
        return df_result
    
    def validate_sentiment_quality(self, df: pd.DataFrame, 
                                  sample_size: int = 1000) -> Dict[str, Any]:
        """
        Validate the quality of sentiment analysis results.
        
        Args:
            df (pd.DataFrame): DataFrame with sentiment and rating columns
            sample_size (int): Number of samples to use for validation
            
        Returns:
            Dict[str, Any]: Validation results
        """
        # Sample data for validation
        if len(df) > sample_size:
            sample = df.sample(n=sample_size, random_state=42)
        else:
            sample = df.copy()
        
        # Calculate correlation
        correlation = self.manual_correlation(
            sample['sentiment'].tolist(),
            sample['rating'].tolist()
        )
        
        # Analyze sentiment distribution
        sentiment_stats = {
            'mean': sample['sentiment'].mean(),
            'std': sample['sentiment'].std(),
            'min': sample['sentiment'].min(),
            'max': sample['sentiment'].max()
        }
        
        # Identify anomalies
        high_rating_negative = len(sample[
            (sample['rating'] >= 4) & (sample['sentiment'] < -0.1)
        ])
        low_rating_positive = len(sample[
            (sample['rating'] <= 2) & (sample['sentiment'] > 0.1)
        ])
        
        anomaly_rate = (high_rating_negative + low_rating_positive) / len(sample)
        
        validation_results = {
            'correlation': correlation,
            'sentiment_stats': sentiment_stats,
            'anomaly_rate': anomaly_rate,
            'sample_size': len(sample),
            'high_rating_negative': high_rating_negative,
            'low_rating_positive': low_rating_positive
        }
        
        return validation_results
    
    @staticmethod
    def manual_correlation(x: List[float], y: List[float]) -> float:
        """
        Calculate Pearson correlation coefficient manually.
        
        Args:
            x (List[float]): First variable
            y (List[float]): Second variable
            
        Returns:
            float: Correlation coefficient
        """
        n = len(x)
        if n != len(y) or n < 2:
            return 0.0
        
        # Calculate means
        x_mean = sum(x) / n
        y_mean = sum(y) / n
        
        # Calculate correlation
        numerator = sum((x[i] - x_mean) * (y[i] - y_mean) for i in range(n))
        sum_sq_x = sum((x[i] - x_mean) ** 2 for i in range(n))
        sum_sq_y = sum((y[i] - y_mean) ** 2 for i in range(n))
        
        if sum_sq_x == 0 or sum_sq_y == 0:
            return 0.0
        
        denominator = (sum_sq_x * sum_sq_y) ** 0.5
        return numerator / denominator
    
    def categorize_sentiment(self, sentiment_score: float) -> str:
        """
        Categorize sentiment score into negative, neutral, or positive.
        
        Args:
            sentiment_score (float): VADER compound score
            
        Returns:
            str: Sentiment category
        """
        if sentiment_score < -0.1:
            return 'negative'
        elif sentiment_score > 0.1:
            return 'positive'
        else:
            return 'neutral'
    
    def get_sentiment_summary(self, df: pd.DataFrame) -> Dict[str, Any]:
        """
        Generate a comprehensive sentiment analysis summary.
        
        Args:
            df (pd.DataFrame): DataFrame with sentiment column
            
        Returns:
            Dict[str, Any]: Summary statistics
        """
        # Basic statistics
        sentiment_stats = {
            'total_reviews': len(df),
            'mean_sentiment': df['sentiment'].mean(),
            'std_sentiment': df['sentiment'].std(),
            'min_sentiment': df['sentiment'].min(),
            'max_sentiment': df['sentiment'].max()
        }
        
        # Sentiment categories
        df['sentiment_category'] = df['sentiment'].apply(self.categorize_sentiment)
        category_counts = df['sentiment_category'].value_counts()
        
        sentiment_distribution = {
            'negative': category_counts.get('negative', 0),
            'neutral': category_counts.get('neutral', 0),
            'positive': category_counts.get('positive', 0)
        }
        
        # Percentages
        sentiment_percentages = {
            category: (count / len(df)) * 100 
            for category, count in sentiment_distribution.items()
        }
        
        return {
            'basic_stats': sentiment_stats,
            'distribution': sentiment_distribution,
            'percentages': sentiment_percentages
        }


def main():
    """
    Example usage of the SentimentAnalyzer class.
    """
    # Sample data
    sample_reviews = [
        "I love this product! It's amazing and works perfectly.",
        "Terrible quality, would not recommend to anyone.",
        "It's okay, nothing special but decent for the price.",
        "Outstanding! Exceeded all my expectations.",
        "Waste of money, completely useless product."
    ]
    
    sample_ratings = [5, 1, 3, 5, 1]
    
    # Initialize analyzer
    analyzer = SentimentAnalyzer(batch_size=1000)
    
    # Analyze sentiment
    sentiments = analyzer.analyze_reviews(sample_reviews)
    
    # Create DataFrame
    df = pd.DataFrame({
        'text': sample_reviews,
        'rating': sample_ratings,
        'sentiment': sentiments
    })
    
    # Validate quality
    validation_results = analyzer.validate_sentiment_quality(df)
    
    # Generate summary
    summary = analyzer.get_sentiment_summary(df)
    
    print("Sentiment Analysis Results:")
    print(f"Correlation: {validation_results['correlation']:.3f}")
    print(f"Mean sentiment: {summary['basic_stats']['mean_sentiment']:.3f}")
    print(f"Sentiment distribution: {summary['distribution']}")


if __name__ == "__main__":
    main()
