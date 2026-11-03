# Credit Card Fraud Detection Analysis

## Project Overview
This project focuses on analyzing credit card transactions to identify fraudulent activities and understand transaction patterns using data analysis and machine learning techniques.

The project uses exploratory data analysis (EDA) and classification algorithms to distinguish between genuine and fraudulent transactions.

## Problem Statement
Credit card fraud is a major financial risk. Identifying fraudulent transactions within large volumes of financial data is challenging due to the highly imbalanced nature of transaction datasets.

## Project Objectives
- Analyze financial transaction patterns.
- Identify differences between genuine and fraudulent transactions.
- Perform exploratory data analysis.
- Build machine learning classification models.
- Evaluate model performance using appropriate metrics.
- Interpret results from a financial risk perspective.

## Dataset
**Source:** [Kaggle – Credit Card Fraud Detection](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)

Dataset features include:
- Time: Seconds elapsed between a transaction and the first transaction.
- V1–V28: Anonymized features obtained through PCA transformation.
- Amount: Transaction amount.
- Class: Target variable (0 = Genuine, 1 = Fraudulent).

## Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Jupyter Notebook

## Project Workflow

### 1. Data Cleaning and Exploratory Data Analysis
- Dataset inspection and validation.
- Missing values and duplicate checks.
- Outlier analysis.
- Transaction distribution analysis.
- Fraud vs. genuine transaction analysis.
- Feature correlation analysis.

### 2. Machine Learning
- Train-test split.
- Feature scaling.
- Logistic Regression.
- Decision Tree Classification.
- Random Forest Classification.

### 3. Model Evaluation
- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix
- ROC-AUC

### 4. Risk Interpretation
- Identification of fraudulent transaction patterns.
- Analysis of false positives and false negatives.
- Evaluation of fraud detection effectiveness.

## Current Project Status
**In Progress**

Completed:
- Data cleaning and validation.
- Exploratory Data Analysis.
- Initial Logistic Regression implementation.
- Initial accuracy evaluation.

Upcoming:
- Detailed model evaluation.
- Handling class imbalance.
- Decision Tree and Random Forest.
- Model comparison.
- Final business and risk interpretation.

## Expected Outcome
An analytical study of credit card transaction patterns and a machine learning-based approach to identifying fraudulent transactions, supported by model evaluation and financial risk interpretation.
