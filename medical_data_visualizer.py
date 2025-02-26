import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1 Import the data from medical_examination.csv and assign it to the df variable.
df = pd.read_csv("medical_examination.csv")

# 2 Add an overweight column to the data. To determine if a person is overweight, first calculate their BMI by dividing their weight in kilograms
# by the square of their height in meters. If that value is > 25 then the person is overweight.
# Use the value 0 for NOT overweight and the value 1 for overweight.
df["bmi"] = round(df["weight"] / ((df["height"] / 100) ** 2), 1)
df["overweight"] = df["bmi"].apply(lambda x: 1 if x > 25 else 0)

# 3 Normalize data by making 0 always good and 1 always bad. If the value of cholesterol or gluc is 1, set the value to 0. If the value is more than 1, set the value to 1.
df["cholesterol"] = df["cholesterol"].apply(lambda x: 0 if x == 1 else 1)
df["gluc"] = df["gluc"].apply(lambda x: 0 if x == 1 else 1)
print(df)

# 4

fig, axs = plt.subplots(1, 2, figsize=(12,6), sharey=True)

c0_data = df.loc[df["cardio"] == 0][["cholesterol", "gluc", "smoke", "alco", "active", "overweight"]].sum()
print(c0_data)
print(c0_data.keys())
c0_names = list(c0_data.keys())
c0_values = list(c0_data)

#cholesterol, gluc, smoke, alco, active, and overweight
#cardio = 0
#cardio = 1

axs[0].bar(c0_names, c0_values)
#fig.suptitle('Categorical Plotting')


fig.savefig('catplot.png')

def draw_cat_plot():
    # 5
    df_cat = None


    # 6
    df_cat = None
    

    # 7



    # 8
    fig = None


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
