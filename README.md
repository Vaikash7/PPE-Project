# 🦺 Vision-Based Real-Time PPE Compliance Monitoring System

> **An AI-powered computer vision system for real-time detection and monitoring of Personal Protective Equipment (PPE) compliance using YOLOv8 and OpenCV.**

<p align="center">

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge\&logo=python\&logoColor=white)
![YOLOv8](https://img.shields.io/badge/YOLOv8-Object%20Detection-00FFFF?style=for-the-badge)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-5C3EE8?style=for-the-badge\&logo=opencv\&logoColor=white)
![Deep Learning](https://img.shields.io/badge/Deep%20Learning-Computer%20Vision-orange?style=for-the-badge)

</p>

---

## 📌 Table of Contents

<details>
<summary><b>Click to expand</b></summary>

* [Overview](#-overview)
* [Research Publication](#-research-publication)
* [Problem Statement](#-problem-statement)
* [Features](#-features)
* [System Architecture](#-system-architecture)
* [Detection Workflow](#-detection-workflow)
* [Technologies Used](#-technologies-used)
* [Project Structure](#-project-structure)
* [Dataset & Training](#-dataset--training)
* [Installation](#-installation)
* [How to Run](#-how-to-run)
* [Detection Classes](#-detection-classes)
* [Alert System](#-alert-system)
* [Applications](#-applications)
* [Performance & Optimization](#-performance--optimization)
* [Screenshots & Demo](#-screenshots--demo)
* [Key Concepts](#-key-concepts)
* [What I Learned](#-what-i-learned)
* [Future Enhancements](#-future-enhancements)
* [Author](#-author)

</details>

---

# 📖 Overview

The **Vision-Based Real-Time PPE Compliance Monitoring System** is an AI-powered computer vision application designed to automatically monitor whether workers are wearing required safety equipment.

The system uses **YOLOv8 object detection** together with **OpenCV** to process live camera/video streams and identify PPE-related objects such as:

* 🪖 Helmets
* 🦺 Safety Vests
* 👤 Persons

When a potential PPE violation is detected, the system can generate an alert to draw attention to the non-compliance.

---

# 🏆 Research Publication

This project was developed as an academic research project and was **published in IEEE Xplore** and **presented at an IEEE International Conference**.

> 📄 **Research Paper:** Add your official IEEE Xplore paper link here.

```markdown
[View Research Paper] https://ieeexplore.ieee.org/document/11518365
```

---

# 🎯 Problem Statement

In industrial environments, workers are often required to wear PPE such as helmets and safety vests.

Manual monitoring can be:

* Time-consuming
* Difficult to perform continuously
* Dependent on human supervision
* Challenging in large industrial environments

This project aims to automate PPE monitoring using computer vision.

```text
Traditional Monitoring
        │
        ▼
Human Supervisor
        │
        ▼
Manual Observation
        │
        ▼
Possible Missed Violations


AI-Based Monitoring
        │
        ▼
Camera / Video Feed
        │
        ▼
YOLOv8 Detection
        │
        ▼
PPE Compliance Analysis
        │
        ▼
Automatic Alert
```

---

# 🚀 Features

### 🎯 Real-Time Detection

Detects objects from live camera or video input using YOLOv8.

### 🦺 PPE Detection

Identifies safety equipment such as:

```text
🪖 Helmet
🦺 Safety Vest
👤 Person
```

### 📹 Live Video Processing

Processes frames from:

* Webcam
* Video files
* Live video streams

### 🚨 Alert System

Generates an alert when PPE non-compliance is identified.

### ⚡ Fast Detection

YOLOv8 enables real-time object detection with efficient inference.

### 🧠 Deep Learning

Uses a trained YOLOv8 model for object detection.

---

# 🏗️ System Architecture

```text
                    ┌────────────────────┐
                    │    Camera / Video  │
                    │       Input        │
                    └──────────┬─────────┘
                               │
                               ▼
                    ┌────────────────────┐
                    │      OpenCV        │
                    │                    │
                    │ Frame Acquisition  │
                    └──────────┬─────────┘
                               │
                               ▼
                    ┌────────────────────┐
                    │      YOLOv8        │
                    │                    │
                    │ Object Detection   │
                    └──────────┬─────────┘
                               │
                               ▼
                    ┌────────────────────┐
                    │ PPE Detection      │
                    │                    │
                    │ Helmet / Vest /    │
                    │ Person             │
                    └──────────┬─────────┘
                               │
                               ▼
                    ┌────────────────────┐
                    │ Compliance Check   │
                    └──────────┬─────────┘
                               │
                     ┌─────────┴─────────┐
                     ▼                   ▼
                Compliant            Violation
                     │                   │
                     ▼                   ▼
                Continue             🚨 Alert
```

---

# 🔄 Detection Workflow

```text
Camera / Video
      │
      ▼
Read Frame
      │
      ▼
Preprocess Frame
      │
      ▼
YOLOv8 Inference
      │
      ▼
Detect Objects
      │
      ▼
Identify PPE
      │
      ▼
Check Compliance
      │
 ┌────┴─────┐
 │          │
 ▼          ▼
Safe     Violation
 │          │
 ▼          ▼
Display    Alert
```

---

# 🛠️ Technologies Used

| Technology           | Purpose                     |
| -------------------- | --------------------------- |
| 🐍 **Python**        | Application development     |
| 👁️ **OpenCV**       | Video and image processing  |
| 🎯 **YOLOv8**        | Object detection            |
| 🧠 **Deep Learning** | PPE detection model         |
| 🔊 **Audio Alert**   | Non-compliance notification |

---

# 📂 Project Structure

```text
PPE-Project/
│
├── main.py
│   └── Real-time PPE detection
│
├── train.py
│   └── YOLOv8 model training
│
├── fix_labels.py
│   └── Dataset preprocessing / label correction
│
├── requirements.txt
│   └── Python dependencies
│
├── alert.wav
│   └── PPE violation alert sound
│
├── dataset/
│   └── Training and validation data
│
├── runs/
│   └── Training and model outputs
│
├── venv/
│   └── Python virtual environment
│
└── README.md
```

---

# 🧠 Dataset & Training

The YOLOv8 model is trained using a labeled PPE dataset.

The training workflow is:

```text
Raw Dataset
     │
     ▼
Label Preparation
     │
     ▼
Label Correction
     │
     ▼
Dataset Split
     │
     ├── Training
     ├── Validation
     └── Testing
     │
     ▼
YOLOv8 Training
     │
     ▼
Trained Model
     │
     ▼
Real-Time Detection
```

The `fix_labels.py` script is used to preprocess/correct dataset labels before training.

---

# 🎓 Model Training

The model can be trained using:

```bash
python train.py
```

The training process generates model outputs under:

```text
runs/
```

The trained weights can then be used for real-time inference.

---

# ⚙️ Installation & Setup

## 1️⃣ Clone Repository

```bash
git clone https://github.com/Vaikash7/PPE-Project.git
```

Navigate to the project:

```bash
cd PPE-Project
```

---

## 2️⃣ Create Virtual Environment

### Windows

```bash
python -m venv venv
```

Activate:

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
python -m venv venv
```

Activate:

```bash
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ How to Run

## 🔹 Real-Time Detection

Start the application:

```bash
python main.py
```

The system will access the configured video source and begin detecting PPE objects.

---

## 🔹 Train the Model

To train the YOLOv8 model:

```bash
python train.py
```

---

## 🔹 Dataset Label Processing

If dataset labels require preprocessing:

```bash
python fix_labels.py
```

---

# 🎯 Detection Classes

The system is designed to identify PPE-related objects.

```text
┌────────────────────────────┐
│       DETECTION CLASSES    │
├────────────────────────────┤
│ 👤 Person                  │
│ 🪖 Helmet                  │
│ 🦺 Safety Vest             │
└────────────────────────────┘
```

> Add additional classes such as **gloves** or **masks** here only if they are actually included in the trained model.

---

# 🚨 Alert System

When the system identifies a PPE violation, an audio alert can be triggered.

```text
PPE Detection
      │
      ▼
Compliance Analysis
      │
      ▼
Violation Detected
      │
      ▼
┌─────────────────┐
│   🚨 ALERT      │
│                 │
│   alert.wav     │
└─────────────────┘
```

The alert sound is stored in:

```text
alert.wav
```

---

# 📹 Input Sources

The system can be adapted to process different input sources.

### Webcam

```text
Live Camera
     ↓
OpenCV
     ↓
YOLOv8
```

### Video File

```text
Video File
     ↓
Frame Extraction
     ↓
YOLOv8
```

### Live Stream

```text
Live Stream
     ↓
Frame Processing
     ↓
YOLOv8
```

---

# 🏭 Applications

The system can be used in environments where PPE compliance is important.

### 🏗️ Construction

Monitor workers for helmets and safety vests.

### 🏭 Manufacturing

Monitor PPE compliance in industrial production areas.

### 📦 Warehouses

Monitor safety equipment in warehouse environments.

### ⚙️ Industrial Facilities

Automate safety monitoring in restricted or hazardous areas.

---

# ⚡ Performance & Optimization

The system is designed for real-time object detection.

Potential optimization techniques include:

```text
YOLOv8 Model
     │
     ├── Image Resizing
     ├── Confidence Threshold
     ├── Efficient Frame Processing
     └── Hardware Acceleration
             │
             ▼
      Faster Inference
```

Performance can depend on:

* Input resolution
* Model size
* GPU/CPU hardware
* Number of objects in a frame
* Video resolution
* Confidence threshold

---

# 📊 Detection Example

Conceptually, the output can look like:

```text
┌────────────────────────────────────────┐
│                                        │
│        👤 Worker                       │
│       ┌─────────┐                      │
│       │ 🪖      │ ← Helmet             │
│       │         │                      │
│       │  🦺     │ ← Safety Vest       │
│       │         │                      │
│       └─────────┘                      │
│                                        │
│       STATUS: ✅ COMPLIANT             │
│                                        │
└────────────────────────────────────────┘
```

For a violation:

```text
┌────────────────────────────────────────┐
│                                        │
│        👤 Worker                       │
│       ┌─────────┐                      │
│       │         │ ← No Helmet          │
│       │         │                      │
│       │  🦺     │ ← Safety Vest       │
│       └─────────┘                      │
│                                        │
│       STATUS: 🚨 VIOLATION             │
│                                        │
└────────────────────────────────────────┘
```

---

# 📸 Screenshots & Demo

Add screenshots of the actual detection output here.

Recommended structure:

```text
screenshots/
│
├── detection-compliant.png
├── detection-violation.png
├── training-results.png
└── application-output.png
```

Then add them to the README:

```markdown
## 📸 Project Demo

### ✅ PPE Compliant

![PPE Compliant](screenshots/detection-compliant.png)

### 🚨 PPE Violation

![PPE Violation](screenshots/detection-violation.png)

### 📊 Training Results

![Training Results](screenshots/training-results.png)
```

---

# 🧠 Key Concepts Demonstrated

This project demonstrates practical knowledge of:

* Computer Vision
* Object Detection
* YOLOv8
* Deep Learning
* Image Processing
* Video Processing
* OpenCV
* Dataset Preparation
* Model Training
* Model Inference
* Real-Time Detection
* PPE Compliance Monitoring
* Automated Alerting

---

# 🎓 What I Learned

Through this project, I gained hands-on experience in:

* Building real-time computer vision applications
* Preparing and preprocessing object detection datasets
* Training YOLOv8 models
* Performing real-time inference
* Processing live video using OpenCV
* Designing PPE compliance detection logic
* Implementing automated alerts
* Integrating AI into industrial safety applications

---

# 🔮 Future Enhancements

Possible improvements include:

* [ ] Add helmet, vest, glove, and mask detection
* [ ] Add person-to-PPE association
* [ ] Add multi-camera monitoring
* [ ] Add violation logging
* [ ] Add database integration
* [ ] Add dashboard for compliance statistics
* [ ] Add email/SMS notifications
* [ ] Add cloud deployment
* [ ] Add CCTV stream integration
* [ ] Add historical violation reports
* [ ] Improve model accuracy with additional training data

---

# 📈 Project Highlights

```text
┌──────────────────────────────────────────────┐
│      PPE COMPLIANCE MONITORING SYSTEM        │
├──────────────────────────────────────────────┤
│                                              │
│  ✓ YOLOv8 Object Detection                  │
│  ✓ Real-Time Video Processing               │
│  ✓ OpenCV Integration                       │
│  ✓ PPE Detection                            │
│  ✓ Automated Violation Alerts               │
│  ✓ Custom Model Training                    │
│  ✓ Dataset Preprocessing                    │
│  ✓ Industrial Safety Application             │
│  ✓ IEEE Research Publication                │
│                                              │
└──────────────────────────────────────────────┘
```

---

# 📄 Research Publication

This project was also presented as an academic research project.

**Publication:** IEEE Xplore

**Conference:** IEEE International Conference

🔗 **Paper:** Add your official IEEE Xplore URL here.

---

# 👨‍💻 Author

## Chatrathi Vaikash

**Computer Science & Engineering Graduate**

### 💻 Skills

```text
Python | Java | SQL
Computer Vision | YOLOv8 | OpenCV
Azure | Databricks | PySpark
Snowflake | Data Engineering
```

### 🔗 GitHub

[![GitHub](https://img.shields.io/badge/GitHub-Vaikash7-181717?style=for-the-badge\&logo=github)](https://github.com/Vaikash7)

---

⭐ **If you found this project useful, consider giving the repository a star!**
