# 🌞 Solar Challenge Week 0 — Final Report

*By Derese Ewunet*

---

## Introduction

Week 0 of the Solar Challenge was focused on understanding and analyzing solar energy potential across **three West African countries**: Benin, Sierra Leone, and Togo. The goal was to perform a full data science workflow—from raw data acquisition and cleaning to exploratory analysis, cross-country comparison, and an interactive visualization dashboard.

This report summarizes the entire process in a **storytelling style**, similar to what you would see on Medium, blending technical rigor with readable narrative.

---

## Project Objectives

* Assess solar irradiance and temperature patterns in each country
* Perform **country-specific exploratory data analysis (EDA)**
* Conduct **cross-country comparisons**
* Build an **interactive dashboard** to visualize insights
* Prepare the data and workflow for future predictive modeling

---

## Data Overview

The datasets included:

| Country      | Dataset Filename       | Observations |
| ------------ | ---------------------- | ------------ |
| Benin        | benin_clean.csv        | 10,000+      |
| Sierra Leone | sierra_leone_clean.csv | 9,500+       |
| Togo         | togo_clean.csv         | 8,800+       |

**Metrics analyzed:**

* **GHI (Global Horizontal Irradiance)**: Total solar radiation received on a horizontal surface
* **DNI (Direct Normal Irradiance)**: Direct beam radiation
* **DHI (Diffuse Horizontal Irradiance)**: Scattered radiation
* **Temperature**: Ambient temperature

---

## Workflow Summary

### 1. Project Setup

* Initialized **GitHub repository** and Python environment
* Installed dependencies via `requirements.txt`
* Established **CI/CD workflow** with GitHub Actions
* Created structured project directories for notebooks, data, scripts, and the Streamlit app

---

### 2. Country-Specific Exploratory Data Analysis

#### Benin

* **Data Cleaning**: Handled missing values using median imputation
* **Outlier Detection**: Applied Z-score method
* **Visualization**: Time series plots for GHI, DNI, DHI, and temperature
* **Insights**: Highest solar potential observed in northern regions; seasonal patterns clearly visible

#### Sierra Leone

* **Statistical Profiling**: Mean, median, standard deviation calculations
* **Visualization**: Boxplots and distribution plots for all solar metrics
* **Insights**: Coastal regions have higher diffuse radiation, while inland shows stronger direct irradiance

#### Togo

* **Time Series Analysis**: Seasonal decomposition and trend analysis
* **Correlation Analysis**: Observed strong correlation between GHI and temperature
* **Insights**: Southern regions have stable solar exposure, while north shows higher variability

---

### 3. Cross-Country Comparison

* **Comparative Statistics**: Evaluated mean, median, and variance across countries
* **Regional Insights**: Northern Benin and Togo exhibit similar GHI patterns; Sierra Leone shows coastal differences
* **Benchmarking**: Identified top-performing regions for potential solar energy deployment

---

### 4. Interactive Dashboard

* Built using **Streamlit**
* Features:

  * Real-time filtering by country and metric
  * Time series visualizations and boxplots
  * Export charts for reporting
* Available online: [Open Interactive Dashboard](https://solar-challenge-week0-derese-ewunet.streamlit.app/){:target="_blank"}

---

## Key Deliverables

| Component                | Status | Description                         |
| ------------------------ | ------ | ----------------------------------- |
| Benin EDA                | ✅      | Completed                           |
| Sierra Leone EDA         | ✅      | Completed                           |
| Togo EDA                 | ✅      | Completed                           |
| Cross-Country Comparison | ✅     | Completed                        |
| Streamlit Dashboard      | ⏳      | Interactive visualizations deployed |

---

## Lessons Learned

* **Data quality is crucial**: Cleaning and validation significantly improved analysis accuracy
* **Visualization is key**: Patterns became immediately visible through plots
* **Automation matters**: Using a structured workflow and CI/CD pipelines improved reproducibility
* **Collaboration readiness**: Git branching strategies allowed multiple analyses in parallel without conflicts

---

## Conclusion

Week 0 laid the foundation for the Solar Challenge, providing **cleaned datasets**, **insights into solar energy potential**, and an **interactive dashboard** for decision-making. This work serves as the base for **predictive modeling and optimization** in future weeks.

---

## References & Tools

* **Python 3.12**, Pandas, NumPy, Matplotlib, Seaborn
* **Streamlit** for interactive dashboard
* GitHub Actions for CI/CD

---


Made with ❤️ by **Derese Ewunet**
