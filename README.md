# Customer Churn Predictor

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/flask-2.0+-blue.svg)

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)
- [Contact](#contact)

---

## Overview

**Customer Churn Predictor** is a professional machine learning web application developed as part of the "100 Days of Bytewise" Fellowship at Bytewise Limited. The app predicts customer churn using a trained Random Forest model and provides interactive data analysis dashboards. The project demonstrates the full ML pipeline: data processing, feature engineering, model training, evaluation, and deployment.

---

## Features

- **Interactive Web App:** User-friendly Flask interface for churn prediction and data exploration.
- **Pre-filled Sample Form:** See a sample prediction instantly, or enter your own data.
- **Modern UI:** Responsive, Bootstrap 5-based design with professional theming.
- **Data Analysis Dashboard:** Visualize feature importances, distributions, correlations, and more.
- **Reproducible ML Pipeline:** Clean code for data processing, feature engineering, and model training.
- **Experiment Tracking:** Modular code for easy experimentation and reproducibility.

---

## Technologies Used

- **Python 3.8+**
- **Flask** (Web framework)
- **scikit-learn** (ML modeling)
- **pandas, numpy** (Data processing)
- **matplotlib, seaborn** (Visualization)
- **Bootstrap 5** (Frontend styling)
- **Jinja2** (Flask templating)
- **pickle** (Model serialization)

---

## Installation

### Prerequisites

- Python 3.8+
- pip

### Steps

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/abubakarp789/Churn_Predictor.git

   cd Churn_Predictor
   ```

2. **Create and Activate a Virtual Environment:**
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

4. **Prepare Data and Model:**
   - Place your dataset files (e.g., `train.csv`, `test.csv`) in the `dataset/` folder.
   - Ensure `random_forest_model.pkl` is present in the project root (or retrain using the notebook).

---

## Usage

### Running the Flask App

1. **Start the App:**
   ```bash
   python app.py
   ```

2. **Access the Application:**
   Open [http://127.0.0.1:10000/](http://127.0.0.1:10000/) in your browser.

### Web Application Pages

- **Home:** Project overview and navigation.
- **Predict:** Fill (or sample) form to get churn prediction.
- **Analysis:** Interactive dashboard with data visualizations.

### API Usage

Send a POST request to `/prediction` with the required fields to get a churn prediction (see form fields in `prediction.html`).

---

## Project Organization

- **Data:** All raw and processed data in `dataset/`.
- **Preprocessing & Feature Engineering:** In Jupyter notebooks and modular Python scripts.
- **Model Training:** Notebooks and scripts, with model saved as `random_forest_model.pkl`.
- **Web App:** Flask app in `app.py`, templates in `templates/`, static plots in `plots/`.
- **Experiment Tracking:** Use notebooks and version control for reproducibility.

---

## Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Acknowledgements

- Developed as part of the **100 Days of Bytewise** Machine Learning Fellowship at Bytewise Limited.
- Thank you to Bytewise Limited for this fantastic opportunity. Special thanks to our track Lead **Nimra Waqar** and colleagues for their unwavering support.

---
## Contact

For questions, suggestions, or collaboration opportunities, feel free to reach out:

- **Email:** abubakarp789@gmail.com
- **GitHub:** [abubakarp789](https://github.com/abubakarp789)
- **LinkedIn:** [Abu Bakar](https://www.linkedin.com/in/abubakar56/)
- **Medium:** [@abubakarp789](https://medium.com/@abubakarp789)

I'm always open to discussing machine learning, data science, and potential collaborations!

---

**Developed by Abu Bakar during 100 Days of Bytewise Fellowship**

---


