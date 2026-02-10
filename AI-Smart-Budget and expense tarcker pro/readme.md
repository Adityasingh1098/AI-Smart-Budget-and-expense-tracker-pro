# 💰 AI Smart Budget & Expense Tracker

An intelligent, command-line based personal finance management system built with Python, MySQL, and OpenAI API.  
This project helps users track expenses, analyze spending patterns, and receive AI-powered financial guidance.

---

## 🚀 Features

✔ Secure OTP-based Login & Registration  
✔ Expense Tracking with Percentage Analysis  
✔ Income & Budget Management  
✔ AI-Powered Personalized Financial Strategy  
✔ MySQL Database Integration  
✔ Email Verification System  
✔ Environment-Based Security (No Hardcoded Secrets)

---

## 🛠️ Tech Stack

| Category        | Technologies Used              |
|-----------------|--------------------------------|
| Language        | Python                          |
| Database        | MySQL                           |
| AI Integration  | OpenAI API                      |
| Security        | dotenv, Environment Variables  |
| Email Service   | SMTP (Gmail)                    |

---

## 📂 Project Structure

AI-Smart-Budget-Tracker/
│
├── main.py # Main application logic
├── verification.py # Email verification module
├── AIinte.py # AI integration module
├── .env # Environment variables (ignored)
├── .gitignore
├── requirements.txt
└── README.md



---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Adityasingh1098/AI-Smart-Budget-Tracker.git
cd AI-Smart-Budget-Tracker

2️⃣ Install Dependencies

pip install -r requirements.txt

3️⃣ Configure Environment Variables
Create a .env file in the root directory:

# Database
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=AIsmartbudgetTracker
DB_PORT=3307

# Email
EMAIL_ADDRESS=your_email@gmail.com
EMAIL_PASSWORD=your_app_password

# OpenAI
OPENAI_API_KEY=your_api_key

4️⃣ Setup Database
Create required tables in MySQL:

CREATE DATABASE AIsmartbudgetTracker;
USE AIsmartbudgetTracker;

(Configure tables according to project schema)


5️⃣ Run the Application
python main.py




📊 How It Works

1️⃣ User registers and verifies email via OTP
2️⃣ User logs in securely
3️⃣ Income and financial details are collected
4️⃣ Expenses are recorded and analyzed
5️⃣ AI generates personalized financial guidance
6️⃣ Users track spending patterns over time



🤖 AI Integration

The project uses OpenAI API to:

Analyze income and expenses

Generate personalized financial strategies

Suggest savings and investment methods

This allows users to make smarter financial decisions.



🔐 Security Measures

✔ No hardcoded passwords
✔ Environment-based credentials
✔ OTP authentication
✔ Secure database queries

This follows industry-standard security practices.


📈 Future Enhancements

Web-based interface (Flask/Django)

Mobile app version

Password-based authentication

Advanced analytics dashboard

Cloud deployment

Data visualization


👨‍💻 Developer

Aditya Singh
Aspiring Software Developer & AI/ML Engineer


this project was solely build by me but it was cleaned by AI to prevent the leak of privacy to public.


⭐ Why This Project?

This project demonstrates:

✔ Backend Development Skills
✔ Database Management
✔ API Integration
✔ Secure Authentication
✔ Real-World Problem Solving
✔ Clean Code Architecture

It reflects practical experience in building production-style applications.