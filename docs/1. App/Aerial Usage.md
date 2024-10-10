---
title: Examples
---

## **Example Data**

Example data can be found in this link: [Example Data](https://ucdavis.box.com/s/ts802xlcddyufixfjmeayxwiiz2mxrb9)

Data includes:

- Drone Images (for Aerial-Based Trait Extraction)
- Rover Images (for Ground-Based Trait Extraction)

## **Aerial-Based Trait Extraction**

Start Docker Desktop and open the GEMINI app. If at any point more specific instructions are needed, navigate to the documentation page for the tab in use. 

### Upload

- Navigate to the Upload tab. If not already chosen, select **Image Data** in the `Data Type` field.
- Populate the following fields with information on the data to be uploaded. 
- After all fields have been populated, drag and drop files into the upload box or click in the box to select files via the file explorer.
- Once you have selected all files from the dataset, click **Upload** to upload the images to the app.
- After the uploading process is finished, click **Done**.
- If you wish to upload GCP Locations, change the `Data Type` field to **GCP Locations** and follow the same upload process as before.

### Process

- Navigate to the Process tab. In the data selection menu, select the `Year`, `Experiment`, `Location`, and `Population` of the previously uploaded data to be processed.
- Click **Begin Data Preparation**. In the Orthomosaic Generation window, expand the dropdown of the chosen `Platform` and `Sensor`. Click `Start` on the date to perform orthomosaic generation with.
- If GCP Locations were uploaded, use the slider bar and the **Previous** and **Next** buttons to step through images and mark the visible GCPs.
- Click **Generate Orthophoto**. Select the desired quality in the `Settings` dropdown. 
- Click **Process Images** to begin generation.

- Once generation has completed, click **Done** on the progress bar. Navigate to the Plot Boundary Preparation window. 
- Follow the instructions on importing of field design data. Once data is uploaded, proceed to the Population Boundary step.
- Select the orthomosaic to create the boundary for via the `Select an orthomosaic` dropdown.
- Use the **Draw** tool to outline the boundary of the portion of the orthomosaic you wish to analyze. 
- Use the **Edit**, **Select**, and **Translate** tools to modify a created boundary.
- Click **Save** and **Proceed** when finished to proceed to the Plot Boundary step.
- Select the correct orthomosaic as before. Use the rectangle generation tool in the bottom left to create the number and size of rectangles needed for the scale of analysis needed.
- Use the available tools to edit the placement of the rectangles.
- Click **Save** when finished.

- After creating the plot boundary, navigate to the Aerial Processing window.
- Expand the dropdown of the chosen `Platform` and `Sensor` once more. Click **Start** to process the traits of the desired date. 

### Stats

- Navigate to the Stats tab. Expand the dropdown of the chosen `Platform` and `Sensor` to see data for the available dates.
- Click **Load** to view the processed data of choice. Click **Download CSV** if desired.

### Map

- Navigate to the Map tab. Open the data selection menu to select the data to analyze.
- Use the dropdown menu to select the `Trait Metric` to view.
- The traits can be seen overlaid on the orthomosaic based on the plot boundaries created earlier.

## **Ground-Based Trait Extraction**

Please complete Aerial-Based Trait Extraction before proceeding with Ground-Based Trait Extraction. You will need to utilize the plot the plot boundaries created in the Aerial-Based Trait Extraction process.

### Upload

#### Images

- Navigate to the Upload tab. If not already chosen, select **Image Data** in the `Data Type` field.
- Populate the following fields with information on the data to be uploaded. 
- After all fields have been populated, drag and drop files into the upload box or click in the box to select files via the file explorer.
- Once you have selected all files from the dataset, click **Upload** to upload the images to the app.
- After the uploading process is finished, click **Done**.
  
#### Metadata

- Change the `Data Type` field to **Platform Logs**.
- Populate the following fields with information on the data to be uploaded and then upload the files.

    - The metadata of these images include camera information, GPS locations, and timestamps.
    - Refer to the the `msgs_synced.csv` file to format your metadata file for personal use.

### Process

#### Locate Plants
In this section, you will use an early date to locate plants in the field.

- Select the **Ground Processing** tab. In the data selection menu, select the `Year`, `Experiment`, `Location`, and `Population` of the previously uploaded data to be processed.
- Navigate to the **Locate Plants** tab. In this tab, you will annotate individual plants in an image, train a machine learning model to detect individual plants, and then find every plant in the field.
- Select the Platform and Sensor you would like to do this process for.
- Click on the `Labels` button to label your data. Click on `Annotate` and wait for the software (CVAT) to open. This could take a while. **Note: Please allow pop-ups for this process.**
  
  - A new tab should open with the labelling software. Create an account if you do not have one already.
  - Perform your annotations and then download the annotations. **Use YOLO format during your export!**
  - Upload the `.txt` files into the app.

- After annotating your images, you can now train your model. Click on the button under `Model` for the specific date. Next, press `Train Model`.

  - You can expand the progress bar to track the model performance.
  - After training, you should be able to see the generated model.

- Next, click on the button under the `Locations` column. 

  - Select the model you would like to use for this process. It is preferred to select the model with the highest performance score.
  - Then, you can press the `Locate` button.

#### Trait Extraction

In this section, you will extract traits from the located plants. You can select any date for this process.

- Navigate to the **Label Traits** tab. In the `Select Trait` dropdown, select the trait you would like to extract.
- Select the Platform and Sensor you would like to do this process for. Similarily to the **Locate Plants**, annotate the necessary images and upload them.
- Next, go to the **Train Traits** tab. Select the `Trait` you would like to train the model for. 

  - Click on the `New Model` button.
  - Select the Platform, Sensor and Date you would like to train the model for.
  - Then, press the `Train Model` button.
  - Again, you can view the resulting model after the process is done.

- Finally, go to the **Extract Traits** tab. Select the `Trait` you would like to extract. 

  - Select the Platform, Sensor, Date, Locations ID, and Model ID you would like to use for this process. It is preferred to select the model with the highest performance score.
  - Then, you can press the `Extract` button.