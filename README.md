# 🌱 Plant Harm Monitoring in Lithuania
### Analysis of Agricultural Plant Harm Using Open Data (data.gov.lt)

This project analyzes agricultural plant harm caused by pests and diseases in Lithuania using publicly available open data.  
It fetches the dataset from the Lithuanian Open Data Portal, cleans it, performs exploratory analysis, and visualizes key insights.

---

## 📌 1. Project Overview

Agricultural productivity is affected by various plant diseases and pests.  
This project helps identify:

- Which plant species experience the **highest levels of harm**
- How plant harm **varies over time**
- General trends useful for farming, agriculture research, and environmental monitoring

The analysis supports farmers, agricultural institutions, and policy makers in making data-driven decisions.

---

## 📊 2. Dataset Information

**Source:**  
Lithuanian Open Data Portal (data.gov.lt)  
API URL:  
`https://get.data.gov.lt/datasets/gov/lzukt/Ivertis`

**Key Fields Used:**

| Column Name | Description |
|-------------|-------------|
| `observation_date` | Date of observation |
| `plant_name` | Name of the plant |
| `disease_pest_name` | Specific disease or pest |
| `harm_value` | Numeric harm score |
| `violation_level` | Severity level of plant damage |
| `municipality` | Observation location |

---

## 🛠️ 3. Features

### ✔ Fetch data from API  
Automatic retrieval of JSON data from the open data portal.

### ✔ Data cleaning  
- Column renaming  
- Date parsing  
- Numeric conversion  
- Missing value handling  

### ✔ Analysis functions  
- **Top 5 plants by total harm**
- **Yearly trend of plant harm**

### ✔ Visualizations  
- Horizontal bar chart for top plants  
- Line chart for yearly harm trends  

### Image
<img width="1919" height="1017" alt="Screenshot 2025-11-19 210545" src="https://github.com/user-attachments/assets/5867514e-3b74-45e3-9a58-a682b2e7abaf" />



## 📂 4. Project Structure

