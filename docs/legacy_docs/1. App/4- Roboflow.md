---
title: Roboflow Usage
---


To extract traits from uploaded images, the GEMINI App supports both use of models trained using Roboflow or locally.

## Getting Started with Roboflow

When using Roboflow, we recommend the following steps to get started:

• Create a Roboflow account: [app.roboflow.com](https://app.roboflow.com){:target="_blank"}

• Create a new workspace or join a shared workspace.

• Create a new project and name it as desired based on the trait(s) you are labeling. 

• Place this project in the correct location based on your workspace's standards for the images being uploaded (location / platform / sensor).

## Extracting Traits Using Roboflow

Traits can be extracted using Roboflow models through two possible methods:

**Method 1: Label and Train Custom Model**

• Download plot images from the manage files tab (ground-based) or plot image extractor (UAV-based). Upload them to your Roboflow project.

• Use the Roboflow labeling tool to annotate your images.

• Train your model in Roboflow.

• Note your model ID, version, and API key.

• Enter these attributes into the "Predict" section of the app to get results.

**Method 2: Use Pretrained Model**

• Select a pretrained model from Roboflow Universe that is close to your use case: universe.roboflow.com.

• Use the Fork Project button to create a copy of the model in your workspace.

• Note the model ID, version, and API key.

• Enter these attributes into the "Predict" section of the app to get results.


**On the "Predict" step, note the difference between cloud (hosted) inference and local inference for Roboflow models. The local option is preferred to minimize cost on Roboflow, but the cloud option may be chosen for less powerful workstations.**

## Using Non-Roboflow Models

If desired, Roboflow can be avoided for trait extraction.

• Train a YOLOv8 or YOLOv11 detection or segmentation model locally or on another service using labeled images.

• Alternatively, you can pull the model weights from another pretrained model and upload those to the app.

• Upload your model weights using the "Select" section of the app.

• Select the local model upload option on the "Predict" step and choose the uploaded model.