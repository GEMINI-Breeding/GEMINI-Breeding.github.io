---
title: Installation
---

- Access the [repository](https://github.com/GEMINI-Breeding/GEMINI-App){:target="_blank"} to prepare to clone. 
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


# Run development server
npm run gemini # It wil run front and server concurrently. It will mix the logs

# If you want to run front only 
npm run front

# If you want to run flask server only
npm run server
```

