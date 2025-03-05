import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv("medical_examination.csv")

# 2
df["bmi"] = round(df["weight"] / ((df["height"] / 100) ** 2), 1)
df["overweight"] = df["bmi"].apply(lambda x: 1 if x > 25 else 0)

# 3
df["cholesterol"] = df["cholesterol"].apply(lambda x: 0 if x == 1 else 1)
df["gluc"] = df["gluc"].apply(lambda x: 0 if x == 1 else 1)

# 4
def draw_cat_plot():
    # 5
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=["active", "alco", "cholesterol", "gluc", "overweight", "smoke"])

    # 6
    df_cat = df_cat.groupby(['variable', 'value', 'cardio']).size().reset_index(name='total')

    # 7
    #print(df_cat.dtypes)

    # 8
    fig = sns.catplot(data=df_cat, x="variable", y="total", hue="value", kind="bar", col="cardio")

    # 9
    fig.savefig('catplot.png')
    return fig

# 10
def draw_heat_map():
    # 11
    df_heat = None

    # 12
    corr = None

    # 13
    mask = None



    # 14
    fig, ax = None

    # 15



    # 16
    fig.savefig('heatmap.png')
    return fig
