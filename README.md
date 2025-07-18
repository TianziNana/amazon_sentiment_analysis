# amazon_sentiment_analysis


# Amazon Beauty Reviews Sentiment Analysis

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Complete-brightgreen.svg)]()

A comprehensive sentiment analysis study of Amazon beauty product reviews, examining the relationship between textual sentiment and numerical ratings using large-scale data.

## 🎯 Project Overview

This project analyzes **701,528 reviews** from **631,986 users** to understand how sentiment expressed in review text relates to numerical ratings. The study employs multiple analytical approaches including correlation analysis, regression modeling, time-series analysis, and user clustering.

### Key Findings
- **Strong sentiment-rating correlation**: r = 0.613 (p < 0.001)
- **Predictive power**: Sentiment explains 34.9% of rating variance (R² = 0.349)
- **User segmentation**: 4 distinct user groups with different behavior patterns
- **Temporal consistency**: Sentiment changes predict rating changes (β = 1.586)

## 📊 Results Summary

| Metric | Value | Interpretation |
|--------|-------|----------------|
| Overall Correlation | 0.613 | Strong positive relationship |
| Model R² | 0.349 | Large effect size |
| Prediction Accuracy | 73.2% | Rating category prediction |
| User Clusters | 4 | Distinct behavioral patterns |

## 🚀 Quick Start

### Installation
```bash
git clone https://github.com/yourusername/amazon-sentiment-analysis.git
cd amazon-sentiment-analysis
pip install -r requirements.txt
```

### Basic Usage
```python
from src.analysis.sentiment_analyzer import SentimentAnalyzer
from src.modeling.regression_models import SentimentRatingModel

# Initialize analyzer
analyzer = SentimentAnalyzer()

# Analyze sentiment
sentiment_scores = analyzer.analyze_reviews(reviews_data)

# Build predictive model
model = SentimentRatingModel()
model.fit(sentiment_scores, ratings)
predictions = model.predict(new_sentiments)
```

## 🔍 Methodology

### Data Processing
- **Dataset**: Amazon Beauty Product Reviews (2023)
- **Scale**: 701,528 reviews, 631,986 users
- **Preprocessing**: Text cleaning, feature engineering, memory optimization

### Sentiment Analysis
- **Tool**: VADER (Valence Aware Dictionary and sEntiment Reasoner)
- **Validation**: Manual verification, correlation analysis
- **Output**: Compound scores [-1, +1]

### Statistical Analysis
- **Cross-sectional**: Correlation analysis across user groups
- **Time-series**: Longitudinal analysis of multi-review users
- **Modeling**: Linear regression with effect size calculation
- **Clustering**: K-means user segmentation

### Key Innovations
- **Memory-efficient processing**: Custom algorithms for large-scale data
- **Manual statistical functions**: Environment-independent implementations
- **Multi-level validation**: Cross-sectional, temporal, and predictive validation

## 📈 Key Results

### 1. Sentiment-Rating Correlation
- **Overall**: r = 0.613 (strong positive correlation)
- **Single-review users**: r = 0.611
- **Multi-review users**: r = 0.619
- **Temporal changes**: r = 0.541

### 2. Predictive Models
- **Sentiment → Rating**: β = 1.719, R² = 0.349
- **Sentiment Change → Rating Change**: β = 1.586, R² = 0.306
- Both models show large effect sizes (R² > 0.25)

### 3. User Segmentation
- **Stable Satisfied (56%)**: High sentiment, low volatility
- **Low Participation-Negative (19.5%)**: Low sentiment, low ratings
- **Low Participation-Neutral (21.8%)**: Moderate sentiment, high volatility
- **Volatile Active (2.8%)**: High activity, high sentiment volatility

## 🎨 Visualizations

Interactive dashboards and charts available in `/results/figures/`:
- [Correlation Analysis](results/figures/correlation_analysis.html)
- [User Segmentation](results/figures/user_segmentation.html)
- [Model Performance](results/figures/model_performance.html)

## 📁 Project Structure

```
├── src/              # Source code modules
├── data/             # Raw and processed data
├── notebooks/        # Jupyter analysis notebooks
├── results/          # Output figures and reports
├── tests/            # Unit tests
└── docs/             # Documentation
```

## 🔧 Technical Details

### Requirements
- Python 3.8+
- pandas, numpy, scipy
- vaderSentiment
- plotly
- scikit-learn

### Performance Optimizations
- **Memory management**: Chunked processing for large datasets
- **Custom statistics**: Hand-written functions to avoid library dependencies
- **Efficient sampling**: Stratified sampling for representative analysis

### Reproducibility
- **Random seeds**: Fixed for consistent results
- **Version control**: All dependencies pinned
- **Documentation**: Comprehensive code comments

## 📊 Business Applications

### User Experience
- **Sentiment-based recommendations**: Personalized product suggestions
- **Early warning systems**: Identify dissatisfied users
- **Quality monitoring**: Automated review quality assessment

### Platform Operations
- **User segmentation**: Targeted marketing strategies
- **Risk prediction**: Churn prediction based on sentiment trends
- **Content moderation**: Identify inconsistent sentiment-rating patterns

## 🔬 Academic Contributions

### Methodological
- Large-scale validation of sentiment-rating relationships
- Environment-independent statistical implementations
- Multi-method validation framework

### Empirical
- Comprehensive analysis of e-commerce user behavior
- Quantification of sentiment-rating relationship strength
- User behavior pattern identification

## 📚 Documentation

- [Methodology](docs/methodology.md): Detailed analytical approach
- [Data Dictionary](docs/data_dictionary.md): Variable definitions
- [API Reference](docs/api_reference.md): Code documentation
- [Tutorial](docs/tutorial.md): Step-by-step usage guide

## 🧪 Testing

Run tests with:
```bash
python -m pytest tests/
```

Coverage report:
```bash
python -m pytest tests/ --cov=src/
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📞 Contact

Your Name - your.email@example.com

Project Link: https://github.com/yourusername/amazon-sentiment-analysis

## 🙏 Acknowledgments

- Amazon for providing the dataset
- VADER sentiment analysis tool developers
- Open source community for Python libraries

## 📖 Citation

If you use this work in your research, please cite:

```bibtex
@misc{amazon_sentiment_analysis_2024,
  title={Amazon Beauty Reviews Sentiment Analysis: Large-Scale User Behavior Study},
  author={Your Name},
  year={2024},
  url={https://github.com/yourusername/amazon-sentiment-analysis}
}
```
```

---

