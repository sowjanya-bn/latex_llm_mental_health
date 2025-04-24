import pandas as pd

# Read CSV file
df = pd.read_csv('refined_bot_comparisons.csv')

# Convert the DataFrame to LaTeX format
latex_table = df.to_latex(index=False)
print(latex_table)
