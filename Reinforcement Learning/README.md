# Tetris Reinforcement Learning Project

## Overview

This project focuses on creating an environment and training an autonomous agent to play Tetris using Reinforcement Learning (RL). We explore the challenges of applying RL to a delayed reward system, such as Tetris, and implement solutions inspired by recent research (post-2019).
Complete documentation is provided in [[Report](https://github.com/JD-CEO/SBU_AdvancedML_FinalProject/blob/main/Reinforcement%20Learning/Tetris.pdf)]
## Group Members

- Hossein Yahyaei
- Katayoun Kobraei
- Mehrdad Baradarn

## Table of Contents

1. [Abstract](#abstract)
2. [Introduction](#introduction)
3. [Project Goals](#project-goals)
4. [Environment Setup](#environment-setup)
5. [Methodology](#methodology)
   - [Algorithm Selection](#algorithm-selection)
   - [Model Architecture](#model-architecture)
   - [Experiment Overview](#experiment-overview)
6. [Results](#results)
7. [Conclusion](#conclusion)

## Abstract

In this work, we address the challenges posed by delayed reward functions in the Tetris environment, known for its complexity in applying machine learning techniques like Q-learning. Tetris features a sparse reward system, making it difficult for an agent to learn effectively due to the vast number of possible game states and actions. We investigate these challenges and discuss our innovative approaches to overcoming them.

## Introduction

Recent advancements in artificial intelligence have enabled applications across various fields, with reinforcement learning (RL) emerging as a prominent technique for solving complex decision-making problems. RL algorithms define an environment through states, actions, and expected rewards, enabling autonomous decision-making to maximize future rewards. However, RL faces limitations in real-world applications characterized by irregular and high-dimensional data, particularly in environments like Tetris with delayed rewards. These challenges necessitate extensive exploration and learning episodes for agents to effectively grasp the game dynamics.

## Project Goals

- Create a Tetris game environment.
- Develop a reinforcement learning agent capable of learning to play Tetris.
- Implement innovative reward structures and learning techniques to enhance agent performance.

## Environment Setup

We sourced our Tetris game environment from existing repositories on GitHub and modified it to fit our needs. The environment allows the agent to observe game states and take actions based on its learned strategies.

### Requirements

- Python 3.x
- Libraries: `numpy`, `gym`, `tensorflow`, `keras`, `matplotlib`, `pygame` , `pytorch`

Install the required libraries using:
```bash
pip install numpy gym tensorflow keras matplotlib pygame pytorch
```

## Methodology

### Algorithm Selection

We initially used a standard Deep Q-Network (DQN) but quickly realized its limitations in the complex Tetris environment. Subsequently, we transitioned to a Double DQN (DDQN) and incorporated a prioritized replay buffer to improve learning stability and efficiency.

### Model Architecture

Our model architecture consists of:
- Two convolutional layers for feature extraction.
- A linear classifier to predict action values.
- An output layer with softmax activation to represent action probabilities.

### Experiment Overview

#### Challenges Faced
- **Delayed Rewards**: Tetris provides sparse rewards, complicating the learning process.
- **State Space Size**: The large number of block types and configurations made exploration challenging.

#### Levels of Implementation
1. **Level 1**: Initial environment with negative rewards for each time step. Resulted in poor agent performance.
2. **Level 2**: Removed negative rewards; introduced positive rewards for survival. This led to suboptimal exploration and convergence.
3. **Level 3**: Introduced a two-part reward system differentiating rewards before and after landing tetrominoes to enhance learning.

### Reward Structure
1. **Reward After Landing**:
   - Game Over: -30 if a block hits the top.
   - Score: +100 for each line cleared.
   - Joints: Positive rewards for blocks joined horizontally.
2. **Reward Before Landing**: Introduced a reward based on empty spaces, encouraging faster decision-making.

## Results

During training, we monitored the agent's performance through metrics like average score and number of lines cleared. The agent demonstrated improvement, especially after refining the reward structure and implementing advanced DQN techniques.

### Visualizations

We utilized Matplotlib for visualizing the learning progress, convergence rates, and performance metrics.
