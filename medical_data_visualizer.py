import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv("medical_examination.csv")

# 2
df["bmi"] = df["weight"] / ((df["height"] / 100) ** 2)
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
    fig = sns.catplot(data=df_cat, x="variable", y="total", hue="value", kind="bar", col="cardio").fig

    # 9
    fig.savefig('catplot.png')
    return fig

# 10
def draw_heat_map():
    # 11
    df_heat = df.loc[
        (df['ap_lo'] <= df['ap_hi'])
        & (df['height'] >= df['height'].quantile(0.025))
        & (df['height'] <= df['height'].quantile(0.975))
        & (df['weight'] >= df['weight'].quantile(0.025))
        & (df['weight'] <= df['weight'].quantile(0.975))
    ]

    df_heat = df_heat.drop(columns=['bmi'])

    #diastolic pressure is higher than systolic (Keep the correct data with (df['ap_lo'] <= df['ap_hi']))
    #height is less than the 2.5th percentile (Keep the correct data with (df['height'] >= df['height'].quantile(0.025)))
    #height is more than the 97.5th percentile
    #weight is less than the 2.5th percentile
    #weight is more than the 97.5th percentile

    # 12
    corr = df_heat.corr()

    # 13
    mask = np.zeros_like(corr)
    mask[np.triu_indices_from(mask)] = True

    # 14
    fig, ax = plt.subplots(figsize=(11,9))

    # 15
    sns.set(font_scale=0.6)
    sns.heatmap(corr, ax=ax, mask=mask, annot=True, fmt=".1f", linewidth=.5, robust=True )

    # 16
    fig.savefig('heatmap.png')
    return fig


draw_heat_map()