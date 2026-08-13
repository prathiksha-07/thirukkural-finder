# Thirukkural Finder

## 📖 Project Description

Thirukkural Finder is a simple and mobile-responsive web application developed using Flask.

The application allows users to enter a Thirukkural number and view the corresponding Thirukkural along with its meaning.

The project does not use a database. Instead, it fetches the required Thirukkural details from a free API.

For example, when the user enters **52**, the application fetches and displays Thirukkural number 52 and its meanings.

## 🎯 Objectives

- To develop a simple Thirukkural searching application.
- To use Flask for the backend.
- To fetch Thirukkural details using a free API.
- To display the Kural and its meanings clearly.
- To create a mobile-responsive user interface.
- To develop the application without using a database.

## ✨ Features

- Search Thirukkural by number.
- Supports Kural numbers from 1 to 1330.
- Displays the Tamil Thirukkural.
- Displays Tamil meaning.
- Displays English meaning.
- Mobile-responsive user interface.
- No database required.
- Data is fetched dynamically from the API.

## 🛠️ Technologies Used

- Python
- Flask
- HTML
- CSS
- REST API
- Requests

## 🔄 How the Application Works

```text
User enters Kural Number
        ↓
Flask receives the number
        ↓
Flask sends a request to the Thirukkural API
        ↓
API returns the Kural details
        ↓
Flask processes the API response
        ↓
The webpage displays the Kural and meanings
```

## 📂 Project Structure

```text
thirukkural_app/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css
```

## 🚀 How to Run the Project

### Step 1: Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### Step 2: Open the Project Folder

```bash
cd thirukkural_app
```

### Step 3: Install the Required Packages

```bash
pip install -r requirements.txt
```

### Step 4: Run the Flask Application

```bash
python app.py
```

### Step 5: Open the Application

Open the following address in your browser:

```text
http://127.0.0.1:5000
```

## 🔗 API

The application uses a free Thirukkural API to retrieve Kural details based on the number entered by the user.

No local database is required because the data is obtained directly from the API.

## 📱 Responsive Design

The user interface is designed to work on:

- Desktop
- Laptop
- Tablet
- Mobile phones

## 📝 Example

If the user enters:

```text
52
```

the application fetches the corresponding Thirukkural and displays:

- Kural number
- Tamil Kural
- Tamil meaning
- English meaning

## 👩‍💻 Project

**Thirukkural Finder**

Developed using **Python, Flask, HTML, CSS, and a free API**.
