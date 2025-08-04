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

# 🧩 Using `dbutils.widgets` for Parameterization in Databricks

## 📘 Overview

Databricks notebooks can accept **runtime parameters** via `dbutils.widgets`, allowing notebooks to be more dynamic and reusable across pipelines, jobs, or manual runs.

---

## 🧠 Why Use Widgets?

- Pass inputs like dates, environment flags, or table names
- Integrate with **job parameters**
- Enable **reusable notebook modules**
- Useful for **testing**, **orchestration**, and **data pipeline logic**

---

## 🛠 Supported Widget Types

| Type         | Description                          | Example Syntax                            |
|--------------|--------------------------------------|-------------------------------------------|
| `text`       | Single-line input                    | `dbutils.widgets.text()`                  |
| `dropdown`   | Select from fixed options            | `dbutils.widgets.dropdown()`              |
| `combobox`   | Text + dropdown                      | `dbutils.widgets.combobox()`              |
| `multiselect`| Multiple selections (string list)    | `dbutils.widgets.multiselect()`           |

---

## ✍️ Example: Creating and Reading Widgets

```python
# Create widgets
dbutils.widgets.text("env", "dev", "Environment")
dbutils.widgets.dropdown("month", "01", [f"{i:02d}" for i in range(1, 13)], "Month")
dbutils.widgets.combobox("country", "US", ["US", "UK", "CA"], "Country")
dbutils.widgets.multiselect("departments", "finance", ["finance", "sales", "hr"], "Departments")

# Read widget values
env = dbutils.widgets.get("env")
month = dbutils.widgets.get("month")
country = dbutils.widgets.get("country")
departments = dbutils.widgets.get("departments").split(",")

print(f"ENV: {env}, MONTH: {month}, COUNTRY: {country}, DEPTS: {departments}")
```
