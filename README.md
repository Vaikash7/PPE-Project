# 🦺 Vision-Based Real-Time PPE Compliance Monitoring System

## 📌 Overview
This project presents an AI-powered system that monitors **Personal Protective Equipment (PPE)** compliance in real-time using **Computer Vision and Deep Learning**. It detects whether workers are wearing safety gear such as helmets and vests through live video streams, helping improve industrial safety and reduce accidents.

---

## 🚀 Features
- 🎯 Real-time person detection using YOLOv8  
- 🦺 PPE detection (Helmet, Safety Vest)  
- 📹 Live camera/live feed processing  
- 🚨 Alert system for non-compliance  
- ⚡ Fast and efficient detection  

---

## 🧠 Technologies Used
- Python  
- OpenCV  
- YOLOv8 (Ultralytics)  
- Deep Learning  

---

## 📂 Project Structure
ppe-project/
│── main.py              # Real-time detection  
│── train.py             # Model training  
│── fix_labels.py        # Dataset preprocessing  
│── requirements.txt     # Dependencies  
│── alert.wav            # Alert sound  
│── runs/                # Training outputs (ignored)  
│── dataset/             # Dataset (ignored)  
│── venv/                # Virtual environment (ignored)  

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository
git clone https://github.com/Vaikash7/PPE-Project.git  
cd PPE-Project  

### 2️⃣ Create Virtual Environment
python -m venv venv  
venv\Scripts\activate  

### 3️⃣ Install Dependencies
pip install -r requirements.txt  

---

## ▶️ How to Run

### 🔹 Run Detection
python main.py  

### 🔹 Train Model
python train.py  

---

## 📊 Applications
- Construction Sites  
- Manufacturing Industries  
- Warehouses  
- Industrial Safety Monitoring  

---

## 🎯 Objective
To enhance workplace safety by automating PPE compliance monitoring and reducing manual supervision.
