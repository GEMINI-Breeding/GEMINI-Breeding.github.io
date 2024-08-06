---
title: Start Guide
---

## Install
- Access the [GEMINI-App repository](https://github.com/GEMINI-Breeding/GEMINI-App){:target="_blank"}. 
- Clone into an IDE such as VSCode using HTTPS or SSH. If using HTTPS, ensure your git credentials are populated via the terminal. If using SSH, make sure an [SSH key](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account){:target="_blank"} for your machine is available in your Github account.
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
- If the path in `package.json` is not properly populated, a `Failed to upload file` error will appear. Make sure the path points to an existing and accessible directory.
- If the GEMINI App is run before starting Docker Desktop, orthophoto generation will fail. To fix this, Docker Desktop must be started and the `GEMINI-App-Data/temp` directory must be deleted. The next attempt at generation with Docker Desktop running will properly create the temp files.
- To ensure that the app is properly running in Docker, after the command `npm start gemini`, ensure that the terminal is NOT cleared (meaning you should be able to scroll up and see previous commands). If the terminal is cleared (you are unable to scroll up to view previous commands), the app is not running in Docker properly. Restart Docker and try again. 
