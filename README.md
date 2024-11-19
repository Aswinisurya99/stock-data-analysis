Stock Data Outlier Analysis
Overview
This project provides a streamlined solution for analyzing stock data and identifying outliers. It includes two APIs:
1.	Data Extraction API: Splits stock data into manageable chunks based on customizable filters.
2.	Outlier Detection API: Identifies outliers in stock data using statistical methods.
The project is designed to work with stock data in CSV format and is flexible for various use cases.

Features
•	Extract stock data into smaller, filtered chunks using a RESTful API.
•	Detect statistical outliers in stock price data using a second API.
•	Output processed data to a separate directory for further analysis.
•	Easily extendable and customizable for other datasets.

Technologies Used
•	Language: Python
•	Libraries: Pandas, Flask, Numpy, etc.

Setup Instructions
1. Clone the Repository
git clone <repository_url>
cd stock-data-analysis
2. Install Dependencies
Make sure you have Python 3.8+ installed. Install the required libraries:
pip install -r requirements.txt
3. Run the APIs Locally
Start the Flask server:
python src/api1.py

Project Folder Structure
stock-analysis/
├── data/
│   ├── stock_data_2023.csv
│   ├── stock_data_2022.csv
│   └── ...
├── main.py
├── requirements.txt
├── utils.py
├── .gitignore
└── README.md

API Details
API 1: Data Extraction
•	Endpoint: /extract
•	Method: POST
•	Input: JSON with filters (e.g., date range, stock symbol).
•	Output: Processed CSV files in the output/ folder.

API 2: Outlier Detection
•	Endpoint: /outliers
•	Method: POST
•	Input: JSON with file path and column name for outlier analysis.
•	Output: Updated CSV files with flagged outliers.

Error Handling
•	Input validation ensures the APIs only accept valid data.
•	Proper error messages are returned for missing or incorrect input.

Future Enhancements
•	Add support for additional statistical analysis methods.
•	Integrate with a database for dynamic data retrieval.
•	Deploy APIs using cloud-based solutions (AWS, Azure, GCP).
