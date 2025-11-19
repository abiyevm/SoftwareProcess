# 🌱 Plant Harm Monitoring in Lithuania
### An Analysis of Plant Damage Using Open Data

This project is part of my **Software Process class assignment**, where I was tasked with selecting a real-world problem and analyzing it using publicly available data. I chose to investigate agricultural plant health in Lithuania and explore how different plant species are affected by pests and diseases.  

I gathered data from the official **Lithuanian Open Data Portal**, cleaned and analyzed it using Python, and created visualizations to better understand plant harm patterns.

---

## 📌 Why I Chose This Topic

Agriculture plays a vital role in Lithuania, and plant damage caused by pests and diseases can have significant impacts on crop yields. I wanted to answer questions like:

- Which plant species are most affected by pests and diseases?  
- How does overall plant harm change over time?  
- What insights can I derive from open government data?  

This assignment gave me the chance to work with **real-world messy datasets** and practice data cleaning, analysis, and visualization.

---

## 📊 Dataset Used

I used a dataset from the **Lithuanian Open Data Portal (data.gov.lt)**:  
API endpoint: `https://get.data.gov.lt/datasets/gov/lzukt/Ivertis`

The dataset contains field observations of plant diseases and pests. Some of the main fields I focused on were:

| Column | Description |
|--------|----------------|
| `observation_date` | Date when the observation was recorded |
| `plant_name` | Name of the plant |
| `disease_pest_name` | Pest or disease identified |
| `harm_value` | Numeric value representing the severity of damage |
| `municipality` | Location of the observation |

---

## 🛠️ What I Did

### 1. Data Collection
I used Python’s `requests` library to fetch the dataset directly from the API in JSON format.

### 2. Data Cleaning and Preparation
I cleaned the data by:

- Renaming columns for readability  
- Converting observation dates into proper datetime format  
- Converting `harm_value` to numeric  
- Removing rows with missing essential values  

This step ensured the data was ready for analysis.

### 3. Data Analysis
I implemented functions to:

- Identify the **Top 5 plants by total harm value**  
- Analyze the **yearly trend of total plant damage**  

This helped me quantify which plants were most affected and how damage changed over time.

### 4. Visualization
Using **Matplotlib** and **Seaborn**, I created:

- A bar chart showing the plants with the highest total harm  
- A line chart showing trends in plant damage over the years  

These visualizations made the data easier to interpret and communicate.

### Image
<img width="1919" height="1017" alt="Screenshot 2025-11-19 210545" src="https://github.com/user-attachments/assets/38505a72-b0bf-489e-aea4-3877889435e8" />



