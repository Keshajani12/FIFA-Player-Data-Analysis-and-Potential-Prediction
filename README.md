# FIFA Player Data Analysis and Potential Prediction

This Python script analyzes FIFA player data, focusing on player age and potential, and employs linear regression to predict potential based on age. The dataset ('fifa.csv') contains a variety of attributes for FIFA players, and this script showcases data exploration, visualization, and predictive modeling using popular Python libraries including Pandas, Seaborn, and scikit-learn.

# Table of Contents
1. Introduction
2. Installation
3. Usage
4. Data Loading and Initial Exploration
5. Data Filtering and Exploration
6. Data Visualization
7. Linear Regression 
8. Model Evaluation and Visualization
9. Screenshots

# Introduction
This script provides an illustrative example of FIFA player data analysis and predictive modeling. Depending on your specific research objectives, you may need to tailor the code and datasets to your requirements. It covers the following tasks:
● Loading data from a CSV file. 
● Data cleaning and preprocessing.
● Creating various plots using Matplotlib and Seaborn for data visualization.
● Implementing a linear regression model to predict relationship between player age and potential.


# Installation
1. Clone this repository: git clone https://github.com/Keshajani12/FIFA-Player-Data-Analysis-and-Potential-Prediction.git

2. Navigate to the project directory: cd fifa

3. Install the required Python packages using pip: pip install pandas numpy matplotlib seaborn scikit-learn

# Or
Download Zip and Install requirements.txt write command : pip install -r requirements.txt

# Usage
1. Run the Python script: python fifa.py

2. The script will load the fifa player data, perform analysis, generate plots, and display them.

# Data Loading and Initial Exploration

The FIFA player dataset is loaded into a Pandas DataFrame called 'df'.
Basic statistics and information about the dataset are displayed using head(), shape, info(), and describe().

Data Preprocessing: Unnecessary columns ('sofifa_id', 'joined', 'player_url', 'preferred_foot', 'weak_foot') are dropped from the DataFrame to streamline the analysis.

# Data Filtering and Exploration

The dataset is divided into three age groups: 'youngAge' (players aged 40 or younger), 'minor' (players under 18), and 'oldAge' (players older than 40).
Data is also filtered based on nationality for Argentina, France, Netherlands, and Germany, creating separate DataFrames.

# Data Visualization

● A count plot is created using Seaborn to visualize the distribution of player ages.
● A bar plot is generated to illustrate the relationship between age and player wages for older players.
● Players are sorted based on their shooting ability, and a bar plot displays the top 10 players with the best shooting skills.
● A line plot demonstrates the relationship between age and league rank for Dutch players.

# Linear Regression

● The dataset is split into training and testing sets using train_test_split().
● Linear regression is employed to predict 'potential' based on 'age'.
● Predictions are made on the test data, and the Mean Squared Error (MSE) is computed to evaluate model performance.

# Model Evaluation and Visualization

● The MSE between the predicted and actual 'potential' values is reported as a measure of prediction accuracy.
● A DataFrame named 'record' is constructed to store the actual and predicted 'potential' values.
● A line plot is generated using Seaborn to visualize the actual and predicted 'potential' values.

# Screenshots
![1](https://github.com/Keshajani12/FIFA-Player-Data-Analysis-and-Potential-Prediction/assets/143489586/e0df8b83-d710-4570-9d6f-b57959cd3c5e)

![2](https://github.com/Keshajani12/FIFA-Player-Data-Analysis-and-Potential-Prediction/assets/143489586/f2234b0e-4e51-4b0e-9d5d-808185d7a54f)

![3](https://github.com/Keshajani12/FIFA-Player-Data-Analysis-and-Potential-Prediction/assets/143489586/03086e56-15e9-4b5e-91f5-290d0e170539)

![4](https://github.com/Keshajani12/FIFA-Player-Data-Analysis-and-Potential-Prediction/assets/143489586/2ec64b20-8de1-4a59-8b37-b856cfdcc077)

![5](https://github.com/Keshajani12/FIFA-Player-Data-Analysis-and-Potential-Prediction/assets/143489586/6498258b-53a9-4e11-b655-d04f1c2e98fb)
