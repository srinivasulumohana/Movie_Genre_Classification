# Movie_Genre_Classification

COMPANY : CODTECH IT SOLUTIONS PVT.LTD 
NAME : Mohana Srinivasulu 
INTERN ID : CITS1567 
DOMAIN : Machine Learning 
DURATION : 6 Weeks 
MENTOR : Neela Santhosh Kumar



🎬 Movie Genre Classification using Machine Learning


📌 Project Overview


The Movie Genre Classification project is a complete Machine Learning and Natural Language Processing (NLP) application developed using Python, Scikit-learn, Pandas, Streamlit, and TF-IDF Vectorization. The main objective of this project is to automatically predict the genre of a movie based on its description or plot summary.

This project demonstrates the practical implementation of text classification using Machine Learning algorithms. The system analyzes movie descriptions, preprocesses textual data, extracts important features, and predicts the most appropriate movie genre with high accuracy.

The project uses a real-world IMDb movie dataset downloaded from Kaggle and follows the complete workflow of an end-to-end Machine Learning application.

The project includes:

Dataset Collection
Text Preprocessing
Exploratory Data Analysis
Feature Extraction
Machine Learning Model Development
Model Evaluation
Genre Prediction System
Streamlit Dashboard Development

This project is beginner-friendly and highly useful for students learning Data Science, Machine Learning, Artificial Intelligence, and Natural Language Processing.

📖 Introduction

The entertainment industry generates a massive amount of movie-related data every year. Movie streaming platforms and recommendation systems require automatic genre classification to organize movies efficiently and improve user recommendations.

Traditionally, movie genres are manually assigned, which can be time-consuming and inconsistent. Machine Learning and Natural Language Processing techniques help automate this process by analyzing movie plot summaries and predicting movie genres accurately.

The Movie Genre Classification project solves this problem by implementing Machine Learning models capable of understanding movie descriptions and automatically classifying them into genres such as Action, Comedy, Drama, Horror, Romance, Thriller, and more.

The project also demonstrates how textual data can be converted into numerical features suitable for Machine Learning algorithms.

🎯 Objectives of the Project

The major objectives of this project are:

To understand Natural Language Processing concepts
To work with real-world textual datasets
To preprocess movie descriptions for Machine Learning
To perform text-based Exploratory Data Analysis
To extract features using NLP techniques
To build Machine Learning classification models
To evaluate model performance using classification metrics
To develop a movie genre prediction system
To create an interactive dashboard using Streamlit

❓ Problem Statement

Movie streaming platforms and entertainment applications contain thousands of movies across different genres. Manually categorizing movies based on descriptions becomes difficult and inefficient as the dataset size increases.

The project aims to solve this issue by developing a Machine Learning-based classification system capable of:

Understanding movie plot descriptions
Extracting meaningful textual patterns
Automatically classifying movies into genres
Improving movie organization and recommendation systems

📂 Dataset Information

This project uses the IMDb Genre Classification Dataset downloaded from Kaggle.

Dataset Link:

https://www.kaggle.com/datasets/hijest/genre-classification-dataset-imdb

The dataset contains:

Movie ID
Movie Title
Genre
Movie Description

The dataset is stored in text format and loaded into Python using Pandas.

🛠 Technologies Used

The project was developed using the following tools and technologies:

Category	Technology
Programming Language	Python
IDE	Visual Studio Code
Data Processing	Pandas, NumPy
NLP	TF-IDF Vectorization
Machine Learning	Scikit-learn
Dashboard Development	Streamlit
Model Storage	Joblib
⚙️ Project Workflow

The project follows a complete Machine Learning and NLP workflow.

1️⃣ Data Collection

The dataset was downloaded from Kaggle and stored in text format. The dataset contains movie descriptions along with corresponding movie genres.

The dataset was loaded into Python using the Pandas library for preprocessing and analysis.

2️⃣ Data Cleaning

Data cleaning is an important stage of any Machine Learning project.

The following preprocessing operations were performed:

Removing missing values
Removing invalid records
Verifying dataset structure
Cleaning textual data

These preprocessing steps improve dataset quality and prepare the data for Machine Learning algorithms.

3️⃣ Text Preprocessing

Natural Language Processing techniques were applied to preprocess textual movie descriptions.

The following NLP techniques were used:

Text Cleaning
Stopword Removal
Lowercase Conversion
TF-IDF Vectorization

Text preprocessing helps convert raw textual movie descriptions into meaningful features suitable for Machine Learning models.

4️⃣ Feature Extraction

Machine Learning algorithms cannot directly understand raw text data. Therefore textual descriptions were converted into numerical vectors using TF-IDF Vectorization.

TF-IDF (Term Frequency – Inverse Document Frequency) helps identify important words in movie descriptions by assigning higher weights to meaningful terms.

Feature extraction converts textual movie descriptions into numerical features that can be processed by Machine Learning algorithms.

5️⃣ Exploratory Data Analysis (EDA)

EDA was performed to understand genre distribution and textual patterns within the dataset.

Different analyses were conducted to identify:

Most frequent genres
Important keywords
Text distribution
Relationships between textual features

EDA helps understand dataset characteristics and improves Machine Learning model performance.

6️⃣ Machine Learning Model Development

The project implements Machine Learning classification algorithms for predicting movie genres.

The project uses:

✅ Multinomial Naive Bayes

Multinomial Naive Bayes is highly effective for text classification problems because it performs efficiently on word-frequency features generated by TF-IDF Vectorization.

The dataset was divided into:

Training Data
Testing Data

The model was trained using training data and evaluated using testing data.

📈 Model Evaluation

The Machine Learning model was evaluated using:

Accuracy Score
Classification Report

Accuracy measures how correctly the model predicts movie genres.

The classification report includes:

Precision
Recall
F1-Score

These metrics help evaluate classification performance and prediction quality.

The model achieved good accuracy and demonstrated strong capability in predicting movie genres correctly.

🎬 Genre Prediction System

The project includes a prediction system where users can enter movie descriptions or plot summaries.

The trained Machine Learning model analyzes the text and predicts the most suitable movie genre automatically.

Example Predictions:

Movie Description	Predicted Genre
Superheroes fight aliens and save Earth	Action
Haunted house with evil spirits	Horror
Romantic story between two people	Romance
Detectives solving mysterious crimes	Thriller

The prediction system demonstrates practical implementation of NLP and Machine Learning in the entertainment domain.

🌐 Streamlit Dashboard

An interactive dashboard was developed using Streamlit to provide a user-friendly interface for movie genre prediction.

The dashboard allows users to:

Enter movie descriptions
Predict movie genres
Interact with the Machine Learning system
View example predictions

The dashboard converts the Machine Learning project into a professional web application.

📊 Dashboard Features

The Streamlit dashboard includes:

Movie Description Input
Genre Prediction Button
Real-Time Genre Prediction
Interactive User Interface
Example Predictions
Streamlit-Based Dashboard

The dashboard improves usability and allows users to interact with the prediction system easily.
















































































































