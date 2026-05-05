# 🚀 my-cicd-app — CI/CD Pipeline with GitHub Actions

[![CI/CD Pipeline](https://github.com/SubratGupta0506/my-cicd-app/actions/workflows/main.yml/badge.svg)](https://github.com/SubratGupta0506/my-cicd-app/actions)
[![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python&logoColor=white)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-2.x-black?logo=flask)](https://flask.palletsprojects.com)
[![Railway](https://img.shields.io/badge/Deployed%20on-Railway-blueviolet?logo=railway)](https://railway.app)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> A Flask web application demonstrating a **complete CI/CD pipeline** using **GitHub Actions** — automatically runs tests and deploys to **Railway** on every push to `main`.

---

## 📌 What This Project Demonstrates

This project is a hands-on implementation of a real-world **CI/CD (Continuous Integration & Continuous Deployment)** workflow:

| Stage | Tool | What Happens |
|-------|------|-------------|
| **Source Control** | GitHub | Code is pushed to `main` branch |
| **Continuous Integration** | GitHub Actions | Automated tests run on every push |
| **Testing** | pytest | Unit tests validate app behaviour |
| **Continuous Deployment** | Railway | App auto-deploys if all tests pass |

---

## 🏗️ Project Structure

```
my-cicd-app/
├── .github/
│   └── workflows/
│       └── main.yml        ← GitHub Actions CI/CD pipeline definition
├── __pycache__/
├── app.py                  ← Flask web application
├── test_app.py             ← Automated unit tests (pytest)
├── requirements.txt        ← Python dependencies
├── Procfile                ← Railway/Gunicorn startup command
├── railway.json            ← Railway deployment configuration
└── .gitignore
```

---

## ⚙️ CI/CD Pipeline Explained

### `.github/workflows/main.yml`
This is the heart of the project — the pipeline definition that GitHub Actions reads automatically.

**Pipeline Stages:**

```
Push to main
    │
    ▼
┌─────────────────────────────────┐
│  GitHub Actions Runner (Ubuntu) │
│  1. Checkout code               │
│  2. Setup Python                │
│  3. Install dependencies        │
│  4. Run pytest tests            │
└─────────────┬───────────────────┘
              │
      Tests Pass?
         │         │
        YES        NO
         │         │
         ▼         ▼
    Deploy to   Pipeline
     Railway     Fails ❌
       ✅
```

---

## 🛠️ Tech Stack

| Technology | Purpose |
|-----------|---------|
| **Python** | Core language |
| **Flask** | Lightweight web framework |
| **pytest** | Automated unit testing |
| **GitHub Actions** | CI/CD pipeline automation |
| **Railway** | Cloud deployment platform |
| **Gunicorn** | Production WSGI server |

---

## 🚀 Getting Started

### Prerequisites
- Python 3.9+
- Git

### Run Locally

```bash
# 1. Clone the repository
git clone https://github.com/SubratGupta0506/my-cicd-app.git
cd my-cicd-app

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the Flask app
python app.py
```

App will be live at: `http://127.0.0.1:5000`

### Run Tests

```bash
pytest test_app.py -v
```

---

## 🔄 How the CI/CD Pipeline Works

### Step 1 — Push Code
```bash
git add .
git commit -m "Your changes"
git push origin main
```

### Step 2 — GitHub Actions Triggers Automatically
- Go to the **Actions** tab in your repo to watch the pipeline run live
- It installs dependencies and runs all pytest tests

### Step 3 — Auto Deploy
- If all tests **pass** ✅ → Railway automatically deploys the new version
- If any test **fails** ❌ → Deployment is blocked, old version stays live

---

## 📋 Key Concepts Learned

- **CI (Continuous Integration):** Every code push automatically runs tests — catching bugs early before deployment
- **CD (Continuous Deployment):** Passing code is automatically deployed without manual steps
- **Pipeline as Code:** The entire pipeline is defined in a YAML file inside the repo — version-controlled and reproducible
- **Test-Gated Deployment:** Production is only updated when tests pass — preventing broken code from going live

---

## 🌐 Deployment

This app is deployed on **Railway** using:
- `Procfile` — tells Railway to use `gunicorn` as the production server
- `railway.json` — Railway-specific build and deploy configuration

---

## 📈 Why CI/CD Matters

> *"Without CI/CD, deployment is a manual, error-prone process. With CI/CD, every commit is a potential release."*

| Without CI/CD | With CI/CD |
|--------------|-----------|
| Manual testing | Automated on every push |
| Manual deployment | Auto-deploy on test pass |
| Bugs discovered in production | Bugs caught before deployment |
| Slow release cycles | Rapid, confident releases |

---

## 🔗 Connect

- **GitHub:** [SubratGupta0506](https://github.com/SubratGupta0506)
- **LinkedIn:** [linkedin.com/in/your-profile](https://linkedin.com/in/your-profile)

---

## 📄 License

This project is open source under the [MIT License](LICENSE).

---

> ⭐ If this helped you understand CI/CD, give it a star!
