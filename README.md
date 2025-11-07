# 🌞 Solar Challenge Week 0

![Python](https://img.shields.io/badge/python-3.12-blue?style=flat-square)
![Status](https://img.shields.io/badge/status-active-success?style=flat-square)
![Contributions](https://img.shields.io/badge/contributions-welcome-brightgreen?style=flat-square)

---

## 🚀 Live Demo

🔗 [Open Interactive Dashboard](https://solar-challenge-week0-derese-ewunet.streamlit.app/){:target="_blank"}

---

## 📋 Project Overview

**Solar Challenge Week 0** is a complete data science project exploring solar energy potential across **Benin, Sierra Leone, and Togo**.
This repository demonstrates an **end-to-end workflow** from data cleaning and exploratory analysis to interactive visualization.

Key Highlights:

* Data profiling and cleaning
* Country-specific exploratory analysis
* Cross-country comparison
* Interactive Streamlit dashboard

---

## 🛠️ Quick Start

### Prerequisites

* Python 3.11+
* Git & GitHub account

### Installation & Setup

```bash
# Clone the repository
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

---

## 📂 Project Structure

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
├── 📈 data/               # Raw and processed datasets
├── 🧪 tests/              # Test suites
├── ⚙️ .github/workflows/  # CI/CD pipelines
└── 📄 requirements.txt    # Project dependencies
```

---

## 🛠️ Development Workflow

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

* Real-time data visualization
* Interactive filtering
* Export-ready charts

---

## 📈 Analysis Features

### Data Processing

* Missing value handling (median imputation)
* Outlier detection (Z-score)
* Data validation & quality checks

### Statistical Analysis

* Descriptive statistics (mean, median, SD)
* Correlation heatmaps
* Time series decomposition
* Distribution analysis

### Visualization

* Time series plots (GHI, DNI, DHI, Temperature)
* Comparative boxplots
* Streamlit interactive dashboards
* Export-ready charts

---

## 🔄 Git Workflow & Branch Strategy

**Branch Naming Convention**

```
feature/description    # New features
eda/country-name       # Exploratory data analysis
fix/description        # Bug fixes
docs/description       # Documentation updates
```

**Example Workflow**

```bash
# Create branch
git checkout -b eda/benin-analysis

# Commit often
git add notebooks/benin_eda.ipynb
git commit -m "feat: add GHI time series analysis for Benin"

# Push & open PR
git push origin eda/benin-analysis
```

---

## ⚙️ Continuous Integration

* Python 3.12 compatibility ✅
* Dependency resolution ✅
* Code integrity checks ✅
* Automated tests readiness ✅

![CI](https://github.com/DE143/solar-challenge-week0/actions/workflows/ci.yml/badge.svg)

---

## 🎯 Key Deliverables

| Component                | Status | Description                   |
| ------------------------ | ------ | ----------------------------- |
| Benin EDA                | ✅      | Complete exploratory analysis |
| Sierra Leone EDA         | ✅      | Statistical profiling         |
| Togo EDA                 | ✅      | Correlation & time series     |
| Cross-Country Comparison | 🔄     | Comparative insights          |
| Streamlit Dashboard      | ⏳      | Interactive visualization     |

---

## 📊 Data Metrics

* **GHI**: Global Horizontal Irradiance
* **DNI**: Direct Normal Irradiance
* **DHI**: Diffuse Horizontal Irradiance
* **Temperature**: Ambient temperature
* **Time Series**: Temporal patterns & seasonality

---

## 🤝 Contributing

We welcome contributions!

**Steps to Contribute:**

1. Fork the repository
2. Create a feature branch:

   ```bash
   git checkout -b feature/amazing-feature
   ```
3. Commit your changes:

   ```bash
   git commit -m "feat: add amazing feature"
   ```
4. Push & open a PR:

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

---

Made with ❤️ by **Derese Ewunet**
