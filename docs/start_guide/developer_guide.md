# Developer Guide

Welcome to the GEMINI Breeding developer documentation.

## Overview
The GEMINI project consists of a Tauri-based desktop shell, a React frontend, and a FastAPI backend.

## Tech Stack
| Layer | Technology |
|-------|-----------|
| Desktop shell | [Tauri v2](https://tauri.app) (Rust) |
| Frontend | React 18, [TanStack Router](https://tanstack.com/router), [TanStack Query](https://tanstack.com/query), [shadcn/ui](https://ui.shadcn.com), Tailwind CSS |
| Backend | [FastAPI](https://fastapi.tiangolo.com), [SQLModel](https://sqlmodel.tiangolo.com), SQLite |
| Python runtime | Python 3.12, managed by [uv](https://docs.astral.sh/uv/) |
| API client | Auto-generated from OpenAPI schema via [@hey-api/openapi-ts](https://heyapi.dev) |

## Development Setup
1. **Clone with submodules:**
   ```
   git clone --recurse-submodules https://github.com/GEMINI-Breeding/GEMINI-App.git
   cd GEMINI-App
   ```
2. **Setup Backend:**
   ```
   cd backend
   uv sync
   ```
3. **Setup Frontend:**
   ```
   cd frontend
   npm install
   ```

## Starting the App
For development, you can use the following commands from the `frontend/` directory:

- **Full stack (Backend + Vite):**
  ```
  npm run dev:full
  ```
- **Tauri native desktop window:**
  ```
  npm run tauri:dev
  ```

## Building the App
Building the application requires environment-specific setups.

### Quick Build Overview
- **Linux/macOS:** Use the root `build.sh` script.
- **Windows:** Use the `build-windows.ps1` PowerShell script.

### Platform-Specific Requirements
| Platform | Key Requirements | Build Command |
|----------|------------------|---------------|
| **Linux** | Ubuntu 22.04 (recommended) | `./build.sh` |
| **macOS** | Xcode CLI Tools | `./build.sh` |
| **Windows** | Visual Studio Build Tools 2022, Inno Setup 6, **Docker Desktop** | `.\build-windows.ps1` |

> **Note on Windows:** **Docker Desktop** is required for certain data processing features in the application. Ensure it is running when performing these tasks.

### Build Optimization
You can skip full rebuilds if only the frontend has changed:
- **Linux/macOS:** `./build.sh tauri`
- **Windows:** `.\build-windows.ps1 tauri`

*For comprehensive build instructions, troubleshooting, and platform-specific prerequisites, please consult the `BUILDING.md` file in the [GEMINI-App repository](https://github.com/GEMINI-Breeding/GEMINI-App).*

## Schema Summary
The GEMINI project utilizes a flexible SQLite-based backend managed by SQLModel, alongside a structured filesystem layout.

### Database
- **Core Tables:** `User`, `Workspace`, `Pipeline`, `PipelineRun`, `TraitRecord`, `PlotRecord`.
- **Schema Management:** The schema is automatically created via `SQLModel.metadata.create_all()` at startup; no manual migrations are required.
- **Data Access:** All persistence is handled via CRUD helpers in `backend/app/crud/`.

### Filesystem Structure
The project follows a deterministic path convention defined in `RunPaths`.
- **`Raw/`**: Stores raw uploaded data (images, logs).
- **`Intermediate/`**: Stores derived data (plot boundaries, GCPs, sync files).
- **`Processed/`**: Stores final outputs (orthomosaics, trait GeoJSONs, cropped plot images).

*All file paths should be accessed via the `RunPaths` utility to ensure environment portability. Relative paths are stored in the database, with absolute paths reconstructed at runtime.*

*For a comprehensive reference, please refer to the `SCHEMA.md` file in the [GEMINI-App repository](https://github.com/GEMINI-Breeding/GEMINI-App).*
