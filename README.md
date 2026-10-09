# 🌿 Mamaearth Returns & Growth Intelligence Pipeline

## 📌 Overview

This project builds an **end-to-end analytics pipeline** for Mamaearth to identify how product returns impact revenue and business performance.

The pipeline consists of three connected layers:

- 🗄️ **SQL Layer** – Stores and analyzes raw transactional data.
- 🐍 **Python/Pandas Layer** – Cleans the raw data, performs Exploratory Data Analysis (EDA), detects outliers, generates visualizations, and exports verified findings.
- 🤖 **GenAI Layer** – Uses the verified findings to generate a business narrative in the **SCR (Situation–Complication–Resolution)** format using the Gemini API, with a fully offline fallback.

Each layer depends on the output of the previous layer. No layer reports numbers that were not calculated by the previous stage.

---

# 📂 Repository Structure

```text
├── README.md
├── sql/
│   ├── schema.sql
│   ├── seed_data.sql
│   └── reports.sql
├── data/
│   ├── customers.csv
│   ├── products.csv
│   └── orders.csv
├── analysis/
│   ├── clean_and_eda.py
│   └── visualize.py
├── visualizations/
│   ├── return_rate_by_payment.png
│   └── monthly_revenue_trend.png
└── narrator/
    ├── findings.json
    ├── sample_output.txt
    └── generate_narrative.py
```

---

# ⚙️ Software Requirements

- 🐍 Python 3.10 or later
- 🗄️ MySQL Workbench
- 📊 pandas
- 📈 matplotlib
- 🤖 google-genai
- 📂 pathlib

### Install Required Libraries

```bash
pip install pandas matplotlib google-genai
```

---

# 🗄️ Part 1 – SQL

### ✅ Step 1

Open **MySQL Workbench**.

### ✅ Step 2

Run:

```text
sql/schema.sql
```

This creates:

- customers
- products
- orders

### ✅ Step 3

Run:

```text
sql/seed_data.sql
```

### ✅ Step 4

Run:

```text
sql/reports.sql
```

This generates all required SQL reports.

---

# 🐍 Part 2 – Python Data Cleaning & EDA

Run:

```bash
python analysis/clean_and_eda.py
```

This script performs:

- 📥 CSV loading
- 🔍 Data inspection
- ✨ Payment method standardization
- 🧹 Duplicate removal
- 🩹 Missing value imputation
- 💰 Revenue calculation
- 🔄 Revenue reconciliation
- 🚨 Outlier detection
- 📈 Return-rate analysis
- 🎯 Multi-level segmentation
- 🔗 Correlation analysis
- 📅 Monthly revenue analysis

At the end of execution, the script automatically creates:

```text
narrator/findings.json
```

---

# 📊 Part 2 – Visualizations

Run:

```bash
python analysis/visualize.py
```

Generated files:

```text
visualizations/
├── return_rate_by_payment.png
└── monthly_revenue_trend.png
```

---

# 🤖 Part 3 – GenAI Insight Narrator

Run:

```bash
python narrator/generate_narrative.py
```

The script loads:

```text
narrator/findings.json
```

and generates an SCR business narrative.

---

# 🔑 Using Gemini API

This project supports **two modes**:

- 🌐 **Online Mode** – Uses the Gemini API.
- 💻 **Offline Mode** – Uses the built-in fallback template.

## ☁️ Option 1 – Google Colab (Recommended)

### Step 1 – Get a Free API Key

1. Open **Google AI Studio**.
2. Sign in with your Google account.
3. Click **Get API Key**.
4. Create a new API key.
5. Copy the API key.

> 💡 Google AI Studio provides a **free Gemini API key** with a free usage tier.

### Step 2 – Add the API Key in Google Colab

1. Open your notebook.
2. Click the **🔑 Secrets** icon.
3. Click **+ Add new secret**.

| Field | Value |
|-------|-------|
| **Name** | `APIkey` |
| **Value** | Paste your Gemini API key |

4. Enable **Notebook access**.

### Step 3 – Run the Narrator

```bash
python narrator/generate_narrative.py
```

✅ If the API key is available, Gemini generates the report.

⚠️ If the API key is missing or invalid, the script automatically switches to the offline mode.

---

## 💻 Option 2 – Local Computer

Set the environment variable.

**Windows CMD**

```cmd
set GEMINI_API_KEY=YOUR_API_KEY
```

**PowerShell**

```powershell
$env:GEMINI_API_KEY="YOUR_API_KEY"
```

**macOS/Linux**

```bash
export GEMINI_API_KEY=YOUR_API_KEY
```

Then run:

```bash
python narrator/generate_narrative.py
```

---

# 🌐 Offline Mode

If no API key is available, the script automatically uses the offline fallback.

✔ No API key required

✔ No internet required

✔ Deterministic output

✔ Uses only verified findings

---

# ✅ Numeric Accuracy Check

The script verifies that the narrative contains:

- 💰 Cleaned revenue
- 💳 COD return rate
- 🎯 Highest-risk segment
- 🔄 Duplicate reconciliation delta
- 📅 True peak month revenue

A PASS/FAIL result is displayed for each value.

---

# 📁 Output Files

```text
visualizations/
├── return_rate_by_payment.png
└── monthly_revenue_trend.png

narrator/
├── findings.json
└── sample_output.txt
```

---

# 🔄 Pipeline Summary

```text
SQL Database
      │
      ▼
schema.sql
      │
      ▼
seed_data.sql
      │
      ▼
reports.sql
      │
      ▼
CSV Files
      │
      ▼
analysis/clean_and_eda.py
      │
      ▼
narrator/findings.json
      │
      ▼
analysis/visualize.py
      │
      ▼
Visualization PNGs
      │
      ▼
narrator/generate_narrative.py
      │
      ▼
SCR Business Narrative
```

---

# 👤 Submission Details

**Capstone Project**

🌿 **Mamaearth Returns & Growth Intelligence Pipeline**

**Submitted By**

*Pooja Agarwal*

**Program**

🎓 Data Analytics with AI & Gen AI  
E&ICT Academy, IIT Roorkee
