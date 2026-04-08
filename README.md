# 📊 A/B Testing: Comparison of Bidding Methods

---

## 🧩 Business Problem

Facebook has introduced a new bidding strategy called **"average bidding"** as an alternative to the existing **"maximum bidding"** method.

A client, **bombabomba.com**, wants to evaluate whether this new method leads to **higher conversion rates**.

To achieve this:
- An A/B test has been conducted for **one month**
- The goal is to determine if there is a **statistically significant difference** between the two bidding methods

📌 The key success metric is: **Purchase**

---

## 📁 Dataset Story

The dataset contains **website interaction and performance data**, including user engagement with ads and resulting revenue.

There are two separate groups:
- **Control Group** → Maximum Bidding  
- **Test Group** → Average Bidding  

These datasets are stored in different sheets of the `ab_testing.xlsx` file.

---

## 📌 Variables

| Variable | Description |
|----------|-------------|
| **Impression** | Number of ad impressions |
| **Click** | Number of clicks on ads |
| **Purchase** | Number of purchases after clicks |
| **Earning** | Revenue generated from purchases |

---

## 🎯 Project Objectives

- Compare **conversion performance** between bidding strategies  
- Determine whether the difference is **statistically significant**  
- Support decision-making with **data-driven insights**  

---

## 🛠️ Methodology

- Exploratory data analysis (EDA)  
- Hypothesis testing:
  - **H₀ (Null Hypothesis):** No difference between groups  
  - **H₁ (Alternative Hypothesis):** There is a difference  
- Assumption checks:
  - Normality (Shapiro-Wilk Test)  
  - Homogeneity of variance (Levene Test)  
- Statistical testing:
  - Independent Two-Sample **T-Test** (if assumptions hold)  
  - **Mann-Whitney U Test** (if assumptions are violated)  

---

## 📊 Key Insight

- No statistically significant difference was found between the control and test groups based on the **Purchase** metric.  
- This suggests that **average bidding does not outperform maximum bidding** in terms of conversions.

---

## 🚀 Expected Outcome

- Clear evaluation of bidding strategy performance  
- Data-backed recommendation for marketing optimization  
- Improved decision-making for advertising investments  
