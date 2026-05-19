# 🩺 Cloud Computing Based Health Monitoring System

An IoT-enabled smart healthcare monitoring system that measures real-time Heart Rate and SpO₂ using the MAX30100 sensor and NodeMCU ESP8266. The collected data is uploaded to Firebase Realtime Database, analyzed using a Machine Learning model, and displayed through a Flask web dashboard with health risk prediction and suggestions.

---

# 📌 Features

- Real-time Heart Rate Monitoring
- Real-time SpO₂ Monitoring
- Firebase Realtime Database Integration
- Flask-based Web Dashboard
- Machine Learning Health Risk Prediction
- Personalized Health Suggestions
- Secure Login Authentication
- IoT + Cloud + ML Integration
- Low-cost healthcare monitoring solution

---
<br>
## Frontend Screens

### Login Page

The login page allows users to securely access the health monitoring system.
<br>
<img width="746" height="335" alt="Screenshot 2026-05-19 230832" src="https://github.com/user-attachments/assets/84716173-6c44-4685-a0c3-e83f600fb228" />


### Dashboard Page

The dashboard displays real-time patient health information including heart rate, SpO₂ level, risk prediction, and personalized recommendations.
<br>
<img width="747" height="316" alt="Screenshot 2026-05-19 230840" src="https://github.com/user-attachments/assets/936ea46a-0465-4e87-9fb4-8ff15bf606ce" />



### The Model
<br>
<img width="440" height="644" alt="Screenshot 2026-05-19 230815" src="https://github.com/user-attachments/assets/942c06f2-0a9c-4390-b5ff-66a68ae6e495" />


---
<br>


# 🛠️ Tech Stack

## Hardware
- NodeMCU ESP8266
- MAX30100 Pulse Oximeter Sensor
- LCD Display (I2C)

## Software
- Python
- Flask
- Firebase Realtime Database
- Scikit-learn
- HTML
- CSS
- Arduino IDE

---

# 🧠 Machine Learning Model

The project uses a Logistic Regression model trained using:
- Heart Rate
- SpO₂ values

## Risk Categories
| Risk Level | Meaning |
|------------|---------|
| 0 | Healthy |
| 1 | Mild Risk |
| 2 | High Risk |
| 3 | Abnormal |

---

# 🏗️ System Architecture

## 1. Hardware Layer
- MAX30100 collects:
  - Heart Rate
  - SpO₂

- NodeMCU ESP8266:
  - Reads sensor data
  - Sends data to Firebase via Wi-Fi

## 2. Cloud Layer
- Firebase Realtime Database stores real-time health data.

## 3. Application Layer
- Flask Web App:
  - Fetches Firebase data
  - Applies ML prediction
  - Displays dashboard
  - Provides health suggestions

---

# ⚙️ Working Flow

1. MAX30100 sensor collects health vitals.
2. NodeMCU reads sensor data.
3. Data is sent to Firebase Realtime Database.
4. Flask app fetches real-time data.
5. ML model predicts risk level.
6. Dashboard displays:
   - Heart Rate
   - SpO₂
   - Risk Prediction
   - Health Suggestions

---

# 🔐 Login Credentials

```txt
Username: admin
Password: 1234
```

---

# 📊 Sample Dashboard Output

```txt
Heart Rate: 78 bpm
SpO₂: 96 %
Risk Level: Mild Risk
Suggestion:
Stay hydrated, take proper sleep, and avoid stress.
```

---

# 📂 Project Structure

```bash
health-monitoring/
│
├── app.py
├── model.py
├── model.pkl
├── templates/
│   ├── login.html
│   └── dashboard.html
│
├── readings.csv
├── requirements.txt
├── Arduino_Code/
│   └── health_monitoring.ino
│
└── README.md
```

---

# 🚀 Installation & Setup

## 1️⃣ Clone Repository

```bash
git clone https://github.com/SshreyanshVITB/health-monitoring.git
cd health-monitoring
```

---

## 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 3️⃣ Configure Firebase

Add your Firebase Admin SDK JSON file:

```bash
firebase-adminsdk.json
```

Update Firebase URL in `app.py`.

---

## 4️⃣ Train ML Model

```bash
python model.py
```

This generates:

```bash
model.pkl
```

---

## 5️⃣ Run Flask App

```bash
python app.py
```

Open browser:

```bash
http://127.0.0.1:5000
```

---

# 🔌 Hardware Connections

| MAX30100 | NodeMCU ESP8266 |
|----------|----------------|
| VIN | 3.3V |
| GND | GND |
| SDA | D2 |
| SCL | D1 |

---

# 📱 Applications

- Remote Patient Monitoring
- Telemedicine
- Preventive Healthcare
- Fitness Tracking
- Rural Healthcare Monitoring

---

# 🔮 Future Scope

- ECG Sensor Integration
- Blood Pressure Monitoring
- Mobile App Development
- SMS/Email Emergency Alerts
- AI-based Personalized Healthcare
- Deep Learning Models

---

# 📚 References

1. MAX30100 Datasheet
2. Flask Documentation
3. Firebase Documentation
4. Scikit-learn Documentation
5. Research Papers on IoT Healthcare Systems

---

# 👨‍💻 Author

Shreyansh Singh

---

# ⭐ If you like this project

Give this repository a ⭐ on GitHub!
