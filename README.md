# ETL Pipeline – JSONPlaceholder Users API

## 📌 Project Overview

This project implements a **clean and modular ETL (Extract, Transform, Load) pipeline** using Python.  
The pipeline fetches user data from a public REST API, validates and cleans the data, and stores the processed output for further analysis.

The project focuses on **core data engineering fundamentals**:
- API data extraction
- Data validation
- Modular pipeline design
- Clean separation of concerns

this is the user db


## 🏗️ Pipeline Architecture

JSONPlaceholder API
↓
Extract (API Fetch)
↓
Validate (Data Quality Rules)
↓
Transform (Clean Structure)
↓
Load (CSV / Local Storage)

yaml
Copy code

---

## 🔗 Data Source

- **API**: https://jsonplaceholder.typicode.com/users  
- **Format**: Nested JSON  
- **Records**: 10 demo users  
- **Note**: This is a public mock API used for learning and testing

---

## 📂 Project Structure

Assignment_2/
│
├── pipeline.py # Pipeline orchestrator
├── extract.py # API extraction logic
├── validate.py # Data validation rules
├── transform.py # Data cleaning & restructuring
├── data/ # Output files (CSV)
├── README.md
└── .gitignore

yaml
Copy code

---

## ⚙️ Technologies Used

- **Python 3**
- **Requests** – API communication
- **CSV / File System** – Data storage
- **Virtual Environment** – Dependency isolation

---

## ✅ Data Validation Rules

The pipeline validates each user record before further processing.

| Rule | Action |
|-----|-------|
| Missing required fields | Reject record |
| Invalid email format | Reject record |
| Empty name or username | Reject record |
| Invalid nested address data | Reject record |

Invalid records are **excluded**, ensuring only clean data is stored.

---

## 🔄 Transformation Highlights

- Flattens nested JSON structures (address, company)
- Extracts only relevant fields
- Produces a clean, tabular structure suitable for analytics
- Removes unused or inconsistent attributes

---

## 📁 Output

- **Cleaned CSV file** containing validated user data
- File is generated automatically when the pipeline runs

Example output fields:
- user_id
- name
- username
- email
- city
- company_name

this is the user data
![User Data](images/insights.png)

## ▶️ How to Run the Project

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/shreyapandey-ai/Assignment_2.git
cd Assignment_2
2️⃣ Create Virtual Environment
bash
Copy code
python3 -m venv venv
source venv/bin/activate
3️⃣ Install Dependencies
bash
Copy code
pip install requests
4️⃣ Run the Pipeline
bash
Copy code
python3 pipeline.py
🧪 Sample Console Output
yaml
Copy code
Fetching data from API...
Total records fetched: 10
Valid records: 10
Invalid records: 0
Pipeline execution completed successfully.
🧠 Key Design Decisions
Modular ETL structure (Extract / Validate / Transform)

Fail-fast approach if API fetch fails

Explicit validation instead of trusting API data

Easy extensibility for database or analytics integration

🎯 Use Cases
ETL pipeline demonstration

Data engineering fundamentals

API data ingestion practice

Portfolio project

📌 Notes
Uses a public demo API (data is synthetic)

Designed for clarity and correctness

Can be extended to include SQLite, Pandas, and SQL analytics

👤 Author
Shreya Pandey
GitHub: https://github.com/shreyapandey-ai

📝 License
This project is for educational and assignment purposes only.
