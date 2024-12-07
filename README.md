# **🌞 Week 0 Challenge: Solar Farm Data Analysis and Dashboard**

Welcome to the **Week 0 Challenge** for the **10 Academy Artificial Intelligence Mastery (AIM) Program**. This project focuses on analyzing solar farm data from **Benin, Sierra Leone, and Togo** to identify high-potential regions for solar installation and support data-driven investment strategies. 

This repository contains the code, notebooks, and resources for Exploratory Data Analysis (EDA), Data Cleaning, Statistical Analysis, and **a Streamlit Dashboard** that visualizes key insights.

---

## 🚀 **Project Overview**
The goal of this challenge is to act as an **Analytics Engineer** for **MoonLight Energy Solutions** and analyze the environmental data to identify the best regions for solar energy investments. 

The main objectives include:
- **Data Cleaning**: Handle missing values, anomalies, and incorrect data.
- **Exploratory Data Analysis (EDA)**: Extract insights from the data.
- **Statistical Analysis**: Identify correlations, trends, and outliers.
- **Interactive Dashboard**: Use **Streamlit** to create an interactive dashboard for visualizing solar radiation, temperature, and other environmental data.
- **Final Report**: Write a blog-style report summarizing the process, methods, and key findings.

---

## 📂 **Folder Structure**
The repository is structured as follows:
```
├── .vscode/           # VS Code settings
├── .github/workflows/ # CI/CD configuration
├── .gitignore         # Files and folders to be ignored by Git
├── requirements.txt   # List of required Python libraries
├── README.md          # Project description (this file)
├── src/               # Source files for scripts and analysis
├── notebooks/         # Jupyter notebooks for EDA, visualizations, and analysis
├── tests/             # Unit tests for testing scripts
├── scripts/           # Scripts for data cleaning, processing, and analysis
└── app/               # Streamlit dashboard files
    ├── main.py       # Main Streamlit app
    └── utils.py      # Utility functions for Streamlit
```

---

## 💾 **Dataset**
The dataset contains solar radiation measurement data collected from **Benin, Sierra Leone, and Togo**. Key features include:

| **Column Name**  | **Description** |
|-----------------|-----------------|
| `Timestamp`      | Date and time of the observation |
| `GHI`            | Global Horizontal Irradiance (W/m²) |
| `DNI`            | Direct Normal Irradiance (W/m²) |
| `DHI`            | Diffuse Horizontal Irradiance (W/m²) |
| `Tamb`           | Ambient temperature (°C) |
| `RH`             | Relative Humidity (%) |
| `WS`             | Wind Speed (m/s) |
| `WD`             | Wind Direction (degrees) |
| `Precipitation`  | Precipitation rate (mm/min) |
| `Cleaning`       | Indicator of cleaning events (1 = cleaned, 0 = not cleaned) |

> **Note**: The dataset is cleaned and analyzed in the **notebooks** and **scripts** directories.

---

## 📊 **Key Features**
- **Data Cleaning**: Handle missing data, anomalies, and inconsistencies.
- **Exploratory Data Analysis (EDA)**: 
  - Summary statistics (mean, median, standard deviation, etc.)
  - Data quality checks for missing values, duplicates, and incorrect data.
  - Visualizations: time-series, scatter plots, heatmaps, histograms, and wind roses.
  - Correlation analysis of features like GHI, DNI, DHI, and temperature.
- **Statistical Analysis**: 
  - Z-score analysis for outlier detection.
  - Time-series analysis of solar radiation patterns.
- **Streamlit Dashboard**:
  - Interactive widgets (sliders, buttons) for filtering data.
  - Visualizations for GHI, DNI, DHI, temperature, and humidity.
  - Wind analysis (wind roses) for visualizing wind patterns.
- **CI/CD Pipeline**:
  - Automated testing and continuous integration using **GitHub Actions**.

---

## 🛠️ **Setup & Installation**
Follow these instructions to set up the project on your local machine.

1. **Clone the Repository**:
   ```bash
   git clone <your-repo-url>
   cd <your-repo-name>
   ```

2. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Streamlit Dashboard**:
   ```bash
   streamlit run app/main.py
   ```

5. **Run Tests** (optional):
   ```bash
   pytest
   ```

> 📝 **Note**: Make sure to create a `.env` file to manage environment variables if needed (e.g., API keys, dataset paths).

---

## 🧪 **Usage**
### **1. Run EDA Notebooks**
- Navigate to the **notebooks/** folder.
- Open and run the Jupyter notebooks to see the EDA and analysis.

### **2. View Interactive Dashboard**
- Run the command below to start the **Streamlit Dashboard**:
  ```bash
  streamlit run app/main.py
  ```

- Explore the visualizations and interact with the filters, sliders, and buttons to see trends in the data.

---

## ✅ **Deliverables**
Here are the key deliverables for this project:

| **Deliverable**       | **Description**                              |
|----------------------|----------------------------------------------|
| **GitHub Repository** | Full repository with EDA, scripts, and reports |
| **EDA Notebook**      | Analysis, plots, and key insights for the dataset |
| **Streamlit Dashboard**| Deployed dashboard for visualizing solar data |
| **Final Report**      | Blog-style report with process, results, and insights |

---

## 🚀 **Features of the Streamlit Dashboard**
- **Interactive Data Exploration**: View GHI, DNI, and DHI radiation trends.
- **Time-series Analysis**: Filter by date range to see changes over time.
- **Custom Filters**: Use sliders to adjust analysis criteria.
- **Visual Analysis**: Display wind direction (wind roses) and radiation trends.

---

## 📋 **To-Do List**
- [x] Create a GitHub repository.
- [x] Set up the Python environment and dependencies.
- [x] Conduct EDA to understand the data.
- [x] Implement data cleaning methods.
- [x] Build an interactive **Streamlit Dashboard**.
- [x] Write the final blog-style report.
- [x] Submit GitHub link, dashboard URL, and report.

---

## 📅 **Key Dates**
| **Event**             | **Date**           |
|----------------------|--------------------|
| Start Date            | December 6, 2024   |
| Submission Deadline   | December 8, 2024, 8:00 PM UTC |

---

## 🔥 **Technologies Used**
- **Programming Languages**: Python
- **Data Analysis**: Pandas, NumPy, Seaborn, Matplotlib
- **Dashboard**: Streamlit
- **Version Control**: Git, GitHub
- **CI/CD**: GitHub Actions

---

## 🤝 **Contributors**
This project was developed as part of the **10 Academy AIM Program**.

| **Name**        | **Role**           |
|-----------------|-------------------|
| Your Name       | Data Analyst, Developer |
| Facilitators    | Yabebal, Mahlet, Kerod, Rediet, Rehmet |

> **Want to contribute?** Feel free to fork the repo and submit a pull request.

---

## ✍️ **License**
This project is licensed under the **MIT License**. You are free to use, modify, and distribute it as you wish.

---

## 📞 **Contact**
If you have any questions or feedback, please reach out to me via **GitHub Issues** or send a message to the facilitators on the **10 Academy community platform**.

---

With this **descriptive README**, anyone visiting your GitHub repository will immediately understand your project. It includes clear explanations, installation instructions, and a professional layout.

Let me know if you'd like any changes, additions, or customization to this README! 😊
