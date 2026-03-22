# Comparison of Bidding Methods Conversion Using A/B Testing

## Business Problem

Facebook has recently introduced a new bidding type called **"average bidding"** as an alternative to the existing **"maximum bidding"** method. One of our clients, **bombabomba.com**, has decided to test this new feature and wants to conduct an A/B test to determine whether average bidding generates more conversions than maximum bidding.

The A/B test has been running for one month, and bombabomba.com now expects you to analyze the results. The ultimate success metric for bombabomba.com is **Purchase**. Therefore, statistical analyses should focus on the **Purchase** metric.

## Dataset Story

This dataset contains website interaction data of a company, including metrics such as the number of ads users view and click, as well as the revenue generated from these interactions.

There are two separate datasets: **Control Group** and **Test Group**. These datasets are located on different sheets of the `ab_testing.xlsx` file.

- **Maximum Bidding** was applied to the Control Group  
- **Average Bidding** was applied to the Test Group  

### Variables

- **Impression** : Number of ad impressions  
- **Click** : Number of clicks on displayed ads  
- **Purchase** : Number of products purchased after clicking ads  
- **Earning** : Revenue generated from purchases  
