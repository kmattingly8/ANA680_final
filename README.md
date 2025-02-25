# Flight Price Prediction Model

## Overview

This project involves the creation of a machine learning model that predicts flight prices based on input features such as **class**, **airline**, **duration**, and **number of stops**. The project covers the full development lifecycle from data exploration and preprocessing to deployment in various environments such as **Flask**, **Docker**, **Heroku**, **AWS SageMaker**, and **Kubernetes**.

## Problem Statement

In the airline industry, understanding and predicting flight prices can be a challenging task, as prices fluctuate depending on multiple factors. This project aims to build a machine learning model that predicts flight prices based on key input features.

### Why Machine Learning?
Machine learning is a great tool to predict flight prices because it can handle large datasets with multiple variables and uncover hidden relationships between features. By using machine learning, we can develop a model that predicts flight prices accurately and at scale, assisting both consumers and airlines in better understanding flight pricing patterns.

## Dataset

The dataset used for this project is a **flight price prediction** dataset available on Kaggle. The dataset can be accessed here:
[Flight Price Prediction 2025 Regression](https://www.kaggle.com/code/didanfariz/flight-price-prediction-2025-regression)

The dataset contains several features that are used to predict the price of flights, including:
- **Class** (Economy, Business, First Class)
- **Airline** (Carrier of the flight)
- **Duration** (Time taken for the flight)
- **Number of Stops** (Direct, 1 stop, or more)

## Steps Taken in This Project

### 1. **Data Exploration and Cleaning**
- Performed initial data exploration to understand the structure and distribution of the dataset.
- Cleaned the data by handling missing values, encoding categorical variables, and normalizing numerical features.

### 2. **Feature Engineering and Selection**
- Created new features from the existing data, including encoding categorical columns such as airline and class.
- Selected the most important features based on domain knowledge and feature importance techniques.

### 3. **Data Splitting and Model Training**
- Split the data into training, validation, and testing datasets.
- Chose **linear regression** as the algorithm for training the model, as it works well for regression tasks like predicting continuous values.
- Trained the model using the **sklearn** library and saved the trained model using **joblib**.

### 4. **Deploying the Model Locally with Flask**
- Created a Flask application that exposes the trained model as a web API.
- The API allows users to make POST requests with flight features and receive predicted flight prices.

### 5. **Containerizing the Model with Docker**
- Dockerized the Flask application so it could be easily deployed in any environment.
- Pushed the Docker image to **Docker Hub** for distribution and deployment.

### 6. **CI/CD Pipeline and Heroku Deployment**
- Implemented a CI/CD pipeline using GitHub Actions to automate testing and deployment.
- Deployed the Flask application with the trained model on **Heroku** for easy access over the internet.

### 7. **Recreating the Project in AWS SageMaker Studio Lab**
- Replicated the entire project using **AWS SageMaker Studio Lab**.
- Used **containers** to deploy the model within the AWS ecosystem.

### 8. **Kubernetes Deployment**
- Created a Kubernetes configuration file to deploy the model on a Kubernetes cluster.
- Deployed the model to a Kubernetes cluster and exposed it to the web using a service.

### 9. **Demonstration**
- Scheduled a demonstration with the instructor via Zoom to showcase the working of the project, including the CI/CD pipeline, Docker containerization, and deployment.

## Key Technologies Used

- **Machine Learning**: Scikit-learn, Pandas, NumPy
- **Flask**: For creating the REST API for model inference
- **Docker**: For containerizing the Flask application
- **Heroku**: For cloud-based deployment
- **AWS SageMaker**: For running the project in the cloud with containers
- **Kubernetes**: For container orchestration and deployment

## Files Included

- **flight_price_model.pkl**: The trained machine learning model in pickle format.
- **app.py**: The Flask application that serves the model.
- **Dockerfile**: The Dockerfile to build the container for the application.
- **deployment.yaml**: The Kubernetes configuration file to deploy the model.
- **requirements.txt**: Python dependencies for the project.
- **GitHub Actions configuration**: CI/CD pipeline configuration for automated testing and deployment.

## Conclusion

This project demonstrates how to take a machine learning model from development to production using a range of technologies including Flask, Docker, AWS, and Kubernetes. The final product is a scalable, containerized web service that predicts flight prices based on user input.
