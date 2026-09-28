
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="College Athletes' Earnings", layout="wide")
st.title("College Athletes' Earnings")
st.write("Interactive recreation of a New York Times visualization "  "showing expected annual N.I.L. earnings across college sports.")


major_data = {"Sport": ["Men's Basketball", "Football", "Women's Basketball", "Baseball"], "Earnings": [630000, 419000, 131000, 74000]}

nonrevenue_data = {"Sport": ["Men's golf", "Women's gymnastics", "Wrestling", "Men's track/cross country", "Women's track/cross country", "Women's swimming/diving", "Women's soccer", "Softball", "Women's volleyball", "Women's golf", "Women's tennis", "Men's lacrosse", "Men's soccer", 
                  "Men's swimming/diving", "Women's lacrosse", "Men's tennis", "Women's ice hockey", "Men's ice hockey", "Men's gymnastics", "Field hockey", "Rowing", "Bowling", "Men's volleyball", "Rifle", "Fencing"], 
                  "Earnings": [22900, 20700, 17900, 17800, 13800, 13400, 12200, 11300, 10500, 7900, 5800, 5700, 4900, 4400, 4300, 4100, 3500, 3500, 2200, 1200, 1000, 600, 500, 150, 100]}

major_df = pd.DataFrame(major_data)
nonrevenue_df = pd.DataFrame(nonrevenue_data)


highlight_options = ["Original NYT view"] + nonrevenue_df["Sport"].tolist()
selected_sport = st.selectbox("Choose a sport to highlight:", highlight_options)


if selected_sport == "Original NYT view":
    nonrevenue_colors = ["lightcoral" if sport in ["Men's track/cross country", "Women's track/cross country"] 
                         else "white" for sport in nonrevenue_df["Sport"]]
else:
    nonrevenue_colors = ["red" if sport == selected_sport 
                         else "white" for sport in nonrevenue_df["Sport"]]


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 9), gridspec_kw={"width_ratios": [1, 1.15], "wspace": 0.48})


#Major sports graph
ax1.barh(major_df["Sport"], major_df["Earnings"], height=0.68, facecolor="white", edgecolor="gray", linewidth=0.8)
ax1.invert_yaxis()

ax1.set_ylim(len(nonrevenue_df) - 0.5, -0.5)
ax1.set_xlim(0, 650000)
ax1.set_xticks([200000, 400000, 600000])
ax1.set_xticklabels(["$200,000", "$400,000", "$600,000"])
ax1.xaxis.tick_top()
ax1.grid(axis="x", color="gray", linewidth=0.8, alpha=0.25)
ax1.set_axisbelow(True)
ax1.set_title("Average earnings of college athletes in major sports", loc="left", fontsize=11, fontweight="bold", pad=20)


#Non revenue sports graph
ax2.barh(nonrevenue_df["Sport"], nonrevenue_df["Earnings"], height=0.68, color=nonrevenue_colors, edgecolor="gray", linewidth=0.8)
ax2.invert_yaxis()
ax2.set_xlim(0, 23000)
ax2.set_xticks([5000, 10000, 15000, 20000])
ax2.set_xticklabels(["$5,000", "$10,000", "$15,000", "$20,000"])
ax2.xaxis.tick_top()
ax2.grid(axis="x", color="gray", linewidth=0.8, alpha=0.25)
ax2.set_axisbelow(True)
ax2.set_title('Average earnings of college athletes in "nonrevenue" sports', loc="left", fontsize=11, fontweight="bold", pad=20)


for ax in [ax1, ax2]:
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["bottom"].set_visible(False)
    ax.spines["left"].set_color("gray")
    ax.spines["left"].set_linewidth(1)
    ax.tick_params(axis="x", length=0, labelsize=9, colors="black")
    ax.tick_params(axis="y", length=0, labelsize=9, colors="black"    )


if selected_sport == "Original NYT view":

    ax2.annotate("Both men's and women's\ntrack and field athletes\nsaw large increases in\nexpected earnings this\nyear, thanks in part to the\nadded exposure for these\nsports at the Olympics\nthis year.", xy=(15000, 3.5), xytext=(10500, 14), fontsize=7.5, color="gray", ha="left", va="center", 
                 arrowprops=dict(arrowstyle="->", color="gray", connectionstyle="arc3,rad=-0.35", linewidth=0.8))

st.pyplot(fig)
