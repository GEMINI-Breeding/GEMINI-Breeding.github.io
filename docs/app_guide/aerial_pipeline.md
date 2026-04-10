# Aerial Pipeline

This guide demonstrates how to set up and execute aerial data processing pipelines using drone imagery. It covers workspace creation, pipeline configuration, orthomosaic generation, and trait extraction steps.

## Video Tutorial
[**Watch the full guide on Guidde**](https://app.guidde.com/playbooks/sHizWZaczgnxsHx2yuwiP8)

[![Quick guidde](https://static.guidde.com/v0/qg%2FDV0gSkUhbsfKSCPMFfYn4kuNAIt1%2FsHizWZaczgnxsHx2yuwiP8%2FfJ2TqYX8GZo82YDMrzwy8g_cover.png?alt=media&token=7a2aedb7-e868-44e5-b893-7787ff858b2b)](https://app.guidde.com/share/playbooks/sHizWZaczgnxsHx2yuwiP8)

---

## 1. Creating a Workspace
To begin processing, navigate to the **Process** tab.
1. Create a new workspace (e.g., "Cowpea 2022") and add a brief description.
2. Click on your newly created workspace to begin pipeline configuration.

- **Actions:** Navigate to Process -> Create New Workspace -> Enter Details.

![Creating New Workspace](https://static.guidde.com/v0/qg%2FDV0gSkUhbsfKSCPMFfYn4kuNAIt1%2FsHizWZaczgnxsHx2yuwiP8%2FjSCXv1dSBB5kxNgytjZ4Gd_doc.png?alt=media&token=4d8d29f8-057d-40c5-9c25-b11fa226132e)

## 2. Configuring the Aerial Pipeline
1. Select **Aerial Pipeline** as the processing type.
2. Define your **ODM (Open Drone Map)** settings. You can choose from pre-selected quality presets (Draft, Standard, High, Ultra) or define custom parameters.
3. Configure **Inference Models** if you intend to run RoboFlow computer vision tasks for detection or segmentation.

- **Pipeline setup:** Select Pipeline type -> Define ODM settings -> Set Inference Models.

![Setting Up Aerial Pipeline](https://static.guidde.com/v0/qg%2FDV0gSkUhbsfKSCPMFfYn4kuNAIt1%2FsHizWZaczgnxsHx2yuwiP8%2FpQEMofHpne3hYbMDRgny33_doc.png?alt=media&token=beec748b-7aeb-42e2-bd02-781da8b2344a)

## 3. Execution Steps
Each pipeline run follows a structured sequence:

### Data Sync
The app extracts GPS metadata directly from the images. Ensure you select **Use own metadata** to proceed with image metadata or sync from another source if available (timestamp based).

### Ground Control Point (GCP) Selection
Matching drone images to GCPs is crucial for accurate orthomosaics.

1. Upload your GCP locations (CSV format).
2. The tool will automatically filter images close to GCPs.
3. Mark the corresponding GCP in each image to establish spatial alignment.

- **GCP workflow:** Upload CSV -> Filter/Select GCPs -> Mark GCPs on images.

![GCP Selection](https://static.guidde.com/v0/qg%2FDV0gSkUhbsfKSCPMFfYn4kuNAIt1%2FsHizWZaczgnxsHx2yuwiP8%2FufoRDgCaYX9BUdpVTRqQS2_doc.png?alt=media&token=e480c0bf-1095-409a-88ef-df50a4229f72)

### Orthomosaic Generation
This step feeds the synced images and GCPs into Open Drone Map. Once finished, you can preview the generated orthomosaic, download a high-resolution version, or export the original TIFF file.

- **Results:** Preview generated orthomosaic, download TIFF files.

### Plot Boundary Preparation
1. Upload your field design CSV and map the columns (`row`, `col`, `plot`, `accession`).
2. Define the population boundary around your field.
3. Generate the plot grid and align the individual plot boundaries with the orthomosaic. You can move, resize, and save these as reusable versions for future dates.

- **Grid tools:** Map CSV columns -> Define population boundary -> Generate grid -> Align plot boundaries.

![Plot Boundary Preparation](https://static.guidde.com/v0/qg%2FDV0gSkUhbsfKSCPMFfYn4kuNAIt1%2FsHizWZaczgnxsHx2yuwiP8%2Ff9Sp4hdKrQVMVRFDhtZ8iX_doc.png?alt=media&token=2b9df1c4-a6c4-4caa-8d62-486b9476693e)

### Initial Trait Extraction
Finally, the app crops individual plots and calculates vegetation fraction and canopy height. Use the threshold slider to ensure accurate vegetation extraction before running the full process.

- **Crop/Extract:** Adjust threshold slider -> Extract traits.

![Initial Trait Extraction](https://static.guidde.com/v0/qg%2FDV0gSkUhbsfKSCPMFfYn4kuNAIt1%2FsHizWZaczgnxsHx2yuwiP8%2FqVzWjHyaisSNpyTBX41JNj_doc.png?alt=media&token=647231fb-ffce-449d-99eb-ae57220f2c86)
