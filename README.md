# Sentiment Analysis Web Application

A full-stack Machine Learning web application that predicts the sentiment (Positive/Negative) of user-provided text in real-time. This project demonstrates the complete ML pipeline from model training to deployment on the web.

---

## Project Overview

This application allows users to input text (such as a movie review) and receive an instant sentiment prediction.

### Key Features

* Real-time sentiment prediction
* Simple and functional web interface
* REST API integration using Flask
* Deployed and accessible via browser

---

## Machine Learning Details

* Dataset: IMDb 50K Movie Reviews

* Text Processing: TF-IDF Vectorization

* Models Compared:

  * Logistic Regression
  * Naive Bayes
  * Support Vector Machine (SVM)

* Final Model: SVM (selected based on highest accuracy)

---

## Tech Stack

### Backend

* Python
* Flask

### Frontend

* HTML
* CSS
* JavaScript (Fetch API)

### Machine Learning

* scikit-learn
* pandas
* numpy

### Deployment

* Render

---

## Project Structure

```text
sentiment-capstone/
│
├── app.py
├── model.pkl
├── vectorizer.pkl
├── requirements.txt
│
└── templates/
    └── index.html
```

---

## How It Works

1. The user enters text in the web interface.
2. The frontend sends the input to the backend using the Fetch API.
3. The backend processes the text using a TF-IDF vectorizer.
4. The trained machine learning model predicts the sentiment.
5. The result is returned and displayed on the webpage.

---

## Model Training

* Data was preprocessed and split into training and testing sets.
* TF-IDF was used to convert text into numerical features.
* Multiple models were trained and evaluated.
* The best-performing model was selected and saved using pickle.

---

## Running Locally

1. Clone the repository
2. Create a virtual environment
3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the application:

```bash
python app.py
```

5. Open in a browser:

```text
http://127.0.0.1:5000
```

---

## Deployment

The application is deployed on Render and accessible through a public URL.

---

## Notes

* Ensure that the scikit-learn version matches between training and deployment.
* Do not upload the `venv/` folder (use a `.gitignore` file).

---

## Learning Outcomes

* Built and evaluated multiple machine learning models
* Applied TF-IDF for text vectorization
* Developed a backend API using Flask
* Connected frontend and backend using Fetch API
* Deployed a full-stack ML application

---

## Future Improvements

* Add prediction confidence score
* Improve UI/UX design
* Extend to multi-class sentiment classification
* Explore deep learning approaches (LSTM, BERT)

---

## Author

Shraddha

---

## License

This project is for academic and educational purposes.
