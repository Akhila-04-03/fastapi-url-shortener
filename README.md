# fastapi-url-shortener
shorten any large url
# 🔗 FastAPI URL Shortener

A simple and efficient URL shortener built with FastAPI. Users can submit long URLs and receive short, redirectable links. Deployed publicly on Render for easy access and demonstration.

## 🚀 Live Demo

Access the app here: [https://fastapi-url-shortener-3.onrender.com](https://fastapi-url-shortener-3.onrender.com)

## 📸 Screenshots

<img width="684" height="280" alt="image" src="https://github.com/user-attachments/assets/a573343c-3576-4694-b005-e55a01c72b89" />


## 🛠 Features

- Submit long URLs via HTML form
- Generate short, unique slugs
- Redirect users from short URL to original URL
- Clean frontend using Jinja2 templates
- Public deployment for easy testing

## 🧰 Tech Stack

- **Backend**: FastAPI
- **Frontend**: HTML + Jinja2
- **Deployment**: Render
- **Version Control**: Git + GitHub


## ⚙️ Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/your-username/fastapi-url-shortener.git
cd fastapi-url-shortener


pip install -r requirements.txt

uvicorn main:app --reload'''

```bash
##
🌐 Deployment (Render)
Render Settings:
- Build Command: pip install -r requirements.txt
- Start Command: uvicorn main:app --host 0.0.0.0 --port 10000
- Environment: Python 3.11+

