---
title: Quick Start Guide
---

## **Getting Started with the farm-ng Amiga**

1. **Control the Amiga.**
    - Go through the dashboard overview. We recommend getting 
comfortable with the speed adjustment and e-stop configuration.
    - We recommend going 100 - 200 ft/min (the first 2 major ticks) to 
get the best image quality. See the [farm-ng Amiga Dashboard Documentation](https://amiga.farm-ng.com/docs/dashboard/dashboard-user-guide){:target="_blank"} for more information on use of the dashboard.
![Image title](imgs/amiga_dash_light.png#gh-light-mode-only)
![Image title](imgs/amiga_dash_dark.png#gh-dark-mode-only)
2. **Set up the GPS RTK base station.**
    - Connect the powerbrick to the CAN/POWER input on the back of 
the Brain. It will start doing its serve and pinning its position. 
    - The base station will get some time to have a good accuracy. Marcelo 
recommends you power it up, use the UI to connect to WIFI, and 
leave static for at least 20 min before connecting to receive 
corrections.
    - Once the base station is connected, you should see the GPS icon at 
the top right of the Brain without the slash.
3. **Record some sample images in a field or with random objects.**
    - Follow the [farm-ng Camera App Documentation](https://amiga.farm-ng.com/docs/apps/camera_app/){:target="_blank"} on how to start and stop a recording. 
    - Have the GPS and the top camera (facing down) centered on the 
Amiga.
    - The side cameras can be placed as low as possible. Play around 
with the angle of the side cameras and preview the images from 
the Brain.

4. **Export the recorded file.**
    - You will need a USB drive plugged into the
back of the brain. Make sure to only plug in the drive after the brain has been turned on.
    - Open the file manager app to view 
 the images and export. Refer to the [farm-ng File Manager App Documentation](https://amiga.farm-ng.com/docs/apps/file_manager_app/){:target="_blank"} for more information on using the file manager for viewing and exporting.

## **Data Saving and Export SOPs**
- The GEMINI App will be used for extraction of the binary files recorded using the Amiga. Follow the [app installation and setup instructions](../../1.%20App/1-%20Installation.md) before proceeding.
- Once you are done recording, use the [file manager app](https://amiga.farm-ng.com/docs/apps/file_manager_app/){:target="_blank"} to export the binary files to an external drive.
    -  Note that the USB drive must be ext4 or exFAT formatted. USB 3.0 drives are recommended for faster file-transfer.
    -  Once data has been successfully transferred to the drive, the files in the file manager can be deleted.
- Using the upload tab of the GEMINI App, upload the binary files to begin extracting the binary files to viewable formats. 
    - Viewing of the extracted data will be added soon to the GEMINI App.



