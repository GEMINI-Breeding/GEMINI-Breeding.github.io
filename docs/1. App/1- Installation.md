---
title: Start Guide
---

# Installation Guide

## Quick Start with Docker Compose (Recommended)

The easiest way to get started with the GEMINI App is using Docker Compose. This method automatically handles all dependencies and configurations.

### Prerequisites

Install [Docker Desktop](https://www.docker.com/products/docker-desktop/){:target="_blank"} for your operating system:

- [Windows](https://docs.docker.com/desktop/install/windows-install/){:target="_blank"}
- [MacOS](https://docs.docker.com/desktop/install/mac-install/){:target="_blank"}
- [Linux](https://docs.docker.com/desktop/install/linux-install/){:target="_blank"}

### Installation Steps

1. Clone the repository

        git clone https://github.com/GEMINI-Breeding/GEMINI-App.git
        cd GEMINI-App

2. Create the data directory:

        mkdir ~/GEMINI-App-Data

3. Optional: Customize the environment variables

    Open the `.env` file in the `GEMINI-App` directory to customize ports and data directory

        # .env file for GEMINI-App
        # MapBox Access Token (required for map functionality)
        REACT_APP_MAPBOX_TOKEN=your.mapbox.access.token.here

        # Port Configuration
        REACT_APP_FRONT_PORT=3000
        REACT_APP_FLASK_PORT=5050
        REACT_APP_TILE_SERVER_PORT=8091
        PORT=$REACT_APP_FRONT_PORT

        # Application Data Directory (absolute path)
        REACT_APP_APP_DATA=$HOME/GEMINI-App-Data

    **Notes:**

    - Get your MapBox token from [MapBox Access Tokens](https://docs.mapbox.com/help/glossary/access-token/){:target="_blank"}
    - Comments must be on separate lines (inline comments are not supported)
    - Use absolute paths for `REACT_APP_APP_DATA`
    - Default values will be used if `.env` file is not present

4. Run the application

        # CPU version (default)
        docker compose up --pull always

        # GPU version (if nvidia-smi works on host)
        docker compose -f docker-compose-gpu.yml up --pull always

    **Note**: The `--pull always` flag ensures you're always using the latest Docker images.

4. Access the application:

    - Frontend: [http://localhost:3000](http://localhost:3000) (or your configured `REACT_APP_FRONT_PORT`)

    For debugging:

    - Backend API: [http://localhost:5050](http://localhost:5050) (or your configured `REACT_APP_FLASK_PORT`)
    - Tile Server: [http://localhost:8091](http://localhost:8091) (or your configured `REACT_APP_TILE_SERVER_PORT`)

### Docker Configuration

#### Understanding docker-compose.yml

The `docker-compose.yml` file defines how the GEMINI App runs in Docker. Here's what each section does:

```yaml
services:
  app:
    image: paibl/gemini-breeding:latest  # Pre-built Docker image
    build:
      context: .
      dockerfile: Dockerfile
    env_file:
      - ./gemini-app/.env  # Load environment variables
    ports:
      - "${REACT_APP_FRONT_PORT:-3000}:${REACT_APP_FRONT_PORT:-3000}"   # Frontend
      - "${REACT_APP_FLASK_PORT:-5050}:${REACT_APP_FLASK_PORT:-5050}"   # Backend
      - "${REACT_APP_TILE_SERVER_PORT:-8091}:${REACT_APP_TILE_SERVER_PORT:-8091}"  # Tile Server
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock  # Allow Docker-in-Docker
      - ${REACT_APP_APP_DATA:-~/GEMINI-App-Data}:/root/GEMINI-App-Data  # Data directory
      - ./gemini-app/.env:/app/gemini-app/.env:ro  # Environment variables (read-only)
```

**Key Configuration Parameters:**

- **Ports**: Maps host ports to container ports
    - Format: `"host_port:container_port"`
    - Default ports: 3000 (frontend), 5050 (backend), 8091 (tile server)
    - Change these if ports are already in use on your system

- **Volumes**:
    - **Docker socket**: `/var/run/docker.sock` enables Docker-in-Docker for OpenDroneMap
    - **Data directory**: `~/GEMINI-App-Data` stores all application data (images, orthomosaics, models)
    - **Environment file**: `.env` file is mounted as read-only

- **Environment Variables**: Loaded from `.env` file with fallback defaults

For more detailed configuration options, see the [docker-compose.yml](https://github.com/GEMINI-Breeding/GEMINI-App/blob/main/docker-compose.yml){:target="_blank"} file.

### Updating the Application

To update to the latest version:

```bash
cd GEMINI-App
docker compose down
docker compose up --pull always
```

The `--pull always` flag will automatically download the latest Docker images before starting the containers.

### Rebuilding Docker Images

If you've made local changes and need to rebuild:

```bash
# Rebuild and start
docker compose up --build

# Or rebuild specific services
docker compose build
docker compose up
```

---

## Platform-Specific Notes

### Windows

- [Install WSL2](https://learn.microsoft.com/en-us/windows/wsl/install){:target="_blank"} for better Docker performance. Install the default Ubuntu distribution to avoid compatibility issues.
- Ensure Docker Desktop is configured to use WSL2 backend.
- Follow the instructions for [Configuring WSL2 with Docker Desktop](https://docs.docker.com/desktop/wsl/){:target="_blank"}.
- The data directory path in WSL2: `~/GEMINI-App-Data` (equivalent to `/home/yourusername/GEMINI-App-Data`)
- In your `.env` file, use Linux-style paths when running in WSL2

### MacOS

- Install [XCode and CLI Tools](https://www.freecodecamp.org/news/how-to-download-and-install-xcode/){:target="_blank"} for development.
- **Note**: The GEMINI App attempts to find an NVIDIA GPU for OpenDroneMap orthomosaic generation. Due to the lack of a compatible GPU on MacOS systems, the following error is expected:
  ```
  docker: Error response from daemon: could not select device driver "" with capabilities: [[gpu]].
  ```
  The app will automatically fall back to CPU processing, which may result in longer processing times.

### Linux

- The recommended distribution for the GEMINI App is Ubuntu. Other distros may encounter compatibility issues.
- If your system has an NVIDIA GPU for orthophoto generation:
  1. Install the [NVIDIA Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html){:target="_blank"}
  2. Follow the relevant setup instructions
  3. Use the GPU-enabled Docker Compose file:

```bash
docker compose -f docker-compose-gpu.yml up --pull always
```

- If the NVIDIA Container Toolkit is not installed, the following error will appear during orthophoto generation:

```
docker: Error response from daemon: could not select device driver "" with capabilities: [[gpu]].
```

The app will fall back to CPU processing automatically.

---

## Advanced: Native Installation for Developers

For developers who want to run the application natively without Docker:

### Prerequisites

- Git
- Python 3.8+
- Node.js 18
- Docker Desktop (for OpenDroneMap container)

### Installation Steps

1. Clone the repository:

        git clone https://github.com/GEMINI-Breeding/GEMINI-App.git
        cd GEMINI-App

2. Initialize git submodules:

        git submodule update --init --recursive

3. Set up Flask backend:

        cd GEMINI-Flask-Server
        ./install_flask_server.sh
        cd ../


4. Install Node Version Manager (NVM):

        curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.5/install.sh | bash
        source ~/.bashrc


5. Install Node 18:

        nvm install 18
        nvm use 18


6. Install frontend dependencies:

        cd gemini-app
        npm install --legacy-peer-deps  # Fix upstream dependency conflicts


### Running the App

Ensure Docker Desktop is running before starting the GEMINI App.

In `GEMINI-App/gemini-app`:

```bash
# Run development server (frontend and backend concurrently)
npm run gemini 

# Run frontend only
npm run front

# Run Flask server only
npm run server
```

### Updating Native Installation

#### Option 1: Auto-Update using startup script
```bash
cd GEMINI-App
./startup.sh
```

#### Option 2: Manual update using git
```bash
cd GEMINI-App

# Stash any local changes
git stash
cd GEMINI-Flask-Server
git stash
cd ..

# Pull changes
git fetch
git pull

# Update submodules
git submodule update --init --recursive
```

---

## Troubleshooting

### Docker-Related Issues

**Container fails to start**: 

  - Ensure Docker Desktop is running and has sufficient resources allocated (recommended: 4GB RAM minimum)
  - Check if `.env` file is properly formatted (no inline comments)

**Port conflicts**: 
  - If ports 3000, 5050, or 8091 are already in use, modify the port mappings in `.env` file
  - Example: Change `REACT_APP_FRONT_PORT=3000` to `REACT_APP_FRONT_PORT=3050`

**Volume mount issues**: 

  - Verify that `~/GEMINI-App-Data` exists and has proper permissions
  - Check that the path in `.env` file is absolute, not relative
  - On Windows WSL2, ensure you're using Linux-style paths

**Environment variable not loading**:

  - Ensure `.env` file is in the correct location (`GEMINI-App/` directory)
  - Check for syntax errors (comments must be on separate lines)
  - Restart containers after modifying `.env`: `docker compose down && docker compose up`

### Native Installation Issues

**Failed to upload file error**: 

  - Check that the path in `package.json` points to an existing and accessible `GEMINI-App-Data` directory
  - Verify the Flask Server started successfully
  - Check terminal logs for Flask Server errors

**Terminal cleared during npm start**: 

  - If you cannot scroll up to see previous commands after running `npm start gemini`, Docker is not running properly
  - Restart Docker Desktop and try again

**Orthophoto generation failures**: 

  - Manually delete the `~/GEMINI-App-Data/temp` directory
  - Try generation again
  - Check Docker logs for OpenDroneMap container errors

**farm-ng-core installation error** (MacOS): 

  - If you see: `error: variable length arrays in C++ are a Clang extension [-Werror,-Wvla-cxx-extension]`
  - Open `setup.py` inside the `farm-ng-core` directory
  - Remove `"-Werror"` from the `extra_compile_args` list
  - Retry installation

**WSL2-specific issues** (Windows):

  - Install libgl1 library: `sudo apt-get update && sudo apt-get install libgl1`
  - Add user to docker group: `sudo usermod -aG docker $USER`
  - Apply changes: `newgrp docker`
  - Verify Docker context: `docker context use default`

### Getting Help

If you encounter issues not covered here:

1. Check the [Full Documentation](https://gemini-breeding.github.io/){:target="_blank"}
2. Review [GitHub Issues](https://github.com/GEMINI-Breeding/GEMINI-App/issues){:target="_blank"}
3. Create a new issue with detailed error logs and system information