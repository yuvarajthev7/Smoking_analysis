import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv('survey lung cancer.csv')
df.head(1)
print("---------------------------")
df.columns = df.columns.str.strip().str.replace(' ', '_').str.upper()
print(df.columns.tolist())
print("\ndataframe info")
df.info()
print("\nmissing values")
df.isnull().sum() # nan values
print("---------------------------")
# Distribution of GENDER
print("Distribution of GENDER")
print(df['GENDER'].value_counts())
print("\nProportions:")
print(df['GENDER'].value_counts(normalize=True).round(2))
plt.figure(figsize=(6, 4))
sns.countplot(x='GENDER', data=df, palette='viridis')
plt.title('Distribution of Gender', fontsize=14)
plt.xlabel('Gender', fontsize=12)
plt.ylabel('Count', fontsize=12)
plt.tight_layout()
plt.show()

# Distribution of PEER_PRESSURE
print("\nDistribution of PEER_PRESSURE (1=Yes, 2=No)")
print(df['PEER_PRESSURE'].value_counts())
print("\nProportions:")
print(df['PEER_PRESSURE'].value_counts(normalize=True).round(2))

plt.figure(figsize=(6, 4))
sns.countplot(x='PEER_PRESSURE', data=df, palette='cividis')
plt.title('Distribution of Peer Pressure (1=Yes, 2=No)', fontsize=14)
plt.xlabel('Peer Pressure', fontsize=12)
plt.ylabel('Count', fontsize=12)
plt.xticks(ticks=[0, 1], labels=['Yes (1)', 'No (2)'])
plt.tight_layout()
plt.show()

# Distribution of SMOKING
print("\nDistribution of SMOKING (1=Yes, 2=No)")
print(df['SMOKING'].value_counts())
print("\nProportions:")
print(df['SMOKING'].value_counts(normalize=True).round(2))

plt.figure(figsize=(6, 4))
sns.countplot(x='SMOKING', data=df, palette='plasma')
plt.title('Distribution of Smoking (1=Yes, 2=No)', fontsize=14)
plt.xlabel('Smoking', fontsize=12)
plt.ylabel('Count', fontsize=12)
plt.xticks(ticks=[0, 1], labels=['Yes (1)', 'No (2)'])
plt.tight_layout()
plt.show()
# Filter for individuals who reported experiencing peer pressure
df_peer_pressure = df[df['PEER_PRESSURE'] == 1].copy()

print("Individuals reporting peer pressure (breakdown by gender)")
print(df_peer_pressure['GENDER'].value_counts())
print("\nProportions:")
print(df_peer_pressure['GENDER'].value_counts(normalize=True).round(2))

# analyzing smoking habits within the peer pressure group, by gender
smoking_by_gender_peer_pressure = df_peer_pressure.groupby('GENDER')['SMOKING'].value_counts(normalize=True).unstack().fillna(0).round(3)
print("\nSmoking Proportions (Yes/No) within peer pressure group, by gender ---")
smoking_by_gender_peer_pressure.columns = ['Smoking_Yes_1', 'Smoking_No_2']
print(smoking_by_gender_peer_pressure)
# Calculating the percentage of each gender who smoke due to peer pressure
# inclduing only who smoke in here
percentage_smoking_peer_pressure = smoking_by_gender_peer_pressure['Smoking_Yes_1'] * 100
print("\nPercentage of Each Gender Smoking (Among Those with Peer Pressure)")
print(percentage_smoking_peer_pressure)
plt.figure(figsize=(10, 6))
sns.countplot(data=df_peer_pressure, x='GENDER', hue='SMOKING', palette='coolwarm')
plt.title('Smoking Status by Gender (Among Those with Peer Pressure)', fontsize=16)
plt.xlabel('Gender', fontsize=12)
plt.ylabel('Number of Individuals', fontsize=12)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.legend(title='Smoking Status', labels=['Yes', 'No']) # Custom labels for legend
plt.tight_layout()
plt.show()
smoking_by_gender_peer_pressure.plot(kind='bar', figsize=(10, 6), colormap='RdYlGn')
plt.title('Proportion of Smoking (Yes/No) by Gender (Among Those with Peer Pressure)', fontsize=16)
plt.xlabel('Gender', fontsize=12)
plt.ylabel('Proportion', fontsize=12)
plt.xticks(rotation=0, fontsize=10)
plt.yticks(fontsize=10)
plt.legend(title='Smoking Status', labels=['Yes', 'No'])
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()


