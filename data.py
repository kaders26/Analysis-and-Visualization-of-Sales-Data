# Gerekli kütüphaneleri içe aktarın
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Rastgele satış verileri oluşturun
np.random.seed(42)
data = {
    'Tarih': pd.date_range(start='2022-01-01', end='2022-12-31', freq='D'),
    'Ürün': np.random.choice(['A', 'B', 'C'], size=365),
    'Satış Miktarı': np.random.randint(50, 500, size=365),
    'Satış Geliri': np.random.uniform(1000, 10000, size=365)
}

df = pd.DataFrame(data)

# Veri setini gözden geçirin
print(df.head())

# Satış trendini görselleştirin
plt.figure(figsize=(12, 6))
sns.lineplot(x='Tarih', y='Satış Miktarı', hue='Ürün', data=df)
plt.title('Satış Trendi')
plt.xlabel('Tarih')
plt.ylabel('Satış Miktarı')
plt.show()

# Aylık satış gelirini görselleştirin
plt.figure(figsize=(12, 6))
sns.barplot(x=df['Tarih'].dt.month_name(), y='Satış Geliri', data=df)
plt.title('Aylık Satış Geliri')
plt.xlabel('Ay')
plt.ylabel('Satış Geliri')
plt.show()
