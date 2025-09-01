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

### Dataset

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

- For standard motorcycle usage, 8,000 images were web scraped from Google and various websites such as Pexels, Pixabay and Unsplash. After cleaning 5,542 images were obtained which were further annotated.
- For no-helmet instances, we utilized the Face-Detection-Dataset from Kaggle consisting of 13,400 images, which was already annotated in YOLO format.  After cleaning the dataset, 2,731 images were retained and was further expanded to 13,655 using data augmentation techniques

#### 🧪 Train-Test-Validation Split

| Dataset                  | Training Set | Test Set | Valid Set |
|---------------------------|--------------|----------|-----------|
| 🏍️ Motorcycle Detection   | 8,873        | 1,110    | 1,109     |
| 🪖 Helmet Detection       | 24,892       | 3,111    | 3,113     |
| 🔢 Number Plate Detection | 45,247       | 5,656    | 5,656     |

### Data Augmentation
- Original 300 triple seat images were expanded to 1,800 using flipping, rotation (±25°), and shearing (±8°) techniques.
- 50% of the images were enhanced using Gaussian blur with a sigma range of 0 to 0.5.
- Contrast (0.75x–1.5x) and lightness (0.8x–1.2x) adjustments were applied to all images.
- Color conversion techniques—color swapping, grayscale, and sepia—were used. 
- A total of 4,736 triple-seat riding images were generated, boosting dataset diversity and model robustness.
- Color conversion techniques were applied on helmet data as well as number plate data to increase the size of dataset.

## ALGORITHMS USED
<p align="center" style="display:flex; justify-content:center; gap:20px;">
  <img src="https://github.com/user-attachments/assets/5b86e7ed-e4a2-40fb-ac26-e2dbab185263" width="450" height="300" style="border:1px solid #ccc; border-radius:6px;" />
  <img src="https://github.com/user-attachments/assets/c9ed6224-5774-47ad-91d1-8b043be63a98" width="450" height="300" style="border:1px solid #ccc; border-radius:6px;" />
</p>



