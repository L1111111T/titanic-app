import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Apply seaborn style
sns.set_style('darkgrid')

# Display the page title
st.title("Titanic App by [L1111111T]")

# Read the train.csv file
df = pd.read_csv("train.csv")

# Display the entire dataframe in the Streamlit app
st.dataframe(df)

# Create three side-by-side box plots for Fare distribution by Pclass
fig, axes = plt.subplots(1, 3, figsize=(15, 5), sharey=True)

for idx, pclass in enumerate(sorted(df['Pclass'].unique())):
    sns.boxplot(
        ax=axes[idx],
        data=df[df['Pclass'] == pclass],
        y='Fare'
    )
    axes[idx].set_title(f'Pclass {pclass}')
    axes[idx].set_xlabel('')  # No x-label needed for a single box
    axes[idx].set_ylabel('Fare' if idx == 0 else '')

# Adjust layout for better spacing
plt.tight_layout()

# Display the plotted figure in the Streamlit page
st.pyplot(fig)
