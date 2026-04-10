# Ground Pipeline

This guide demonstrates how to set up and execute ground-based image processing pipelines using rover (e.g., Amiga) data. It covers workspace creation, plot marking, image stitching, and running inference models.

## Video Tutorial
[**Watch the full guide on Guidde**](https://app.guidde.com/playbooks/abiKKaPsfMQKarLxansBaA)

[![Quick guidde](https://static.guidde.com/v0/qg%2FDV0gSkUhbsfKSCPMFfYn4kuNAIt1%2FabiKKaPsfMQKarLxansBaA%2F4DMvYsHK5LCsuNVFgmeHWU_cover.png?alt=media&token=d1b6dc98-1993-4eac-bcde-f6e8482ea402)](https://app.guidde.com/share/playbooks/abiKKaPsfMQKarLxansBaA)

---

## 1. Creating a Ground Workspace
Navigate to the **Process** tab.
1. Create a new workspace specifically for your ground data (e.g., "Amiga Ground 2025").
2. Select **Ground Pipeline** when creating the pipeline.

- **Actions:** Navigate to Process -> Create New Workspace -> Enter Details.

## 2. Configuration
- **Stitch Settings:** Choose your platform (e.g., "Amiga"). Predefined settings are available, or you can configure parameters manually.
- **Inference Models:** Configure your RoboFlow API key and model ID to run tasks like flower detection. You can toggle between cloud and local server processing.

- **Setup:** Select platform -> Configure processing settings -> Define inference models.

![Ground Pipeline Configuration](https://static.guidde.com/v0/qg%2FDV0gSkUhbsfKSCPMFfYn4kuNAIt1%2FabiKKaPsfMQKarLxansBaA%2FcNkSPv4QDotEvTwAgbFLfw_doc.png?alt=media&token=7c49369b-2f8a-4f2c-a962-9ad6790681ca)

## 3. Pipeline Execution Steps

### Plot Marking
Unique to the ground pipeline, this tool defines the start and end of each plot in your image sequence.
1. Use keyboard shortcut `S` to mark the start of a plot and `E` to mark the end.
2. Select the **Stitch Direction** (e.g., Right).
3. Use the GPS Map view to track the rover's path as a quality check.
4. Press `N` to start marking the next plot.

- **Marking tools:** S (Start) -> E (End) -> N (New plot) -> GPS Map check.

![Plot Navigation And Quality Checks](https://static.guidde.com/v0/qg%2FDV0gSkUhbsfKSCPMFfYn4kuNAIt1%2FabiKKaPsfMQKarLxansBaA%2Fa84aMYw8ZzbFiTAe4Xveyv_doc.png?alt=media&token=e94b2895-e7f4-490a-9bc5-9fa7ee393e07)

### Stitching
Run the stitching step once your plots are marked.
- **Optional Cropping:** Use the crop tool in settings to remove inconsistent lighting and ensure a clean stitch.
- Rerun as needed to fine-tune stitching parameters.

- **Stitching workflow:** Optional crop -> Configure params -> Run stitch.

![Stitching Setup And Execution](https://static.guidde.com/v0/qg%2FDV0gSkUhbsfKSCPMFfYn4kuNAIt1%2FabiKKaPsfMQKarLxansBaA%2FkbetACm7ALbideV4kcS88k_doc.png?alt=media&token=51cbc67d-e2d8-4b5e-b858-3752d5bc65d6)

### Boundary Preparation and Association
1. Upload your field design CSV and map columns (`row`, `col`, `plot`, `accession`).
2. The population boundary will auto-generate; adjust if necessary.
3. Use the **Associate Boundaries** step to link the field design metadata to your stitched plots.

- **Field Design:** Upload/map CSV -> Auto-generate/Adjust boundary -> Associate.

![Boundary Preparation And Field Design](https://static.guidde.com/v0/qg%2FDV0gSkUhbsfKSCPMFfYn4kuNAIt1%2FabiKKaPsfMQKarLxansBaA%2Ffhu8iBtWnvrP3qJeQkATKs_doc.png?alt=media&token=5d5b5301-d052-4307-bda7-21a542a3708a)

### Inference
Run your configured RoboFlow model. You can tune detection results by adjusting:
- **Confidence Threshold:** Lower this to catch more detections if they are being missed.
- **Overlap Threshold:** Adjust to handle overlapping bounding boxes.
Apply these thresholds to generate your final trait output.

- **Tuning:** Adjust confidence/overlap thresholds -> Apply settings.

![Inference Results And Parameter Tuning](https://static.guidde.com/v0/qg%2FDV0gSkUhbsfKSCPMFfYn4kuNAIt1%2FabiKKaPsfMQKarLxansBaA%2FoGeR85wHymUT8HrCsTXHBS_doc.png?alt=media&token=ba7d7d9e-9900-44bd-a3df-42d3b26773c1)
