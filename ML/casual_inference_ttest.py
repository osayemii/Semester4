import numpy as np
import pandas as pd
from scipy import stats

# Load public A/B testing dataset
url = "https://raw.githubusercontent.com/beery4010/Analyze-AB-Test-Results/master/ab_data.csv"
df = pd.read_csv(url)
df.head(5)

# Keep correctly assigned experiment records
df = df[
    ((df['group'] == 'control') &
     (df['landing_page'] == 'old_page')) |
    ((df['group'] == 'treatment') &
      (df['landing_page'] == 'new_page'))
].drop_duplicates(subset='user_id')

# Separate Group A (control) and Group B (variation)
group_a_data = df.loc[
    df['group'] == 'control', 'converted'
].dropna()

group_b_data = df.loc[
    df['group'] == 'treatment', 'converted'
].dropna()

# Performance independent samples t-test (Welch's t-test)
# scipy returns a 3-field named tuple: (statistic, pvalue, df)
result = stats.ttest_ind(
    group_a_data,
    group_b_data,
    equal_var=False
)
t_statistics, p_value = result.statistic, result.pvalue

# Display results
print('Group A conversion rate:', round(group_a_data.mean() * 100, 2), '%')
print('Group B conversion rate:', round(group_b_data.mean() * 100, 2), '%')

print('T-statistics:', round(t_statistics, 4))
print('P-value:', round(p_value, 4))

# Check significance threshold
alpha = 0.05

if p_value < alpha:
    print('Statistically significant difference detected!')

    if group_b_data.mean() > group_a_data.mean():
        print('Group B performed better.')
        print('Consider implementing the new version.')
    else:
        print('Group B performed worse.')
        print('Keep the original version.')
else:
    print('No statistically significant difference detected.')
    print('Insufficient evidence of a difference.')