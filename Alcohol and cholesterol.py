import numpy as np
import pandas as pd
import scipy.stats as stats
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import shapiro, t, levene, pearsonr, spearmanr

# We will find out if Alcohol Consumption correlates to Cholesterol levels
df = pd.read_csv("alzheimers_disease_data.csv")

sns.boxplot(x=df["CholesterolTotal"])
plt.show()

Q1 = df["CholesterolTotal"].quantile(0.25)
Q3 = df["CholesterolTotal"].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - (1.5*IQR)
upper_bound = Q3 + (1.5*IQR)
outliers = df[(df["CholesterolTotal"] < lower_bound) | (df["CholesterolTotal"] > upper_bound)]
print(len(outliers))
print("No Outliers for either Alcohol consumption anf Cholesterol:")
print("Therefore we can move onto the normality tests ")

print("Kolmogorov smirnov test:")
mean_alcohol = np.mean(df["AlcoholConsumption"])
std_alcohol = np.std(df["AlcoholConsumption"])
result_kol_alcohol = stats.kstest(df["AlcoholConsumption"], 'norm', args=(mean_alcohol, std_alcohol))
print(f"kolmogorov result of Alcohol:{result_kol_alcohol}")
mean_cholesterol = np.mean(df["CholesterolTotal"])
std_cholesterol = np.std(df["CholesterolTotal"])
result_kol_Cholesterol = stats.kstest(df["CholesterolTotal"], 'norm', args=(mean_cholesterol, std_cholesterol))
print(f"kolmogorov result of Cholesterol:{result_kol_Cholesterol}")

result_of_spearsman = spearmanr(df["CholesterolTotal"], df["AlcoholConsumption"])
print(f"Spearman Correlation Coefficient: {result_of_spearsman}")

sns.regplot( data=df, x=df["AlcoholConsumption"], y=df["CholesterolTotal"],
             # scatter_kws: Styles only the dots
             scatter_kws={"alpha": 0.7, "s":5},
             # line_kws: Styles the line only
             line_kws={"color": "red"}
             )
plt.title("Correlation between Alcohol Consumption and Cholesterol build-up")
plt.show()