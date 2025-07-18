# Data Dictionary

## Raw Data Files

### All_Beauty.jsonl
Original Amazon review dataset containing individual review records.

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| `rating` | int | User rating (1-5 scale) | 5 |
| `title` | string | Review title | "Great product!" |
| `text` | string | Review text content | "I love this moisturizer..." |
| `images` | list | Review images (if any) | [] |
| `asin` | string | Amazon Standard Identification Number | "B08XYZ123" |
| `parent_asin` | string | Parent product identifier | "B08XYZ123" |
| `user_id` | string | Anonymous user identifier | "AE222BBOV..." |
| `timestamp` | datetime | Review timestamp | "2023-03-07 03:10:12" |
| `helpful_vote` | int | Number of helpful votes | 2 |
| `verified_purchase` | bool | Verified purchase indicator | true |

### meta_All_Beauty.jsonl
Product metadata containing information about beauty products.

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| `main_category` | string | Product main category | "Beauty" |
| `title` | string | Product title | "Moisturizing Face Cream" |
| `average_rating` | float | Average product rating | 4.2 |
| `rating_number` | int | Number of ratings | 1543 |
| `features` | list | Product features | ["Anti-aging", "Hydrating"] |
| `description` | string | Product description | "Premium face cream..." |
| `price` | float | Product price | 29.99 |
| `images` | list | Product images | ["url1", "url2"] |
| `videos` | list | Product videos | [] |
| `store` | string | Store name | "Beauty Store" |
| `categories` | list | Product categories | ["Beauty", "Skincare"] |
| `details` | dict | Product details | {"Brand": "XYZ"} |
| `parent_asin` | string | Parent product identifier | "B08XYZ123" |
| `bought_together` | list | Frequently bought together | [] |

## Processed Data Files

### data_cleaned.parquet
Cleaned and processed review data with sentiment analysis.

| Field | Type | Description | Range/Values |
|-------|------|-------------|--------------|
| `rating` | int8 | User rating | 1-5 |
| `text` | string | Cleaned review text | Variable length |
| `user_id` | category | User identifier | Categorical |
| `timestamp` | datetime64 | Review timestamp | 2013-2023 |
| `sentiment` | float32 | VADER sentiment score | -1.0 to 1.0 |
| `user_type` | string | User classification | "single", "multi" |
| `helpful_vote` | int8 | Helpful votes received | 0+ |
| `verified_purchase` | bool | Purchase verification | True/False |

### data_cross_sectional.parquet
User-level aggregated data for cross-sectional analysis.

| Field | Type | Description | Calculation |
|-------|------|-------------|-------------|
| `user_id` | string | User identifier | Unique identifier |
| `sentiment_mean` | float | Average user sentiment | Mean of user's sentiments |
| `sentiment_std` | float | Sentiment standard deviation | Std dev of user's sentiments |
| `sentiment_count` | int | Number of reviews | Count of user's reviews |
| `rating_mean` | float | Average user rating | Mean of user's ratings |
| `rating_std` | float | Rating standard deviation | Std dev of user's ratings |
| `timestamp_min` | datetime | First review timestamp | Earliest review date |
| `timestamp_max` | datetime | Last review timestamp | Latest review date |
| `time_span_days` | int | Review time span | Days between first and last |
| `user_type` | string | User classification | "single", "multi" |

### data_multi_users_timeseries.parquet
Time-series data for multi-review users with sequential features.

| Field | Type | Description | Calculation |
|-------|------|-------------|-------------|
| `user_id` | string | User identifier | Unique identifier |
| `rating` | int8 | Review rating | 1-5 scale |
| `sentiment` | float32 | Sentiment score | VADER compound score |
| `timestamp` | datetime64 | Review timestamp | Original timestamp |
| `prev_sentiment` | float32 | Previous sentiment | Lagged sentiment |
| `prev_rating` | int8 | Previous rating | Lagged rating |
| `sentiment_change` | float32 | Sentiment change | Current - Previous |
| `rating_change` | int8 | Rating change | Current - Previous |
| `sentiment_cumsum` | float32 | Cumulative sentiment | Running sum |
| `review_sequence` | int | Review sequence number | 1, 2, 3, ... |
| `sentiment_rolling_mean` | float32 | Rolling average sentiment | 3-period rolling mean |
| `sentiment_volatility` | float32 | Rolling sentiment volatility | 3-period rolling std |

## Analysis Results Files

### sentiment_validation.json
Results from sentiment analysis validation.

| Field | Type | Description |
|-------|------|-------------|
| `pearson_correlation` | float | Pearson correlation coefficient |
| `spearman_correlation` | float | Spearman correlation coefficient |
| `validation_score` | int | Overall validation score (0-5) |
| `sample_size` | int | Number of samples analyzed |
| `anomaly_rate` | float | Percentage of anomalous cases |
| `p_value` | float | Statistical significance |

### statistical_modeling.json
Statistical modeling results and coefficients.

| Field | Type | Description |
|-------|------|-------------|
| `model1_sentiment_change_to_rating_change` | dict | Change model results |
| `model2_sentiment_to_rating` | dict | Level model results |
| `sample_size` | int | Modeling sample size |
| `interpretation` | dict | Effect size interpretations |

### clustering_results.json
User clustering analysis results.

| Field | Type | Description |
|-------|------|-------------|
| `cluster_statistics` | dict | Statistics for each cluster |
| `cluster_names` | dict | Business names for clusters |
| `user_clusters` | dict | User-to-cluster assignments |

## Derived Variables

### Sentiment Categories
Based on sentiment score ranges:
- **Negative**: sentiment < -0.1
- **Neutral**: -0.1 ≤ sentiment ≤ 0.1
- **Positive**: sentiment > 0.1

### User Activity Levels
Based on review count:
- **Low Active**: < 5 reviews
- **High Active**: ≥ 5 reviews

### Effect Size Categories
Based on Cohen's criteria:
- **Small Effect**: R² ≥ 0.01
- **Medium Effect**: R² ≥ 0.09
- **Large Effect**: R² ≥ 0.25

## Data Quality Metrics

### Completeness
- **Rating**: 100% complete
- **Text**: 100% complete
- **User ID**: 100% complete
- **Timestamp**: 100% complete
- **Sentiment**: 100% complete (post-processing)

### Validity
- **Rating Range**: All values in 1-5 range
- **Sentiment Range**: All values in -1 to +1 range
- **Timestamp**: All dates between 2013-2023
- **User ID**: All values non-null and properly formatted

### Reliability
- **Sentiment Analysis**: Cross-validated with sample verification
- **User Classification**: Consistent across all datasets
- **Temporal Ordering**: Verified chronological sequence
- **Statistical Calculations**: Multiple validation approaches

## Missing Data Handling

### Original Data
- **Price**: ~75% missing (not used in analysis)
- **Store**: ~15% missing (not used in analysis)
- **Other fields**: <1% missing

### Processed Data
- **Sentiment_std**: Expected missing for single-review users
- **Rating_std**: Expected missing for single-review users
- **Prev_sentiment**: Expected missing for first reviews
- **Prev_rating**: Expected missing for first reviews

## Data Transformations

### Sentiment Analysis
- **Input**: Raw review text
- **Processing**: VADER sentiment analysis
- **Output**: Compound sentiment score [-1, +1]

### User Classification
- **Input**: Review count per user
- **Processing**: Count-based classification
- **Output**: "single" or "multi" user type

### Temporal Features
- **Input**: Timestamp sequences
- **Processing**: Lag creation and difference calculation
- **Output**: Change variables and rolling statistics

### Aggregation
- **Input**: Review-level data
- **Processing**: User-level aggregation
- **Output**: User summary statistics
