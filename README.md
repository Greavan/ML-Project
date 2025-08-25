# 📊 Student Performance Prediction - ML Project

## �� Project Overview

This is an **End-to-End Machine Learning Project** that predicts student performance (math scores) based on various demographic and academic factors. The project implements a complete ML pipeline from data ingestion to model deployment, featuring a user-friendly Streamlit web application for real-time predictions.

## �� Key Features

- **Complete ML Pipeline**: Data ingestion, transformation, model training, and prediction
- **Multiple ML Algorithms**: CatBoost, XGBoost, Random Forest, Decision Tree, and more
- **Interactive Web App**: Streamlit-based interface for easy predictions
- **Model Persistence**: Trained models and preprocessors saved for production use
- **Comprehensive EDA**: Detailed exploratory data analysis with visualizations
- **Hyperparameter Tuning**: Automated model optimization using RandomizedSearchCV

## 🎯 Problem Statement

The project addresses the question: **"How do various factors affect student performance in exams?"**

**Target Variable**: Math Score (Numerical)

**Features Analyzed**:
- Gender (Male/Female)
- Race/Ethnicity (Group A, B, C, D, E)
- Parental Level of Education
- Lunch Type (Standard/Free-Reduced)
- Test Preparation Course (Completed/None)
- Reading Score
- Writing Score

## 🏗️ Architecture
src/
├── components/ # Core ML components
│ ├── data_ingestion.py
│ ├── data_transformation.py
│ └── model_trainer.py
├── pipeline/ # Training and prediction pipelines
│ ├── train_pipeline.py
│ └── predict_pipeline.py
├── utils.py # Utility functions
├── logger.py # Logging configuration
└── exception.py # Custom exception handling

## ��️ Technologies Used

- **Machine Learning**: Scikit-learn, CatBoost, XGBoost
- **Data Processing**: Pandas, NumPy
- **Visualization**: Matplotlib, Seaborn
- **Web Framework**: Streamlit
- **Model Persistence**: Pickle, Dill
- **Development**: Python, Jupyter Notebooks

## 📊 Dataset

- **Source**: [Kaggle - Students Performance in Exams](https://www.kaggle.com/datasets/spscientist/students-performance-in-exams)
- **Size**: 1000 rows × 8 columns
- **Features**: 7 input variables + 1 target variable

## 📈 Model Performance

The project evaluates multiple ML algorithms:
- **CatBoost Regressor** (Best Performance)
- **XGBoost Regressor**
- **Random Forest Regressor**
- **Decision Tree Regressor**
- **Gradient Boosting Regressor**
- **Linear Regression**
- **AdaBoost Regressor**

