
# Amazon Reviews Data Mining with MapReduce (MRJob)

## Project Description

This project applies the MapReduce programming model using Python's **MRJob** framework to analyze large-scale Amazon customer review data in **Pycharm** . The aim is to demonstrate how distributed data processing can be used to extract valuable insights from massive datasets.

The project performs five analytical tasks:

* Count the total number of reviews
* Identify the Top 10 most reviewed products
* Calculate the average helpfulness score of reviews
* Perform sentiment analysis on customer reviews
* Compute the average rating per product

## Dataset

The analysis uses Amazon customer review data in JSON format. Each review record contains information such as:

* Product ID (`parent_asin`)
* Review text
* Star rating
* Helpful votes
* Total votes

Example:

```json
{
  "parent_asin": "B001234",
  "rating": 5,
  "helpful_vote": 10,
  "total_vote": 12,
  "text": "Excellent product!"
}
```

## Technologies Used

* Python 3
* MRJob in Pycharm
* JSON

## Project Structure

```text
├── count_reviews.py
├── top10_reviewed_products.py
├── average_helpfulness_score.py
├── sentiment_analysis.py
├── average_rating_per_product.py
├── data/
└── README.md
```

## Analysis Tasks

### 1. Count Reviews

Calculates the total number of reviews in the dataset.

### 2. Top 10 Most Reviewed Products

Identifies products with the highest review counts.

### 3. Average Helpfulness Score

Calculates:

```
Helpfulness Score = Helpful Votes / Total Votes
```

and determines the overall average helpfulness score.

### 4. Sentiment Analysis

Classifies reviews into:

* Positive
* Neutral
* Negative

to understand overall customer sentiment.

### 5. Average Rating per Product

Calculates the mean star rating for each product based on customer reviews.

## How to Run

Install MRJob:

```bash
pip install mrjob
```

Run a job:

```bash
python count_reviews.py reviews.json
```

Examples:

```bash
python top10_reviewed_products.py reviews.json
python average_helpfulness_score.py reviews.json
python sentiment_analysis.py reviews.json
python average_rating_per_product.py reviews.json
```

## Sample Results

### Sentiment Distribution

| Sentiment |     Count |
| --------- | --------: |
| Positive  | 1,535,553 |
| Neutral   |   223,337 |
| Negative  |   321,123 |

### Insights

* Most reviews are positive, indicating generally favorable customer experiences.
* A small number of products account for a large share of total reviews.
* Helpfulness scores provide insight into review quality and trustworthiness.
* Average ratings help identify highly rated products.

---

A nice addition on GitHub is to include screenshots of your output results under a **Results** section. Repositories with screenshots tend to look more professional and attract more attention from recruiters and lecturers.
