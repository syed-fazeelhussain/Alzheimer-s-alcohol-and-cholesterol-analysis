Statistical analysis assessing the correlation between alcohol consumption and cholesterol level in Alzheimer's patients.
The object of this analysis was to determine if there is a direct correlation between alcohol consumption and cholesterol level in Alzheimer's patients.
The data was utilized in this analysis was acquired via kaggle
The analysis was conducted using python, leveraging several libraries including numpy, pandas, scipy, matplotlib and seaborn
To begin with, it was identified that the data contained no null values so boxplots were plotted to identify any outliers and interquartile ranges were also used but there were no signs of any outliers disturbing the data
Hence we moved onto kolmogorov Smirnov which is used to test the normalty of a sample data
If the p value from this test is greater than alpha or 0.05 then we reject the null hypothesis and the data is normally distributed, we may then run the pearson correlation . However, if the p-value is less than alpha then that means the data is not normally distribted and spearsman correlation is to be opted for.
The data for alcohol consumption and cholesterol level both were not normally distributed hence spearsman correlation was employed
The result was statistically insignificant(p-value=0.114) and the correlation was extremely Weak(-0.034) suggesting there is no direct correlation of alcohol consumption with cholesterol levels in Alzheimer's patients 
Regression plot was plotted using matplotlib and seaborn for better visualization

