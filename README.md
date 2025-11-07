# 🌞 Solar Challenge Week 0 Dashboard

![Python](https://img.shields.io/badge/python-3.12-blue?style=flat-square)
![Status](https://img.shields.io/badge/status-active-success?style=flat-square)
![Contributions](https://img.shields.io/badge/contributions-welcome-brightgreen?style=flat-square)

---

## 📌 Table of Contents

* [🚀 Live Demo](#-live-demo)
* [📋 Project Overview](#-project-overview)
* [🛠️ Quick Start](#-quick-start)
* [📂 Project Structure](#-project-structure)
* [🛠️ Development Workflow](#-development-workflow)
* [📈 Analysis Features](#-analysis-features)
* [🔄 Git Workflow & Branch Strategy](#-git-workflow--branch-strategy)
* [⚙️ Continuous Integration](#-continuous-integration)
* [🎯 Key Deliverables](#-key-deliverables)
* [📊 Data Metrics](#-data-metrics)
* [🤝 Contributing](#-contributing)

---

## 🚀 Live Demo

🔗 [Open Interactive Dashboard](https://solar-challenge-week0-derese-ewunet.streamlit.app/){:target="_blank"}

---

## 📋 Project Overview

<details>
<summary>Click to expand Project Overview</summary>

**Solar Challenge Week 0** is a full-stack data science project exploring solar energy potential across **Benin, Sierra Leone, and Togo**.

**Highlights**:

* Data profiling & cleaning
* Country-specific exploratory analysis
* Cross-country comparison
* Interactive Streamlit dashboard

</details>

---

## 🛠️ Quick Start

<details>
<summary>Click to expand Quick Start Instructions</summary>

### Prerequisites

* Python 3.11+
* Git & GitHub account

### Installation

```bash
# Clone repository
git clone https://github.com/DE143/solar-challenge-week0.git
cd solar-challenge-week0

# Create & activate virtual environment
python -m venv venv
# Windows
venv\Scripts\activate

# Upgrade pip and install dependencies
pip install --upgrade pip
pip install -r requirements.txt
```

</details>

---

## 📂 Project Structure

<details>
<summary>Click to expand Project Structure</summary>

```
solar-challenge-week0/
├── 📊 notebooks/          # Jupyter notebooks for analysis
│   ├── benin_eda.ipynb
│   ├── sierra_leone_eda.ipynb
│   ├── togo_eda.ipynb
│   └── compare_countries.ipynb
├── 🔧 scripts/            # Utility scripts
├── 🎯 app/                # Streamlit dashboard
│   ├── main.py
│   └── utils.py
├── 📈 data/               # Raw & processed datasets
├── 🧪 tests/              # Test suites
├── ⚙️ .github/workflows/  # CI/CD pipelines
└── 📄 requirements.txt    # Dependencies
```

</details>

---

## 🛠️ Development Workflow

<details>
<summary>Click to expand Workflow</summary>

### Phase 1: Setup ✅

* Repository initialization
* Python environment configuration
* CI/CD pipeline setup
* Project structure creation

### Phase 2: Country-Specific EDA 🔍

* **Benin**: Complete data exploration & cleaning
* **Sierra Leone**: Statistical profiling & visualization
* **Togo**: Time series & correlation analysis

### Phase 3: Cross-Country Comparison 📊

* Comparative statistics
* Regional insights
* Performance benchmarking

### Phase 4: Interactive Dashboard 🎯 *(Optional)*

* Real-time visualization
* Interactive filters
* Export-ready charts

</details>

---

## 📈 Analysis Features

<details>
<summary>Click to expand Analysis Features</summary>

### Data Processing

* Missing value handling (median imputation)
* Outlier detection (Z-score)
* Data validation & quality checks

### Statistical Analysis

* Descriptive stats (mean, median, SD)
* Correlation heatmaps
* Time series decomposition
* Distribution analysis

### Visualization

* Time series plots (GHI, DNI, DHI, Temperature)
* Comparative boxplots
* Streamlit interactive dashboards
* Export-ready charts

</details>

---

## 🔄 Git Workflow & Branch Strategy

<details>
<summary>Click to expand Git Workflow</summary>

**Branch Naming Convention**

```
feature/description    # New features
eda/country-name       # EDA
fix/description        # Bug fixes
docs/description       # Documentation
```

**Example**

```bash
# Create branch
git checkout -b eda/benin-analysis

# Commit changes
git add notebooks/benin_eda.ipynb
git commit -m "feat: add GHI time series analysis for Benin"

# Push & open PR
git push origin eda/benin-analysis
```

</details>

---

## ⚙️ Continuous Integration

<details>
<summary>Click to expand CI</summary>

* Python 3.12 ✅
* Dependency resolution ✅
* Code integrity checks ✅
* Automated tests ✅

![CI](https://github.com/DE143/solar-challenge-week0/actions/workflows/ci.yml/badge.svg)

</details>

---

## 🎯 Key Deliverables

<details>
<summary>Click to expand Deliverables</summary>

| Component                | Status | Description                   |
| ------------------------ | ------ | ----------------------------- |
| Benin EDA                | ✅      | Complete exploratory analysis |
| Sierra Leone EDA         | ✅      | Statistical profiling         |
| Togo EDA                 | ✅      | Correlation & time series     |
| Cross-Country Comparison | 🔄     | Comparative insights          |
| Streamlit Dashboard      | ⏳      | Interactive visualization     |

</details>

---

## 📊 Data Metrics

<details>
<summary>Click to expand Metrics</summary>

* **GHI**: Global Horizontal Irradiance
* **DNI**: Direct Normal Irradiance
* **DHI**: Diffuse Horizontal Irradiance
* **Temperature**: Ambient temperature
* **Time Series**: Temporal patterns & seasonality

</details>

---

## 🤝 Contributing

<details>
<summary>Click to expand Contribution Guidelines</summary>

**Steps to Contribute:**

1. Fork the repo
2. Create a feature branch:

```bash
git checkout -b feature/amazing-feature
```

3. Commit changes:

```bash
git commit -m "feat: add amazing feature"
```

4. Push & open PR:

```bash
git push origin feature/amazing-feature
```

**Commit Message Convention**

```
init:      Initial setup
feat:      New feature
fix:       Bug fix
docs:      Documentation
chore:     Maintenance
```

</details>

---

Made with ❤️ by **Solar Challenge Contributors**
