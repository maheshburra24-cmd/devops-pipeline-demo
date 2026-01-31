# 🚀 DevOps Pipeline Demo – Flask CI/CD with Jenkins

## 📌 Project Overview
This project demonstrates a complete **CI/CD pipeline using Jenkins** for a **Flask-based web application**.  
Whenever code changes are pushed to GitHub, Jenkins automatically deploys the updated application and records deployment metadata, making the pipeline activity visible from the UI itself.

---

## 🛠️ Tech Stack
- Python (Flask)
- Git & GitHub
- Jenkins
- Linux
- Shell Scripting
- Oracle Cloud Infrastructure (OCI)

---

## ⚙️ CI/CD Workflow
1. Developer pushes code to GitHub
2. Jenkins pipeline is triggered
3. Dependencies are installed from `requirements.txt`
4. Application is deployed to OCI compute instance
5. Deployment details are updated in data files
6. Web UI reflects latest pipeline activity

---

## 📂 Project Structure

devops-pipeline-demo/
│
├── app.py # Flask application
├── Jenkinsfile # CI/CD pipeline definition
├── requirements.txt # Python dependencies
│
├── data/ # Data updated by CI/CD pipeline
│ ├── price.txt # Current product price
│ ├── deploy_info.txt # Deployment metadata
│ └── change_log.txt # Change history
│
├── templates/ # Flask HTML templates
│ ├── base.html # Common layout
│ ├── product.html # Product price view
│ └── pipeline.html # CI/CD activity view
│
├── static/ # Frontend assets
│ ├── css/
│ │ └── style.css
│ └── images/
│ └── product.png
│
└── README.md


---

## 🔄 Jenkins Pipeline Stages
- Source code checkout
- Install Python dependencies
- Update application data
- Deploy Flask application
- Log deployment details

---

## 🚀 How to Run the Project

### Clone Repository
```bash
git clone https://github.com/your-username/devops-pipeline-demo.git
cd devops-pipeline-demo
