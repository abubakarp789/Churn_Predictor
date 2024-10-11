# Churn Prediction

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/flask-2.0+-blue.svg)

## Table of Contents

- [Introduction](#introduction)
- [Project Overview](#project-overview)
- [Technologies](#technologies)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

**Customer churn** is when customers stop using a company's services. Predicting churn helps businesses retain customers by identifying at-risk individuals and addressing their concerns.

## Project Overview

The **Churn Prediction** project utilizes machine learning to forecast customer churn based on historical data. It includes data preprocessing, exploratory analysis, feature engineering, model training, and deployment through a Flask web application.

### Features

- **Data Cleaning:** Handles missing values and encodes categorical variables.
- **Exploratory Data Analysis:** Visualizes data distributions and correlations.
- **Model Training:** Implements Decision Tree, Random Forest, and ANN models.
- **Deployment:** Provides a Flask web app for real-time predictions.

## Technologies

- **Language:** Python 3.8+
- **Libraries:** pandas, numpy, matplotlib, seaborn, scikit-learn, torch, Flask, pickle

## Contributors ✨

Thanks to these amazing people for contributing to this repository:

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tbody>
    <tr>
       <td align="center" valign="top" width="14.28%"><a href="https://github.com/alienx5499"><img src="#" width="100px;" alt="Prabal Patra"/><br /><sub><b>Prabal Patra</b></sub></a><br /><a href="https://github.com/alienx5499" title="Code"></a></td>
       <td align="center" valign="top" width="14.28%"><a href="https://github.com/Nazim9945"><img src="#" width="100px;" alt="Nazim Saifi"/><br /><sub><b>Nazim Saifi</b></sub></a><br /><a href="https://github.com/Nazim9945" title="Code"></a></td>
    </tr>
  </tbody>
</table>

## Installation

### Prerequisites

- Python 3.8+
- pip

### Steps

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/Churn_Prediction.git
   cd Churn_Prediction
   ```

2. **Create and Activate Virtual Environment:**

   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS/Linux
   source venv/bin/activate
   ```

3. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Prepare Dataset:**

   Place `train.csv` and `test.csv` in the `dataset/` folder.

5. **Train Models (Optional):**

   Run the notebook in `notebooks/Churn_Prediction.ipynb` to train and save models.

## Usage

### Running the Flask App

1. **Navigate to App Directory:**

   ```bash
   cd app
   ```

2. **Ensure Model is Present:**

   Verify `models/random_forest_model.pkl` exists.

3. **Start the App:**

   ```bash
   python app.py
   ```

4. **Access the Application:**

   Open [http://127.0.0.1:5000/](http://127.0.0.1:5000/) in your browser.

### Using the API

Send a POST request to `http://127.0.0.1:5000/predict` with the required data to receive churn predictions.

## Contributing

Contributions are welcome! Follow these steps:

1. **Fork the Repository**
2. **Clone Your Fork:**

   ```bash
   git clone https://github.com/yourusername/Churn_Prediction.git
   cd Churn_Prediction
   ```

3. **Create a Branch:**

   ```bash
   git checkout -b feature/YourFeature
   ```

4. **Commit Changes:**

   ```bash
   git commit -m "Description of your feature"
   ```

5. **Push and Create Pull Request:**

   ```bash
   git push origin feature/YourFeature
   ```

## License

This project is licensed under the [MIT License](LICENSE).