# 🔍 Databricks Cluster & Job Monitoring Toolkit

## 📘 Overview

This project provides a set of scripts and utilities to **automatically monitor the health of Databricks clusters and jobs**, detect unresponsive or failed states, and optionally take automated recovery actions like restarting clusters or rerunning failed jobs.

---

## 🚀 Features

- ✅ Check if clusters are running and responsive
- ❌ Detect crashed or unresponsive clusters (e.g., `INTERNAL_ERROR`, driver hangs)
- 🔁 Restart problematic clusters (optional)
- 📊 Monitor job run status (`FAILED`, `SUCCESS`, etc.)
- 🔔 Integrate with alerting tools (Slack, Email, etc.)
- ⏱ Schedule as cron job, Databricks job, or in serverless functions

---

## 🗂 Directory Structure

