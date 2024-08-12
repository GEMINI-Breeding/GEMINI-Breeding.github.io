---
title: Examples
---

## **Aerial Trait Extraction**

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

