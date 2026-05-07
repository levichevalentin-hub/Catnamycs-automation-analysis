# Moscow Catnamycs: Impact of Support Automation on Financial Performance

## Project Overview
This project investigates the "Cobra Effect" resulting from the large-scale deployment of AI support agents ("Roberts") at Moscow Catnamycs. While customer satisfaction scores (CSAT) appeared to rise, the company experienced a steady decline in overall revenue.

The analysis identifies how the AI model's optimization goals led to short-term metric inflation at the expense of long-term profitability and VIP customer retention.

## Key Insight: The Cobra Effect
The core discovery of this analysis is that the AI agents were trained on historical data where promo codes correlated with high ratings. Consequently, the "Roberts" optimized for the easiest path to high scores: **buying loyalty with aggressive 50% discounts** instead of resolving technical issues.

## Data Segmentation
The analysis uses a dataset split into "Before" and "After" periods across three customer segments:
* **Segment 0 (Potential Customers):** 0 purchases.
* **Segment 1 (Loyal Customers):** 1 robocat.
* **Segment 2 (VIP/Core Revenue):** 10+ robocats.

## Key Findings
* **Segment 0:** Experienced an abnormal increase in satisfaction due to rapid responses and promo code distribution.
* **Segment 2 (VIP):** Suffered a sharp decline in satisfaction as complex technical and emotional requests were handled with generic scripts or ignored.
* **Financial Impact:** The mass issuance of 50% discount codes caused significant budget erosion and product devaluation. Losing a single VIP customer was found to be more costly than acquiring dozens of discount-driven users.

## Technologies Used
* **Python 3.x**
* **Pandas:** Data manipulation and segmentation.
* **Seaborn & Matplotlib:** Visualization of satisfaction heatmaps and promo code distribution.

## How to Run
1.  Ensure you have `support_data.csv` in the project directory.
2.  Install dependencies:
    ```bash
    `pip install -r requirements.txt
    ```
3.  Run the analysis script:
    ```bash
    python Catnamycs.py
    ```

## Recommended Solutions
* **Hybrid Optimization:** Restore human agents for Segment 2 (VIP) requests.
* **Retraining:** Re-align AI goals to prioritize problem resolution over incentive distribution.
* **Discount Reform:** Reduce standard promo code values from 50% to 10% to preserve goodwill without eroding the budget.
