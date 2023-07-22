import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pandas.api.types import CategoricalDtype

sns.set(rc={'figure.figsize':(6,4)})

df_airbnb = pd.read_csv('AB_NYC_2019.csv')
df_airbnb.head()

df_airbnb.info()

df_airbnb.columns


df_airbnb["neighbourhood_group"].unique()

df_airbnb["neighbourhood_group"].value_counts()

df_airbnb[["neighbourhood_group"]]

# df_airbnb["neighbourhood_group"].value_counts().plot.barh().set_title("Neighbourhood Names"

sns.barplot(x="neighbourhood_group", y= df_airbnb["neighbourhood_group"].index, data = df_airbnb, color = "red").set_title("Number of Neighbourhood Groups")

sns.barplot(x="neighbourhood_group", y="price", hue="room_type", data = df_airbnb)
plt.title("Price & Neighbourhood Groups & Room Type")

df_airbnb.groupby("room_type").sum().plot.pie(y="price", autopct="%.1f%%", ylabel = "", legend = False, figsize=(5,5))

columns = ["number_of_reviews", "reviews_per_month"]

for col in columns:
  plt.figure(figsize=(5,5))
  sns.scatterplot(x=col, y="price", data=df_airbnb)




sns.histplot(df_airbnb["price"], kde=True, bins=80)

sns.kdeplot(df_airbnb["price"])

sns.jointplot(x="price", y=df_airbnb["neighbourhood_group"], data=df_airbnb)

sns.catplot(x="room_type", y="price", data=df_airbnb)
plt.title("Room Type - Price")

# @title
plt.figure(figsize=(10,10))
sns.catplot(x="neighbourhood_group", y="price", hue="room_type", kind="point", data=df_airbnb)
plt.title("Neighbourhood - Price")

sns.kdeplot(df_airbnb["price"], shade=True)

(sns.FacetGrid(df_airbnb, hue="room_type", height=5, xlim=(0, 1250)).map(sns.kdeplot, "price", shade=True).add_legend())

plt.figure(figsize=(8,8))
plt.title("Correlation Matrix")
sns.heatmap(df_airbnb.corr(), annot=True);