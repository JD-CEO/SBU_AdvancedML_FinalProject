# Final Project: Advanced ML  SBU 2023

## Overview

This project encompasses multiple machine learning tasks, each aimed at solving distinct problems using various techniques. Students are encouraged to explore innovative solutions and provide thorough documentation of their approaches, challenges faced, and results obtained.

## Project Requirements

- Students must select at least **two tasks**, ensuring one is worth **2 points** and the other **5 points**.
- We decided to do 3 projects. Two with 5 points ( Task 3 and Task 2), one with 2 points (Persian Sentiment Analysis for Marketing)

## Tasks

### Task 1: Persian Sentiment Analysis for Marketing (2 points)
- **Objective**: Perform a 3-class sentiment analysis on a Persian dataset.
- **Dataset**: [Snappfood Dataset](https://hooshvare.github.io/docs/datasets/sa#snappfood)
- **Constraints**: No pre-trained models allowed; supplementary data from other sources is permitted.
- **Metric**: Weighted F1 score.

### Task 2: LLM Text Detection (5 points)
- **Objective**: Develop a model to detect whether an essay was written by a student or generated by an LLM.
- **Dataset**: Mix of student-written and LLM-generated essays.
  - [Kaggle Competition](https://www.kaggle.com/competitions/llm-detect-ai-generated-text/overview)
  - [Google Drive Link](https://drive.google.com/file/d/1Mgz5tZ-T0YBzgI8jB61JuRNscngvMy6n/view?usp=sharing)
- **Constraints**: Implement at least two models—one deep learning and one non-neural network. Both must perform adequately.
- **Metric**: ROC-AUC.

### Task 3: Reinforcement Learning (5 points)
- **Objective**: Create an environment and train an autonomous agent to play Tetris.
- **Constraints**: Use techniques proposed in papers from 2019 or later.
- **Innovation**: Creativity in your approach is highly valued for extra credit.

### Task 4: Few Shot Image Segmentation (5 points)
- **Objective**: Perform semantic segmentation using the FSS-1000 dataset.
- **Dataset**: [FSS-1000 Dataset](https://www.kaggle.com/datasets/meowmeowmeowmeowmeow/fss1000-a-1000-class-fewshot-segmentation/data)
  - [Alternative Link](https://drive.google.com/file/d/1ilimlQth8qSUOm7k1yeAcmyG-33pBbT/view?usp=sharing)
- **Constraints**: Must achieve mIoU > 80%; innovative architecture required.
- **Metric**: Mean Intersection over Union (mIoU).

### Task 5: Financial Market Prediction (2 points)
- **Objective**: Predict financial market trends (e.g., EURUSD or AAPL) using the triple barrier method.
- **Dataset**: Historical prices available [here](https://drive.google.com/file/d/1VHqRM5vp2sz0mEAtL7WbcmxtXcA0WM0T/view?usp=sharing).
- **Constraints**: Focus on classification rather than regression; assess precision and recall.
- **Metric**: Weighted F1 score.
