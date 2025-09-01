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

<div style="display:flex; justify-content: space-around; gap: 20px;">

  <!-- Triple Seat Data -->
  <div>
    <h3 style="background-color:#ff9933; padding:6px; border-radius:6px; text-align:center; color:white;">
      Triple Seat Data
    </h3>
    <table>
      <tr><th>Dataset</th><th>Source</th><th>Size</th></tr>
      <tr><td>Traffic Violation</td><td>Roboflow</td><td>454</td></tr>
      <tr><td>Triple Ride</td><td>Roboflow</td><td>3,000</td></tr>
      <tr><td>Google Images</td><td>Google</td><td>300</td></tr>
    </table>
  </div>

  <!-- Helmet Data -->
  <div>
    <h3 style="background-color:#ffcc00; padding:6px; border-radius:6px; text-align:center; color:white;">
      Helmet Data
    </h3>
    <table>
      <tr><th>Dataset</th><th>Source</th><th>Size</th></tr>
      <tr><td>helmet-2</td><td>Roboflow</td><td>3,774</td></tr>
      <tr><td>helmet-1</td><td>Roboflow</td><td>2,420</td></tr>
      <tr><td>Helmet Detection-I</td><td>Roboflow</td><td>523</td></tr>
      <tr><td>Helmet Dataset-I</td><td>Roboflow</td><td>523</td></tr>
      <tr><td>helmet-detection-20241117</td><td>Roboflow</td><td>4,110</td></tr>
      <tr><td>Helmet Wearing Image Dataset: 13th reference</td><td>Mendeley</td><td>13,780</td></tr>
    </table>
  </div>

  <!-- Number Plate Data -->
  <div>
    <h3 style="background-color:#ff6600; padding:6px; border-radius:6px; text-align:center; color:white;">
      Number Plate Data
    </h3>
    <table>
      <tr><th>Dataset</th><th>Source</th><th>Size</th></tr>
      <tr><td>License-Plate-Detection-2</td><td>Roboflow</td><td>2,460</td></tr>
      <tr><td>ANPR_PROJECT</td><td>Roboflow</td><td>8,270</td></tr>
      <tr><td>Vehicle-Registration-Plates-2</td><td>Roboflow</td><td>21,175</td></tr>
    </table>
  </div>

</div>

