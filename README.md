#  Customer_Shopping_Behavior Analysis

##  Overview
This project analyzes consumer shopping patterns to generate data-driven business insights.  

The workflow covers:
- Data cleaning & transformation in Python  
- Advanced querying in PostgreSQL  
- Interactive dashboard development in Power BI  

The goal is to demonstrate end-to-end analytics capability — from raw data to business insights.


##  Dataset
**File:** `customer_shopping_behavior.csv`  
**Records:** 3,900 transactions  

Includes:
- Demographics (Age, Gender, Location)
- Purchase details (Amount, Category, Frequency)
- Loyalty indicators (Subscription, Previous Purchases, Ratings)
- Logistics (Shipping Type, Payment Method, Discounts)


##  Tools Used
- **Python:** Pandas, SQLAlchemy  
- **PostgreSQL:** Data storage & querying  
- **SQL:** Joins, CTEs, Window Functions  
- **Power BI:** Dashboard visualization  


##  Project Highlights

### Data Processing
- Performed EDA and handled missing values  
- Standardized data types  
- Loaded cleaned data into PostgreSQL  

### SQL Analysis
- Revenue segmentation by gender  
- Customer classification (New, Returning, Loyal)  
- Ranked top products using window functions  
- Analyzed loyalty vs subscription behavior  

### Power BI Dashboard
- KPI cards (Revenue, AOV, Ratings)  
- Revenue comparison by gender  
- Product & category performance insights  


##  Key Insights
- Identified high-revenue customer segments  
- Evaluated shipping type impact on spending  
- Highlighted retention opportunities for returning customers  


##  How to Run

```bash
pip install pandas sqlalchemy psycopg2

1. Run the notebook to clean & load data into PostgreSQL  
2. Execute SQL queries  
3. Open `customer_behavior_dashboard.pbix` in Power BI


## Skills Demonstrated
Data Cleaning • ETL • Advanced SQL • Customer Segmentation • BI Dashboarding 
