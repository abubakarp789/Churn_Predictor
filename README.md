# Churn Prediction

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.11+-blue.svg)
![Flask](https://img.shields.io/badge/flask-3.0+-blue.svg)

## Table of Contents

- [Introduction](#introduction)
- [Project Overview](#project-overview)
- [Project Structure](#project-structure)
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

## Project Structure

```
├── .gitattributes
├── .gitignore
├── app.py
├── Churn_Prediction.ipynb
├── CONTRIBUTING.md
├── LICENSE
├── Procfile
├── random_forest_model.pkl
├── README.md
├── requirements.txt
├── utils.py
├── __pycache__
├── dataset
│   ├── test.csv
│   └── train.csv
├── static
│   ├── style.css
│   └── plots
│       ├── categorical_features_distribution.png
│       ├── cleaned_transaction_value_boxplot.png
│       ├── correlation_heatmap.png
│       ├── feature_importances.png
│       ├── feedback_countplot.png
│       ├── numeric_features_distribution.png
│       └── numerical_features_pairplot.png
├── templates
│   ├── analysis.html
│   ├── base.html
│   ├── index.html
│   └── prediction.html
└── venv
    ├── Include
    ├── Lib
    ├── Scripts
    └── share
```

## Technologies

- **Language:** Python 3.11
- **Libraries:**
    - Flask==3.0.0
    - pandas==2.2.2
    - numpy==1.26.4
    - scikit-learn==1.4.1.post1
    - matplotlib==3.8.3
    - seaborn==0.13.2
    - Jinja2==3.1.3
    - gunicorn==21.2.0

## Contributors ✨

Thanks to these amazing people for contributing to this repository:

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->

<!-- prettier-ignore-start -->

<!-- markdownlint-disable -->

<table>
  <tbody>
    <tr>
       <td align="center" valign="top" width="14.28%"><a href="https://github.com/alienx5499"><img src="https://avatars.githubusercontent.com/u/163229512?v=4" width="100px;" alt="Prabal Patra"/><br /><sub><b>Prabal Patra</b></sub></a><br /><a href="https://github.com/alienx5499" title="Code"></a></td>
       <td align="center" valign="top" width="14.28%"><a href="https://github.com/Nazim9945"><img src="https://avatars.githubusercontent.com/u/127049743?v=4" width="100px;" alt="Nazim Saifi"/><br /><sub><b>Nazim Saifi</b></sub></a><br /><a href="https://github.com/Nazim9945" title="Code"></a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/bala51214"><img src="https://avatars.githubusercontent.com/u/140279813?v=4" width="100px;" alt="Muhammad Bilal"/><br /><sub><b>Muhammad Bilal</b></sub></a><br /><a href="https://github.com/bala51214" title="Code"></a></td>
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
   git clone https://github.com/abubakarp789/Churn_Prediction.git
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

## Usage

### Running the Flask App

1. **Start the App:**

   ```bash
   python app.py
   ```
2. **Access the Application:**

   Open [http://127.0.0.1:5000/](http://127.0.0.1:5000/) in your browser.

### Using the Web Interface

1.  Navigate to the **Prediction** page.
2.  Fill in the form with the customer's details.
3.  Click on the **Predict Churn** button to get the prediction.

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