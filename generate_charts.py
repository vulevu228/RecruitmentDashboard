"""Generates supplementary charts from data/job_application.xlsx.

These sit alongside the Power BI report (dashboard/job-application-data.pbix)
as a quick, static preview of metrics the Azure Maps visual and DAX measures
cover interactively in the .pbix.
"""

import pandas as pd
import matplotlib.pyplot as plt

BLUE = "#2a78d6"
ORANGE = "#eb6834"
INK = "#0b0b0b"
INK_SECONDARY = "#52514e"
MUTED = "#898781"
GRID = "#e1e0d9"
BASELINE = "#c3c2b7"
SURFACE = "#fcfcfb"

plt.rcParams.update({
    "font.family": "sans-serif",
    "font.size": 11,
    "axes.edgecolor": BASELINE,
    "axes.labelcolor": INK_SECONDARY,
    "text.color": INK,
    "xtick.color": MUTED,
    "ytick.color": MUTED,
    "figure.facecolor": SURFACE,
    "axes.facecolor": SURFACE,
    "savefig.facecolor": SURFACE,
})


def style_axes(ax):
    for spine in ("top", "right"):
        ax.spines[spine].set_visible(False)
    ax.spines["left"].set_color(BASELINE)
    ax.spines["bottom"].set_color(BASELINE)


df = pd.read_excel("data/job_application.xlsx")
df["Date"] = pd.to_datetime(df["Date"])

# ---------------------------------------------------------------------------
# 1. Top 10 cities by application volume
# ---------------------------------------------------------------------------
top_cities = df["Job Location"].value_counts().head(10).sort_values()

fig, ax = plt.subplots(figsize=(8, 5))
ax.barh(top_cities.index, top_cities.values, color=BLUE, height=0.65)
for y, v in enumerate(top_cities.values):
    ax.text(v + top_cities.max() * 0.01, y, f"{v:,}", va="center", fontsize=9.5, color=INK_SECONDARY)
ax.set_xlabel("Applications")
ax.set_title("Top 10 Cities by Application Volume", loc="left", fontsize=13, fontweight="bold")
ax.xaxis.grid(True, color=GRID, linewidth=0.8)
ax.set_axisbelow(True)
style_axes(ax)
ax.tick_params(axis="y", length=0)
ax.set_xlim(0, top_cities.max() * 1.12)
plt.tight_layout()
plt.savefig("dashboard/top_cities.png", dpi=150)
plt.close()

# ---------------------------------------------------------------------------
# 2. Hiring rate: Easy Apply vs. traditional application
# ---------------------------------------------------------------------------
by_method = df.groupby("Easy Apply")["Hired"].mean().mul(100).reindex([False, True])
by_method.index = ["Traditional Form", "Easy Apply"]

fig, ax = plt.subplots(figsize=(5, 5))
bars = ax.bar(by_method.index, by_method.values, color=[BLUE, ORANGE], width=0.5)
for bar, v in zip(bars, by_method.values):
    ax.text(bar.get_x() + bar.get_width() / 2, v + 0.3, f"{v:.1f}%",
            ha="center", va="bottom", fontsize=11, fontweight="bold")
ax.set_ylabel("Hiring rate (%)")
ax.set_ylim(0, max(by_method.values) + 5)
ax.set_title("Hiring Rate by Application Method", loc="left", fontsize=13, fontweight="bold")
ax.yaxis.grid(True, color=GRID, linewidth=0.8)
ax.set_axisbelow(True)
style_axes(ax)
plt.tight_layout()
plt.savefig("dashboard/hiring_rate_by_method.png", dpi=150)
plt.close()

# ---------------------------------------------------------------------------
# 3. Monthly application volume, 2023
# ---------------------------------------------------------------------------
monthly = df.set_index("Date").resample("MS").size()

fig, ax = plt.subplots(figsize=(9, 5))
ax.plot(monthly.index, monthly.values, color=BLUE, linewidth=2, marker="o", markersize=6)
ax.set_ylabel("Applications")
ax.set_title("Monthly Application Volume (2023)", loc="left", fontsize=13, fontweight="bold")
ax.grid(True, axis="y", color=GRID, linewidth=0.8)
ax.set_axisbelow(True)
style_axes(ax)
fig.autofmt_xdate()
plt.tight_layout()
plt.savefig("dashboard/applications_by_month.png", dpi=150)
plt.close()

# ---------------------------------------------------------------------------
# 4. Top 10 job titles by volume
# ---------------------------------------------------------------------------
top_titles = df["Job Title"].value_counts().head(10).sort_values()

fig, ax = plt.subplots(figsize=(8, 5))
ax.barh(top_titles.index, top_titles.values, color=BLUE, height=0.65)
for y, v in enumerate(top_titles.values):
    ax.text(v + top_titles.max() * 0.01, y, f"{v:,}", va="center", fontsize=9.5, color=INK_SECONDARY)
ax.set_xlabel("Applications")
ax.set_title("Top 10 Job Titles by Volume", loc="left", fontsize=13, fontweight="bold")
ax.xaxis.grid(True, color=GRID, linewidth=0.8)
ax.set_axisbelow(True)
style_axes(ax)
ax.tick_params(axis="y", length=0)
ax.set_xlim(0, top_titles.max() * 1.12)
plt.tight_layout()
plt.savefig("dashboard/top_job_titles.png", dpi=150)
plt.close()

print("Charts written to dashboard/")
