# Iris Data Classifier

This project uses containerized flask api that classifies the flowers of iris dataset using sklearn's RandomForest Classifier.

##  Features

- Trains a RandomForest Classifier
- Saves the model with joblib
- Provides an endpoint localhost/predict for prediction
- Runs locally through docker

## Technologies used

- Python
- Docker
- Flask
- Joblib
- Sklearn

## Request format

Send json request with "data" variable.
```json
{
    data : [2.4,  3.6, 1.9, 4.1]
}
```

## Results

Accuracy of 0.99, since dataset is small.

## Setup project 

- Import in your directory.
- Create virtual environment (recommended)
- Run this command `pip install -r requirements.txt`

## License

MIT License
