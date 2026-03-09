# Credit Default Predictor

A multimodal machine learning project for predicting credit default using financial data and text-based features.

## Overview

This project explores credit default prediction by combining structured financial data with text-based information to build predictive models. It includes data exploration, cleaning, feature engineering, baseline modeling, and deep learning experiments using an LSTM-based approach.

The goal is to understand how multiple data sources can improve credit risk prediction and support better decision-making in financial analytics.

## Project Objectives

- Explore patterns in credit default data
- Clean and prepare structured and text-based features
- Engineer features for predictive modeling
- Build a baseline machine learning model
- Experiment with an LSTM-based deep learning model
- Compare approaches for credit default prediction

## Tools and Technologies

- Python
- Pandas
- NumPy
- Scikit-learn
- Jupyter Notebook
- PyTorch or TensorFlow
- LSTM
- FinBERT
- Git/GitHub

## Project Workflow

### 1. Data Exploration
Understand the dataset structure, variable types, missing values, and early patterns related to default behavior.

### 2. Data Cleaning
Prepare the dataset by handling missing values, fixing inconsistencies, and creating analysis-ready data.

### 3. Feature Engineering
Create useful structured and text-based features for modeling.

### 4. Baseline Model
Build a simple machine learning baseline to establish initial predictive performance.

### 5. Deep Learning Model
Train an LSTM-based model to capture deeper patterns in the data and compare performance against the baseline.

## Repository Structure

```text
credit_default_project/
│
├── notebooks/
│   ├── 01_data_exploration.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_feature_engineering.ipynb
│   ├── 04_baseline_model.ipynb
│   └── 05_lstm_model.ipynb
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── features/
│
├── src/
│   ├── data_collection.py
│   ├── feature_engineering.py
│   └── models.py
│
├── outputs/
│   ├── models/
│   ├── visualizations/
│   └── reports/
│
└── README.md
