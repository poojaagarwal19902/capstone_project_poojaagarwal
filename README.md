# 🌿 Mamaearth Returns & Growth Intelligence Pipeline

An end-to-end Data Analytics Capstone Project that combines **SQL**, **Python (Pandas & Matplotlib)**, and **Generative AI (Gemini)** to analyze customer returns, identify business risks, and generate an executive business narrative.

---

# 📋 Project Overview

This project was developed to analyze how product returns affect Mamaearth's revenue and business performance.

The complete pipeline consists of three connected layers:

- 🗄 **SQL Layer** – Stores and analyzes raw order data.
- 🐍 **Python Layer** – Cleans data, performs EDA, identifies trends, and generates visualizations.
- 🤖 **GenAI Layer** – Generates an executive business report using the SCR (Situation–Complication–Resolution) framework.

Each layer depends on the verified output of the previous layer, ensuring complete consistency throughout the project.

---

# 📂 Repository Structure

```
Mamaearth_Returns_Growth_Intelligence/
│
├── README.md
│
├── sql/
│   ├── schema.sql
│   ├── seed_data.sql
│   └── reports.sql
│
├── data/
│   ├── customers.csv
│   ├── products.csv
│   └── orders.csv
│
├── analysis/
│   ├── clean_and_eda.py
│   └── visualize.py
│
├── visualizations/
│   ├── return_rate_by_payment.png
│   └── monthly_revenue_trend.png
│
└── narrator/
    ├── findings.json
    ├── sample_output.txt
    └── generate_narrative.py
```

---

# 🛠 Technologies Used

| Technology | Purpose |
|------------|---------|
| MySQL | Database Management |
| SQL | Data Storage & Reporting |
| Python | Data Analysis |
| Pandas | Data Cleaning & Analysis |
| Matplotlib | Data Visualization |
| Google Gemini API | AI Narrative Generation |
| JSON | Data Exchange |
| Git & GitHub | Version Control |

---

# ⚙️ Software Requirements

- Python 3.10 or above
- MySQL Workbench

### Install Required Python Libraries

```bash
pip install pandas matplotlib google-genai
```

---

# 🚀 Project Workflow

```
Raw CSV Files
      │
      ▼
SQL Database
      │
      ▼
SQL Reports
      │
      ▼
Python Data Cleaning
      │
      ▼
Exploratory Data Analysis
      │
      ▼
Visualizations
      │
      ▼
findings.json
      │
      ▼
Gemini / Offline Narrator
      │
      ▼
Business SCR Report
```

---

# 🗄 Part 1 – SQL Layer

### Step 1 – Create Database Tables

Run:

```text
sql/schema.sql
```

This creates the following tables:

- customers
- products
- orders

---

### Step 2 – Load Data

Run:

```text
sql/seed_data.sql
```

This inserts all customer, product, and order records.

---

### Step 3 – Generate SQL Reports

Run:

```text
sql/reports.sql
```

The report includes:

- Order Totals
- COUNT(*) vs COUNT(column)
- LEFT JOIN
- GROUP BY + HAVING
- Ranking (LIMIT/OFFSET)
- Three-table JOIN
- LIKE
- DISTINCT
- ALTER TABLE + UPDATE

---

# 🐍 Part 2 – Python Data Cleaning & Analysis

Run:

```bash
python analysis/clean_and_eda.py
```

This script performs:

- CSV Loading
- Data Inspection
- Payment Method Standardization
- Duplicate Detection & Removal
- Missing Value Imputation
- Revenue Calculation
- Revenue Reconciliation
- Outlier Detection
- Return Rate Analysis
- Customer Segmentation
- Correlation Analysis
- Monthly Revenue Analysis

At the end of execution, the script automatically creates:

```
narrator/findings.json
```

This JSON file stores all verified metrics used in the GenAI layer.

---

# 📊 Visualizations

Run:

```bash
python analysis/visualize.py
```

Generated files:

- `visualizations/return_rate_by_payment.png`
- `visualizations/monthly_revenue_trend.png`

---

# 🤖 Part 3 – GenAI Insight Narrator

Run:

```bash
python narrator/generate_narrative.py
```

The script:

- Loads `narrator/findings.json`
- Generates an SCR business narrative
- Validates all required numerical values
- Saves the generated narrative as `narrator/sample_output.txt`

---

# 🔑 Gemini API Setup

A free API key can be obtained from **Google AI Studio**.

Set the environment variable before running the narrator.

### Windows Command Prompt

```cmd
set GEMINI_API_KEY=YOUR_API_KEY
```

### Windows PowerShell

```powershell
$env:GEMINI_API_KEY="YOUR_API_KEY"
```

### macOS / Linux

```bash
export GEMINI_API_KEY=YOUR_API_KEY
```

After setting the API key, run:

```bash
python narrator/generate_narrative.py
```

---

# 💻 Offline Mode

If no Gemini API key is configured, or the API request fails, the project automatically switches to the offline narrative generator.

The offline mode:

- Requires no API key
- Requires no internet connection
- Produces deterministic output
- Uses only verified values from `findings.json`

---

# ✅ Numeric Accuracy Validation

The generated narrative is automatically checked to ensure it contains:

- ✔ Cleaned Total Revenue
- ✔ COD Return Rate
- ✔ Highest-Risk Segment Return Rate
- ✔ Duplicate Reconciliation Delta
- ✔ True Peak Month Revenue

A PASS/FAIL result is displayed for every required value.

---

# 📁 Generated Outputs

After running the project successfully, the following files are generated:

```
visualizations/
│
├── return_rate_by_payment.png
└── monthly_revenue_trend.png

narrator/
│
├── findings.json
└── sample_output.txt
```

---

# ▶️ Execution Order

Run the project in the following order:

```
1. sql/schema.sql

2. sql/seed_data.sql

3. sql/reports.sql

4. python analysis/clean_and_eda.py

5. python analysis/visualize.py

6. python narrator/generate_narrative.py
```

Following this sequence ensures that each stage receives the verified output from the previous stage.

---

# 📌 Submission Details

**Capstone Project**: Mamaearth Returns & Growth Intelligence Pipeline
**Submitted by:** : Pooja Agarwal

**Data Analytics with AI & Gen AI**

**E&ICT Academy, IIT Roorkee**
