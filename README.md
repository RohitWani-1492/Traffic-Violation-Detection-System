# 🛵 SafeRide: Automatic Detection of Traffic Violations using YOLOv11-Based Object Detection  

---

## 🚀 Introduction  

### 🎯 Motivation  
- 🚦 Road safety violations like riding without helmets or triple-seat riding are **major contributors** to traffic accidents.  
- 👮 Manual enforcement is often **ineffective** due to limited manpower and high traffic density.  
- 🤖 Advances in **AI & Object Detection** enable automated monitoring for smarter traffic systems.  
- ✅ Automation reduces human error, ensures **consistent enforcement**, and improves response time.  
- 🌍 A smart system can **assist authorities** in promoting safer roads and reducing accident rates.  

### ❓ Problem Statement  
- 📸 Manual traffic monitoring struggles to detect **frequent violations** such as non-helmet usage and triple-seat riding.  
- 🚧 Offenders often go **unnoticed** in busy zones with limited coverage.  
- ⏱️ Lack of timely action → preventable accidents and fatalities.  
- ✅ A **reliable, real-time detection system** is essential to support law enforcement.  

### 🎯 Scope and Objectives  
- 🔍 Detect two-wheelers violating traffic rules in **real-time**.  
- 🪖 Identify absence of helmets & triple riding.  
- 🔢 Extract **vehicle number plates** for offender identification.  
- 🛠️ Build an **end-to-end pipeline** using deep learning models.  

---

## 🛠️ Requirements  

### 📌 Functional  
- ✅ Traffic Violation Detection  
- ⏱️ Real-Time Processing  
- 💾 Violation Recording  
- 📢 Notification System  

### ⚙️ Non-Functional  
- ⚡ Performance  
- 📈 Scalability  
- 🎨 Usability  

### 🧰 Tools & Technologies  
- 🏷️ LabelImg  
- 📊 Kaggle  
- 💻 Pycharm  

---

## 🧪 Methodology  

### 📂 Dataset  

#### 🪑 Triple Seat Data  
| Dataset           | Source    | Size  |
|-------------------|-----------|-------|
| Traffic Violation | Roboflow  | 454   |
| Triple Ride       | Roboflow  | 3,000 |
| Google Images     | Google    | 300   |

#### 🪖 Helmet Data  
| Dataset                              | Source        | Size   |
|--------------------------------------|---------------|--------|
| helmet-2                             | Roboflow      | 3,774  |
| helmet-1                             | Roboflow      | 2,420  |
| Helmet Detection-I                   | Roboflow      | 523    |
| Helmet Dataset-I                     | Roboflow      | 523    |
| helmet-detection-20241117            | Roboflow      | 4,110  |
| Helmet Wearing Image Dataset (13th)  | Mendeley Data | 13,780 |

#### 🔢 Number Plate Data  
| Dataset                       | Source   | Size   |
|-------------------------------|----------|--------|
| License-Plate-Detection-2     | Roboflow | 2,460  |
| ANPR_PROJECT                  | Roboflow | 8,270  |
| Vehicle-Registration-Plates-2 | Roboflow | 21,175 |

📌 **Additional Data**  
- 🏍️ Motorcycle: 8,000 scraped → cleaned → **5,542 annotated**.  
- 🪖 No-helmet: Kaggle dataset (13,400 → cleaned to 2,731 → **augmented to 13,655**).  

#### 🧪 Train-Test-Validation Split  
| Dataset                  | Training | Test | Validation |
|---------------------------|----------|------|------------|
| 🏍️ Motorcycle Detection   | 8,873    | 1,110 | 1,109 |
| 🪖 Helmet Detection       | 24,892   | 3,111 | 3,113 |
| 🔢 Number Plate Detection | 45,247   | 5,656 | 5,656 |

---

### 🎨 Data Augmentation  
- 🔄 Flipping, rotation (±25°), shearing (±8°).  
- 🌀 Gaussian blur (σ = 0–0.5).  
- 🌗 Contrast (0.75–1.5x), Lightness (0.8–1.2x).  
- 🎨 Color conversions (swapping, grayscale, sepia).  
- 📈 Triple-seat: Expanded from **300 → 4,736** images.  

---

### ⚙️ Algorithms Used  
<p align="center" style="display:flex; justify-content:center; gap:20px;">
  <img src="https://github.com/user-attachments/assets/80bdeb0a-ea2c-4667-a725-69b2fdc7b7b6" width="450" height="300" style="border:1px solid #ccc; border-radius:6px;" />
  <img src="https://github.com/user-attachments/assets/c9ed6224-5774-47ad-91d1-8b043be63a98" width="450" height="300" style="border:1px solid #ccc; border-radius:6px;" />
</p>  

---

### 🔧 Hyperparameters  
| **Hyperparameter** | **Settings** |
|---------------------|--------------|
| 📐 Image Size       | 640 × 640 px |
| 📦 Batch Size       | 16 / 32      |
| ⏳ Epochs           | 50–100       |
| ⚡ Learning Rate    | 0.01         |
| 🧮 Optimizer        | SGD          |
| 🌀 Weight Decay     | 0.0005       |
| 🔁 Momentum         | 0.937        |

---

### 🏗️ Proposed System Architecture  
<p align="center">
  <img src="https://github.com/user-attachments/assets/59d761e6-b387-40c8-94d3-2f0f9975a156" width="800"/>
</p>  

---

## ⚡ Implementation  

### 📷 Detection & Interfaces  
<!-- First Row -->
<p align="center" style="display:flex; justify-content:center; gap:20px;">
  <img src="https://github.com/user-attachments/assets/64ca4e37-7790-4e91-82e3-732bbf6a6312" width="400" />
  <img src="https://github.com/user-attachments/assets/afe22220-bc54-4b26-9108-1475df9782b2" width="400" />
</p>

<!-- Second Row -->
<p align="center" style="display:flex; justify-content:center; gap:20px;">
  <img src="https://github.com/user-attachments/assets/091c7b00-d3eb-4572-b734-ca39aca72a9f" width="400" />
  <img src="https://github.com/user-attachments/assets/3fcfe8a9-8c90-4956-90f2-7f5417b87d26" width="400" />
</p>

<!-- Third Row (Mobile Screenshot) -->
<p align="center">
  <img src="https://github.com/user-attachments/assets/01291d30-4e8a-4dbb-b9f4-84f2124ae335" width="300" />
</p>

---

## 📊 Results  

### 🏍️ Motorcycle Detection  
| **Model** | **Precision** | **Recall** | **mAP50** | **Training Time** |
|-----------|---------------|------------|-----------|-------------------|
| YOLOv8    | 99.29%        | 98.83%     | 99.37%    | 2.68 hrs |
| YOLOv9    | 98.67%        | 98.84%     | 99.44%    | 4.39 hrs |
| YOLOv10   | 98.61%        | 97.92%     | 99.41%    | 3.46 hrs |
| YOLOv11   | **99.59%**    | 98.62%     | 99.36%    | 3.42 hrs |

### 🪖 Helmet Detection  
| **Model** | **Precision** | **Recall** | **mAP50** | **Training Time** |
|-----------|---------------|------------|-----------|-------------------|
| YOLOv8    | 98.2%         | 92.02%     | 95.6%     | 6.8 hrs |
| YOLOv9    | 97.6%         | 93.4%      | 96.5%     | 11.15 hrs |
| YOLOv10   | 97.3%         | 93.3%      | 96.6%     | 8.8 hrs |
| YOLOv11   | **98.4%**     | **93.8%**  | **96.8%** | 7.5 hrs |

### 🔢 Number Plate Detection  
| **Model** | **Precision** | **Recall** | **mAP50** | **Training Time** |
|-----------|---------------|------------|-----------|-------------------|
| YOLOv8    | 98.72%        | 95.03%     | 97.51%    | 2.37 hrs |
| YOLOv9    | 98.25%        | 95.04%     | 97.00%    | 5.03 hrs |
| YOLOv10   | 97.47%        | 93.77%     | 97.24%    | 3.21 hrs |
| YOLOv11   | **98.91%**    | 94.42%     | 97.39%    | 4.06 hrs |

---

## ✅ Conclusion  
✨ The developed **SafeRide system**:  
- 🚦 Automates helmet & triple-seat detection.  
- ⏱️ Operates in **real-time with high accuracy**.  
- 📊 Shows **strong precision, recall & mAP** across YOLOv8–YOLOv11.  
- 🧾 Enables **automatic challan generation**, reducing manual work.  
- 🌍 Promotes **road safety & regulation adherence**.  

---
