---
title: Start Guide
---

## Install
- **Note: Requires a MacOS or Linux system.**
- Access the [GEMINI-App repository](https://github.com/GEMINI-Breeding/GEMINI-App){:target="_blank"}. 
- Clone into an IDE such as VSCode either using HTTPS or SSH. If using HTTPS, ensure your git credentials are populated via the terminal. If using SSH, make sure an SSH key for your machine is available in your Github account.
- Input the commands for setup listed on the GEMINI-App README.md:
```
# Download git submodules
git submodule update --init --recursive

# Install conda virtual environment
cd GEMINI-Flask-Server
./install_flask_server.sh
cd ../

# Install Node Version Manager
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.5/install.sh | bash
source ~/.bashrc

# Install Node 18
nvm install 18
nvm use 18

# Install dependencies
cd gemini-app
npm install --legacy-peer-deps # Fix the upstream dependency conflict
```

## Setup
- Create a directory `GEMINI-App-Data` in your home directory (`mkdir ~/GEMINI-App-Data`).
    - If this directory is created anywhere else, the path listed in `GEMINI-App/gemini-app/package.json` must be modified:

![package.json Path](_attachments/install/packageJsonPath.png)

- This path must point to a `GEMINI-App-Data` directory for the app to function.
- Install [Docker Desktop](https://www.docker.com/products/docker-desktop/){:target="_blank"} for your system. Ensure Docker Desktop is running before running the GEMINI App each time. 

## Running the App
*In gemini-app:*
```

# Run development server
npm run gemini # It wil run front and server concurrently. It will mix the logs

# If you want to run front only 
npm run front

# If you want to run flask server only
npm run server
```

## Troubleshooting
- If the GEMINI App is run before starting Docker Desktop, orthophoto generation will fail. To fix this, Docker Desktop must be started and the `GEMINI-App-Data/temp` directory must be deleted. The next attempt at generation with Docker Desktop running will properly create the temp files.