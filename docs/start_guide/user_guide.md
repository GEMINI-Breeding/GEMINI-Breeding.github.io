# User Guide

GEMI (short for GxExMINI) is a desktop app for Windows, macOS and Linux. It turns drone flights, rover runs and plot photos into per-plot images and trait measurements. It analyses them alongside field designs and genotype data. An optional AI agent can do the processing for you when you ask.

## Install

Download the installer for your system from the [releases page](https://github.com/GEMINI-Breeding/GEMINI-App/releases) and open GEMI.

If macOS says the app cannot be opened, allow it under *System Settings → Privacy & Security → Open Anyway*.

## Where the processing runs

The heavy work (orthomosaics, stitching, models) runs in a **processing stack**: a database, file storage and workers. GEMI needs one of these:

| Where | What you need | Good for |
|---|---|---|
| **This computer** | [Docker Desktop](https://www.docker.com/products/docker-desktop/) | Small data sets, trying things out |
| **A cluster (HPC)** | A Slurm cluster with Apptainer that you can log in to with an SSH key | Whole fields and seasons |

**On this computer**, GEMI downloads Docker Desktop and opens its installer for you; your system asks you to approve it. On Linux it shows the terminal commands instead. The first start downloads the core services (about 2 GB). The processing workers (about 6 GB more) follow in the background. Altogether the services take about 18 GB. With an NVIDIA graphics card that Docker can use, models run on the card.

**On a cluster**, nothing has to be installed beforehand. Give the agent your SSH login command and it sets GEMI up there, asking before each step that changes something on the cluster. Every action on the cluster goes through one script, confined to GEMI's own folder, with job size limits and a log of every call. Workers stop themselves when no job needs them. A cluster session can be shared with your group.

## First run

A short walkthrough asks three things. Each can be changed later in Settings:

1. **Where the processing runs**: this computer or a cluster.
2. **How you want to work**: with the agent, or by hand. Working by hand needs no language model; every step can be done in the app.
3. **Which model the agent uses** (only with the agent):
    - a free open model on this computer, through [Ollama](https://ollama.com), which GEMI installs for you;
    - a free open model on your cluster's GPUs;
    - a hosted model with an API key (Anthropic Claude, OpenAI or a compatible service).

Then follow the [App Guide](../app_guide/index.md) for each step. Every page also has its own **Help** and guided tour.

## Example data

[Example data sets](https://ucdavis.box.com/s/ts802xlcddyufixfjmeayxwiiz2mxrb9) are available to try the app with.
