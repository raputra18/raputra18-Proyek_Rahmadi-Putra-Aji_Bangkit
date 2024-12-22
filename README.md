# Bike Sharing Dashboard ✨

## Project Overview
This project aims to analyze and visualize the factors affecting bike sharing rentals, including weather, temperature, workday, and seasonality. The goal is to understand the relationship between these factors and bike rentals, providing valuable insights for bike-sharing services.

### Key Insights:
- The weather affects bike rentals, with lower rentals during bad weather (e.g., rain or fog).
- Higher temperatures correlate with increased bike rentals.
- Bike rentals are higher on workdays compared to weekends.
- Summer has the highest bike rental numbers, indicating a strong seasonal effect.

## Setup Environment - Anaconda
To set up the environment using Anaconda, follow these steps:

1. Create a new conda environment:
   ```bash
   conda create --name bike-dashboard python=3.8
2. Activate the virtual environment:
   ```bash
   conda activate bike-dashboard
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt

## Requirements
Ensure the following Python libraries are installed:

- matplotlib==3.7.5
- pandas==2.0.3
- seaborn==0.11.0
- streamlit==1.40.1

## Running the Streamlit App
To run the Streamlit app, execute the following command:
- ```bash
   streamlit run app.py
This will launch the dashboard in your browser.

## Dataset
This project uses two datasets for analysis:

1. day.csv: Contains daily bike rental data, including weather conditions, temperature, humidity, etc.
2. hour.csv: Contains hourly bike rental data with similar features.

## Project Files
- app.py: This file contains the main logic for the Streamlit dashboard. It includes data loading, data cleaning, and visualizations of how different factors (weather, temperature, workday, season, etc.) impact bike rental numbers.
- notebook.ipynb: The Jupyter notebook includes detailed analysis of the data, including Exploratory Data Analysis (EDA) and insights into how weather, temperature, and other factors correlate with bike rentals.
- requirements.txt: This file lists the Python dependencies required to run the project.

## Data Cleaning and Analysis Process
- Data Cleaning:
Unnecessary columns are dropped (e.g., instant).
Missing values are filled with the mean of the respective column.
- Exploratory Data Analysis (EDA):
Visualizations are used to analyze the distribution of bike rentals, weather, temperature, and other factors.
Correlation analysis helps in understanding relationships between numerical variables.
- Visualization:
A variety of plots are used, including boxplots, scatterplots, and heatmaps, to visually assess the impact of factors like weather, temperature, and workday on bike rentals.

## Example Visualizations
- Impact of Weather on Bike Rentals: Boxplot showing bike rentals across different weather conditions.
- Temperature vs. Bike Rentals: Scatterplot illustrating the relationship between temperature and bike rentals.
- Bike Rentals on Workdays vs. Weekends: Boxplot comparing rentals on workdays and weekends.
- Seasonal Impact on Bike Rentals: Boxplot showing the variation in bike rentals across different seasons.

## Running the Analysis Locally
1. Install all dependencies using the setup instructions above.
2. Run the Streamlit app:
   ```bash
   streamlit run app.py
3. Open the provided URL in your browser to interact with the dashboard.

## Conclusion
The analysis reveals key trends, such as how weather and temperature impact bike rentals. By understanding these trends, bike-sharing companies can better plan for peak times and improve their services.

Feel free to explore and modify the project to gain further insights or test other hypotheses.

## Contact
- Name: Rahmadi Putra Aji
- Email: m008b4ky3624@bangkit.academy
- ID Dicoding: raputra
