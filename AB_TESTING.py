#####################################################
# Data Preparation and Analysis
#####################################################

import itertools
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.stats.api as sms
from scipy.stats import ttest_1samp, shapiro, levene, ttest_ind, mannwhitneyu, \
    pearsonr, spearmanr, kendalltau, f_oneway, kruskal
from statsmodels.stats.proportion import proportions_ztest
pd.set_option("display.max_columns", None)
pd.set_option("display.expand_frame_repr", False)
pd.set_option("display.max_rows", 10)
pd.set_option("display.float_format", lambda x: "%.5f" % x)

df_control = pd.read_excel("Measurement Problems/Ödev/ab_testing.xlsx", sheet_name="Control Group")
df_test = pd.read_excel("Measurement Problems/Ödev/ab_testing.xlsx", sheet_name="Test Group")

df_control.describe().T
df_test.describe().T

df_control.groupby("Purchase")[["Impression", "Click", "Earning"]].mean()
df_test.groupby("Purchase")[["Impression", "Click", "Earning"]].mean()


# After the analysis, combining the control and test group datasets using the concat method.

df_control["group"] = "control"
df_test["group"] = "test"

df = pd.concat([df_control, df_test], axis=0, ignore_index=True)

df


#####################################################
# Defining the Hypothesis of the A/B Test
#####################################################

# H0: M1 = M2 (Reject H0 if p < 0.05)
# H1: M1 ≠ M2

# Analyzing the average Purchase (revenue) values for the control and test groups.

df.groupby("group")["Purchase"].mean()


#####################################################
# Performing the Hypothesis Test
#####################################################

# H0: Data follows a normal distribution (if p < 0.05 → not normal)
# H0: Variances are homogeneous (if p < 0.05 → not homogeneous)

test_stat, pvalue = shapiro(df.loc[df["group"] == "control", "Purchase"])        # distribution is normal
print("Test Stat = %.4f, p-value = %.4f" % (test_stat, pvalue))

test_stat, pvalue = shapiro(df.loc[df["group"] == "test", "Purchase"])        # distribution is normal
print("Test Stat = %.4f, p-value = %.4f" % (test_stat, pvalue))

test_stat, pvalue = levene(df.loc[df["group"] == "control", "Purchase"], df.loc[df["group"] == "test", "Purchase"])        # varience is homogeneous
print("Test Stat = %.4f, p-value = %.4f" % (test_stat, pvalue))


# Because the distributions are normal and varience is homogeneous, we're picking the T test which is parametric.

test_stat, pvalue = ttest_ind(df.loc[df["group"] == "control", "Purchase"],
                              df.loc[df["group"] == "test", "Purchase"])
print("Test Stat = %.4f, p-value = %.4f" % (test_stat, pvalue))

### There is no statistically significant difference between the purchase averages of the control and test groups.



