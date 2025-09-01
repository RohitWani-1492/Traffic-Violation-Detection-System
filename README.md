# SafeRide: Automatic Detection of Traffic Violations using YOLOv11-Based Object Detection

## INTRODUCTION

### Motivation 
- Road safety violations like riding without helmets or triple-seat riding are major contributors to traffic accidents.
- Manual enforcement is often ineffective due to limited manpower and high traffic density.
- Technological advancements in AI and object detection offer opportunities for automated monitoring.
- Automation can reduce human error, ensure consistent rule enforcement, and improve response time.
- Developing a smart system can assist authorities in promoting road safety and reducing accident rates.

### Problem Statement
- Manual traffic monitoring struggles to detect frequent violations such as non-helmet usage and triple-seat riding.
- Many offenders go unnoticed, especially in busy zones with limited enforcement coverage.
- There is a need for a reliable, real-time system to track and report violations automatically.
- Lack of timely action often leads to preventable accidents and fatalities.
- An efficient detection and alert system is essential to support law enforcement and enhance road safety.

### SCOPE AND OBJECTIVES
- Detect two-wheelers violating traffic rules in real-time. 
- Recognize absence of helmets and triple riding. 
- Extract vehicle number plate data for offender identification. 
- Build an end-to-end pipeline using deep learning models.

## REQUIREMENTS

### Functional Requirements
- Traffic Violation Detection
- Real-Time Proccessing
- Violation Recording
- Notification System

### Non-Functional Requirements
- Performance
- Scalability
- Usability

### Tools and Technologies Used
- LabelImg
- Kaggle
- Pycharm

## METHODOLOGY 

### DATASET 

#### 🪑 Triple Seat Data

| Dataset          | Source    | Size  |
|------------------|-----------|-------|
| Traffic Violation | Roboflow | 454   |
| Triple Ride       | Roboflow | 3,000 |
| Google Images     | Google   | 300   |

#### 🪖 Helmet Data

| Dataset                              | Source    | Size   |
|--------------------------------------|-----------|--------|
| helmet-2                             | Roboflow  | 3,774  |
| helmet-1                             | Roboflow  | 2,420  |
| Helmet Detection-I                   | Roboflow  | 523    |
| Helmet Dataset-I                     | Roboflow  | 523    |
| helmet-detection-20241117            | Roboflow  | 4,110  |
| Helmet Wearing Image Dataset: 13th reference | Mendeley Data | 13,780 |

#### 🔢 Number Plate Data

| Dataset                       | Source   | Size   |
|-------------------------------|----------|--------|
| License-Plate-Detection-2     | Roboflow | 2,460  |
| ANPR_PROJECT                  | Roboflow | 8,270  |
| Vehicle-Registration-Plates-2 | Roboflow | 21,175 |


