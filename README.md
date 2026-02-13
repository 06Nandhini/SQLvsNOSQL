# SQL vs NoSQL Analytics: Performance Evaluation

## Project Overview
This project compares **SQL and NoSQL databases** in performing analytics on **structured** (CSV) and **semi-structured** (JSON) data. It evaluates performance in terms of execution time and query efficiency.

## Folder Structure
- `data/` - Datasets (CSV for structured, JSON for semi-structured)
- `sql/` - SQL scripts and Python scripts for analytics
- `nosql/` - Python scripts for NoSQL analytics (MongoDB)
- `results/` - Performance metrics and charts

## Dependencies
Python libraries:
pandas
pymongo
sqlite3


Install with:
```bash
pip install pandas pymongo
How to Run
SQL Analytics

python sql/sql_performance.py
NoSQL Analytics

python nosql/insert_data.py
python nosql/analytics_queries.py
python nosql/nosql_performance.py
