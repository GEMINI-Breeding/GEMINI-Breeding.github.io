# Developer Guide

Welcome to the GEMINI Breeding developer documentation.

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Desktop shell | [Tauri v2](https://tauri.app) (Rust) |
| Frontend | React 18, [TanStack Router](https://tanstack.com/router), [TanStack Query](https://tanstack.com/query), [shadcn/ui](https://ui.shadcn.com), Tailwind CSS v4 |
| Backend | [FastAPI](https://fastapi.tiangolo.com), [SQLModel](https://sqlmodel.tiangolo.com), SQLite |
| Python runtime | Python 3.12, managed by [uv](https://docs.astral.sh/uv/) |
| API client | Auto-generated from OpenAPI schema via [@hey-api/openapi-ts](https://heyapi.dev) |
| Linting | [Biome](https://biomejs.dev) (frontend), [Ruff](https://docs.astral.sh/ruff/) (backend) |

---

## Development Tools & Ecosystem

GEMINI-App leverages a modern, high-performance toolchain to ensure developer productivity and a polished user experience.

### Frontend Tooling

- **Vite:** The project uses Vite for lightning-fast Hot Module Replacement (HMR) and optimized production builds. In development mode, Vite's proxy handles requests to the FastAPI backend, while in production, it's bundled into the Tauri desktop shell.
- **Tauri v2:** Provides a lightweight Rust-based bridge between the webview and the operating system. It manages the lifecycle of the Python sidecar (the backend), handles native file dialogs, and manages the desktop window.
- **shadcn/ui & Radix UI:** Instead of a traditional component library, the app uses `shadcn/ui` which provides high-quality, accessible Radix UI primitives that are "owned" by the project (copied into `src/components/ui/`). This allows for full customization of every component.
- **Tailwind CSS v4:** A CSS-first utility framework used for styling. Version 4 provides a high-performance engine and a streamlined development workflow.
- **TanStack Ecosystem:**
    - **TanStack Router:** Provides a type-safe, file-based routing system. This ensures that every URL and parameter is verified at compile-time, reducing runtime errors.
    - **TanStack Query:** Manages all server state, caching, and background synchronization between the frontend and the FastAPI backend.
    - **TanStack Table:** Powering the "Analyze" tab's grid view, this headless library allows for complex filtering, sorting, and pagination of large datasets without sacrificing performance.
- **Biome:** A fast, all-in-one tool for formatting, linting, and import sorting in the frontend. It replaces ESLint and Prettier for a simpler, faster experience.

### Backend Tooling

- **uv:** The project uses `uv`, a high-performance Python package manager written in Rust. It replaces `pip`, `pip-tools`, and `venv` with a single tool that is significantly faster and provides reproducible builds via `uv.lock`.
- **Ruff:** A Rust-based Python linter and formatter. It ensures consistent code style across the backend and provides instant feedback during development.
- **SQLModel:** Combines [SQLAlchemy](https://www.sqlalchemy.org/) and [Pydantic](https://docs.pydantic.dev/) into a single library. This allows us to define database models that are simultaneously Pydantic schemas, ensuring type safety from the database layer all the way to the API response.
- **Hey API (openapi-ts):** Our TypeScript client is 100% auto-generated from the FastAPI OpenAPI schema. This means any backend change is immediately reflected in the frontend's type system after running the generator.

---

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
