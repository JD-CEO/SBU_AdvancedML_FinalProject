# Persian Sentiment Analysis for Marketing

## Overview

This project aims to classify user comments from the Snappfood dataset into two sentiment categories: Happy and Sad. The analysis is performed using various machine learning and deep learning techniques while adhering to project constraints, including the prohibition of pre-trained models.

## Group Members

- Mehrdad Baradaran
- Hossein Yahyaei
- Katayoun Kobraei

## Table of Contents

1. [Introduction to Dataset](#introduction-to-dataset)
2. [Abstract](#abstract)
3. [Preprocessing](#preprocessing)
4. [Tokenizers and Models](#tokenizers-and-models)
   - [CountVectorizer & Logistic Regression](#countvectorizer--logistic-regression)
   - [TF-IDF Vectorizer & Logistic Regression](#tf-idf-vectorizer--logistic-regression)
   - [TF-IDF Vectorizer & Neural Network](#tf-idf-vectorizer--neural-network)
   - [Word Embeddings & LSTM](#word-embeddings--lstm)
   - [Byte Pair Encoding Tokenizer & LSTM](#byte-pair-encoding-tokenizer--lstm)
5. [Conclusion](#conclusion)

## Introduction to Dataset

The dataset used in this project is sourced from Snappfood, an online food delivery service in Iran. It contains **70,000 comments** with sentiment labels categorized into two classes: Happy (0) and Sad (1). The dataset includes three features:
- Comment text
- Sentiment label
- Label ID

You can access the dataset [here](https://hooshvare.github.io/docs/datasets/sa#snappfood).

## Abstract

This project focuses on a 2-class classification problem using the Snappfood dataset. Our goal is to develop models that accurately classify user comments to derive insights into customer sentiment for marketing strategies. We utilize various machine learning and deep learning methods, while our primary evaluation metric is the weighted F1 score.

## Preprocessing

Preprocessing is crucial to ensure the quality of input data for modeling. We utilized the **Hazm** library for natural language processing tasks in Persian. Key preprocessing steps included:

- **Data Cleaning**: Removed English words, converted Persian numbers to English, and replaced specific smileys and emojis with tokens.
- **URL Removal**: Extracted and removed URLs from comments.
- **Lowercasing and Whitespace Reduction**: Converted all characters to lowercase and reduced multiple whitespace characters.
- **Punctuation Removal**: Eliminated unnecessary punctuations.
- **Stop Words**: Defined and removed Persian stop words manually due to computational constraints.

After preprocessing, we saved the cleaned dataset for further analysis.

## Tokenizers and Models

To convert textual data into numerical vectors for model input, we implemented several vectorization methods and models:

### CountVectorizer & Logistic Regression

CountVectorizer transforms the text into a bag-of-words model. We trained a logistic regression model on the vectorized data and evaluated its performance.

### TF-IDF Vectorizer & Logistic Regression

We applied TF-IDF Vectorizer, which considers the frequency of words in the context of the entire dataset. A logistic regression model was then trained, yielding improved results over the CountVectorizer.

### TF-IDF Vectorizer & Neural Network

We constructed a simple neural network architecture with three hidden layers. The model exhibited signs of overfitting, and we plan to explore hyperparameter tuning for better performance.

### Word Embeddings & LSTM

Using word embeddings, we converted words into dense vectors. We trained a Bidirectional LSTM model to capture context from both directions, achieving better accuracy.

### Byte Pair Encoding Tokenizer & LSTM

We experimented with Byte Pair Encoding (BPE) for tokenization, allowing us to handle rare words effectively. Although the initial results were lower than expected, the model's potential can be improved with further training iterations.
