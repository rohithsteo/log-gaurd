# log-sentinel
Real-time log anomaly detection using machine learning
# 🚨 LogSentinel: Real-Time Log Anomaly Detection

A real-time log monitoring system that uses machine learning to detect anomalies in application logs.

---

## 🧠 Overview

LogSentinel continuously monitors a log file, stores logs in a database, and uses an unsupervised machine learning model to detect unusual patterns or anomalies.

This project simulates real-world backend monitoring systems used in production environments.

---

## ⚙️ Features

- Real-time log monitoring
- SQLite database storage
- Machine Learning using Isolation Forest
- Automatic anomaly detection
- Log simulation using generator script

---

## 🛠️ Tech Stack

- Python
- Scikit-learn
- NumPy
- SQLite

---

## 📂 Project Structure

your_file.py        # Main anomaly detection system  
log_generator.py    # Generates sample logs  
app.log             # Log file (input)  
logs.db             # Database (auto-created)  

---

## 🚀 How to Run

1. Install dependencies  
pip install -r requirements.txt  

2. Generate logs  
python log_generator.py  

3. Run the system  
python your_file.py  

---

## 🧠 How Machine Learning is Used

The system uses an Isolation Forest algorithm, an unsupervised learning model, to identify anomalies.

Steps:
1. Convert log messages into numerical features  
2. Train the model on normal patterns  
3. Detect deviations as anomalies  

---

## 🎯 Example Output

Monitoring logs... Press Ctrl+C to stop  

🚨 Anomalies Detected:  
(12, '2026-04-03 10:05:01', 'ERROR', 'Server overload detected')  

---

## 📌 Future Improvements

- Add real-time dashboard (Streamlit/Flask)  
- Use NLP techniques (TF-IDF or embeddings)  
- Email or Telegram alerts  
- Docker deployment  

---

## 👨‍💻 Author

Rohith Raj  

---

## ⭐ If you like this project, consider starring the repo!
