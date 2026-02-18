# 🌡️ Temperature Converter (Celsius → Fahrenheit)

A simple full-stack project that converts Celsius to Fahrenheit using:

- 🐍 Python (HTTP server)
- 🌐 HTML
- 🎨 CSS
- ⚡ JavaScript (Fetch API)

This project demonstrates basic backend–frontend communication using a Python HTTP server and a web interface with AI GENERATIVE (COPILOT).

---

## 🚀 Features

- Convert Celsius to Fahrenheit
- Simple and clean UI
- JSON communication between frontend and backend
- CORS enabled for local development

---

## 🛠️ Technologies Used

- Python 3
- http.server (built-in Python module)
- HTML5
- CSS3
- JavaScript (Fetch API)

---



## 📂 Project Structure


project-folder/
│
├── server.py # Python backend server
├── index.html # Frontend HTML
├── style.css # Styling
└── script.js # Frontend logic (fetch request)



---

## ▶️ How to Run the Project

### 1️⃣ Start the Python Server

Make sure you have Python installed.

Run:

```bash
python app.py


You should see:

Servidor Python corriendo en http://localhost:8000


2️⃣ Open the Frontend

Open index.html in your browser.

Enter a Celsius value and click Convert.

How It Works

The user enters a Celsius value.

JavaScript sends a POST request to:

http://localhost:8000


The Python server:

Receives the JSON

Converts Celsius → Fahrenheit

Returns the result as JSON

The browser displays the converted value.


Example Request
Request (JSON)
{
  "celsius": 25
}

Response (JSON)
{
  "fahrenheit": 77.0
}

Learning Purpose

This project is ideal for beginners who want to understand:

How HTTP servers work in Python

How to handle POST requests

How frontend and backend communicate

Basic CORS handling


Author

Maycol Michel Mohr and AI Generative with Prompt Engineering (COPILOT).
