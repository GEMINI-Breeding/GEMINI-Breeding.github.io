# Developer Guide

Welcome to the GEMINI Breeding developer documentation.

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Desktop shell | [Tauri v2](https://tauri.app) (Rust) |
| Frontend | React 18, [TanStack Router](https://tanstack.com/router), [TanStack Query](https://tanstack.com/query), [shadcn/ui](https://ui.shadcn.com), Tailwind CSS v4 |
| Processing stack | [GEMINIbase](https://github.com/GEMINI-Breeding/GEMINIbase) (the `backend/` submodule): a [Litestar](https://litestar.dev) API, PostgreSQL, MinIO file storage, Redis, TiTiler map tiles, and job workers |
| Workers | OpenDroneMap (orthomosaics), AgRowStitch (rover stitching), farm-ng Amiga SDK (rover logs), detection models, GWAS |
| Where it runs | Docker Compose on one computer, or Slurm jobs with Apptainer images on a cluster |
| Agent | Python (`agent/gemi_agent`), with skills in `agent/skills/`; also usable as an MCP server (`gemi-agent mcp`) |
| API client | Auto-generated from the API's OpenAPI schema via [@hey-api/openapi-ts](https://heyapi.dev) |
| Linting | [Biome](https://biomejs.dev) (frontend), [Ruff](https://docs.astral.sh/ruff/) (backend) |

---

## Development Tools & Ecosystem

GEMINI-App leverages a modern, high-performance toolchain to ensure developer productivity and a polished user experience.

### Frontend Tooling

- **Vite:** The project uses Vite for lightning-fast Hot Module Replacement (HMR) and optimized production builds. In development mode, Vite's proxy forwards requests to the processing stack's API; in production the frontend is bundled into the Tauri desktop shell.
- **Tauri v2:** Provides a lightweight Rust-based bridge between the webview and the operating system. It starts the processing stack (Docker on this computer, or the cluster session over SSH) and the agent service, handles native file dialogs, and manages the desktop window.
- **shadcn/ui & Radix UI:** Instead of a traditional component library, the app uses `shadcn/ui` which provides high-quality, accessible Radix UI primitives that are "owned" by the project (copied into `src/components/ui/`). This allows for full customization of every component.
- **Tailwind CSS v4:** A CSS-first utility framework used for styling. Version 4 provides a high-performance engine and a streamlined development workflow.
- **TanStack Ecosystem:**
    - **TanStack Router:** Provides a type-safe, file-based routing system. This ensures that every URL and parameter is verified at compile-time, reducing runtime errors.
    - **TanStack Query:** Manages all server state, caching, and background synchronization between the frontend and the API.
    - **TanStack Table:** Powering the "Analyze" tab's grid view, this headless library allows for complex filtering, sorting, and pagination of large datasets without sacrificing performance.
- **Biome:** A fast, all-in-one tool for formatting, linting, and import sorting in the frontend. It replaces ESLint and Prettier for a simpler, faster experience.

### Backend Tooling

- **Litestar:** The processing stack's API framework, with typed controllers and an OpenAPI schema.
- **SQLAlchemy and Alembic:** Database models and migrations for PostgreSQL.
- **uv:** Python package manager, with reproducible builds via `uv.lock`.
- **Ruff:** Python linter and formatter.
- **Hey API (openapi-ts):** The frontend's TypeScript client is generated from the API's OpenAPI schema, so a backend change is reflected in the frontend's types after running the generator.

---

## Development Setup

Development has two parts: the **backend** (GEMINIbase), which runs in Docker, and the **frontend**, which runs on your machine. On Windows, run the commands in Git Bash.

| Tool | Version | Needed for |
|---|---|---|
| Git | 2.46 or newer on Windows | Cloning the repo and the backend submodule |
| Docker Desktop (or Docker Engine with Compose v2) | Current | The backend |
| [Node.js](https://nodejs.org) | 22 or newer | The frontend |
| [Rust](https://rustup.rs) (stable) | 1.77 or newer | The desktop window only |
| Python | 3.11 or newer | The agent from source |

```
git clone --recurse-submodules https://github.com/GEMINI-Breeding/GEMINI-App.git &&
cd GEMINI-App &&
./scripts/setup-backend.sh &&
docker compose up -d --build
```

The first build takes 10 minutes or more. `docker compose ps` should then show `rest-api` and `logger` as healthy.

## Starting the App

From the `frontend/` directory, after `npm install`:

- **In a browser** (http://localhost:5173):
  ```
  npm run dev
  ```
- **In the desktop window:**
  ```
  npm run tauri:dev
  ```
- **Backend containers and the browser app together:**
  ```
  npm run dev:full
  ```

Run only one of `npm run dev` and `npm run tauri:dev` at a time; both use port 5173. The development admin account is in `backend/gemini/pipeline/.env`.

The agent from source: `cd agent && python -m gemi_agent serve` (for the app's Agent tab), or `python -m gemi_agent chat` in a terminal.

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

The processing stack keeps its records in **PostgreSQL** and its files in **MinIO** (S3-compatible object storage).

### Database

- **Core tables:** experiments, seasons, sites, populations, lines and accessions, plots, sensors and sensor platforms, traits, datasets, and jobs.
- **Records:** `trait_records` and `sensor_records` are columnar tables, with incrementally maintained views for fast queries in Analyze.
- **Schema management:** Alembic migrations in `backend/alembic/`.

### File layout

Files are stored by experiment, season, site, population, date, platform and sensor:

- **`Raw/`**: uploaded data (images, rover logs, orthomosaics).
- **`Intermediate/`**: derived inputs (plot boundaries, GCP files, synced positions).
- **`Processed/`**: results (orthomosaics, plot images, model predictions, trait files).

*For details, see `docs/` in the [GEMINI-App repository](https://github.com/GEMINI-Breeding/GEMINI-App) and the [GEMINIbase repository](https://github.com/GEMINI-Breeding/GEMINIbase).*
