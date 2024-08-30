import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('sample_population_data.csv')

plt.figure(figsize=(8, 6))
df['Gender'].value_counts().plot(kind='bar', color=['skyblue', 'lightgreen'])
plt.title('Distribution of Gender')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.show()

plt.figure(figsize=(8, 6))
plt.hist(df['Age'], bins=5, color='skyblue', edgecolor='black')
plt.title('Distribution of Age')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()
