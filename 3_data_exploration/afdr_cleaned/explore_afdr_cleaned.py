import os
import warnings

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

warnings.filterwarnings("ignore")
plt.style.use("default")
sns.set_palette("husl")

# Set up the correct figures directory relative to this script
FIGURES_DIR = os.path.join(os.path.dirname(__file__), "figures")
os.makedirs(FIGURES_DIR, exist_ok=True)


def load_data():
    df = pd.read_csv("../../1_datasets/processed_data/afdr_cleaned.csv")
    # Ensure only expected columns are used
    expected_cols = [
        "Year",
        "Quarter",
        "All_Loan_Sizes",
        "$1k–9k",
        "$10k–24k",
        "$25k–49k",
        "$50k–99k",
        "$100k–249k",
        "$250k+",
    ]
    missing_cols = [col for col in expected_cols if col not in df.columns]
    if missing_cols:
        raise ValueError(f"Missing expected columns: {missing_cols}")
    return df[expected_cols]


def overview_and_visualizations(df):
    # Always construct 'PeriodTS' from 'Year' and 'Quarter'
    df["PeriodTS"] = pd.PeriodIndex(
        df["Year"].astype(str) + "Q" + df["Quarter"].astype(str), freq="Q"
    ).to_timestamp()
    loan_size_cols = [
        "$1k–9k",
        "$10k–24k",
        "$25k–49k",
        "$50k–99k",
        "$100k–249k",
        "$250k+",
    ]

    # Overview visualizations
    fig, axes = plt.subplots(2, 2, figsize=(16, 12))
    fig.suptitle("AFDR Dataset Overview", fontsize=18, fontweight="bold")

    # 1. Time series of total loans
    ax1 = axes[0, 0]
    total_loans = df.groupby("PeriodTS")["All_Loan_Sizes"].sum()
    ax1.plot(total_loans.index, total_loans.values, linewidth=2.5, color="#2E86AB")
    ax1.set_title("Total Loan Volume Over Time", fontsize=14, fontweight="bold")
    ax1.set_xlabel("Year", fontsize=12)
    ax1.set_ylabel("Total Loan Volume", fontsize=12)
    ax1.grid(True, alpha=0.3)

    # 2. Distribution of loan sizes (pie)
    ax2 = axes[0, 1]
    loan_size_totals = df[loan_size_cols].sum()
    colors = ["#A23B72", "#F18F01", "#C73E1D", "#592E83", "#2E86AB", "#A23B72"]
    ax2.pie(
        loan_size_totals.values,
        labels=loan_size_cols,
        autopct="%1.1f%%",
        colors=colors,
        startangle=90,
    )
    ax2.set_title(
        "Distribution of Loans by Size Category", fontsize=14, fontweight="bold"
    )

    # 3. Time series by loan size category
    ax3 = axes[1, 0]
    for i, col in enumerate(loan_size_cols):
        monthly_data = df.groupby("PeriodTS")[col].sum()
        ax3.plot(
            monthly_data.index,
            monthly_data.values,
            label=col,
            linewidth=2,
            color=colors[i],
        )
    ax3.set_title(
        "Loan Volume by Size Category Over Time", fontsize=14, fontweight="bold"
    )
    ax3.set_xlabel("Year", fontsize=12)
    ax3.set_ylabel("Loan Volume", fontsize=12)
    ax3.legend(bbox_to_anchor=(1.05, 1), loc="upper left", fontsize=10)
    ax3.grid(True, alpha=0.3)

    # 4. Correlation heatmap
    ax4 = axes[1, 1]
    correlation_matrix = df[loan_size_cols + ["All_Loan_Sizes"]].corr()
    sns.heatmap(
        correlation_matrix,
        annot=True,
        cmap="RdYlBu_r",
        center=0,
        ax=ax4,
        fmt=".2f",
        square=True,
        cbar_kws={"shrink": 0.8},
    )
    ax4.set_title("Correlation Matrix of Loan Sizes", fontsize=14, fontweight="bold")

    plt.tight_layout()
    plt.savefig(
        os.path.join(FIGURES_DIR, "afdr_overview_visualizations.png"),
        dpi=300,
        bbox_inches="tight",
    )
    plt.show()
    return loan_size_cols


def detailed_analysis(df, loan_size_cols):
    # Statistical analysis
    fig, axes = plt.subplots(2, 2, figsize=(16, 12))
    fig.suptitle("Statistical Analysis of AFDR Data", fontsize=18, fontweight="bold")

    # 1. Box plot of loan distributions
    ax1 = axes[0, 0]
    df_melted = df[loan_size_cols].melt()
    sns.boxplot(data=df_melted, x="variable", y="value", ax=ax1, palette="Set3")
    ax1.set_title(
        "Distribution of Loans by Size Category", fontsize=14, fontweight="bold"
    )
    ax1.set_xlabel("Loan Size Category", fontsize=12)
    ax1.set_ylabel("Loan Volume", fontsize=12)
    ax1.tick_params(axis="x", rotation=45)

    # 2. Quarterly patterns
    ax2 = axes[0, 1]
    quarterly_totals = df.groupby("Quarter")["All_Loan_Sizes"].mean()
    colors = ["#A23B72", "#F18F01", "#C73E1D", "#592E83"]
    ax2.bar(quarterly_totals.index, quarterly_totals.values, color=colors)
    ax2.set_title("Average Loan Volume by Quarter", fontsize=14, fontweight="bold")
    ax2.set_xlabel("Quarter", fontsize=12)
    ax2.set_ylabel("Average Loan Volume", fontsize=12)
    ax2.set_xticks([1, 2, 3, 4])

    # 3. Year-over-year growth
    ax3 = axes[1, 0]
    yearly_totals = df.groupby("Year")["All_Loan_Sizes"].sum()
    growth_rate = yearly_totals.pct_change() * 100
    colors_growth = ["red" if x < 0 else "green" for x in growth_rate.values[1:]]
    ax3.bar(
        growth_rate.index[1:], growth_rate.values[1:], color=colors_growth, alpha=0.7
    )
    ax3.set_title("Year-over-Year Growth Rate", fontsize=14, fontweight="bold")
    ax3.set_xlabel("Year", fontsize=12)
    ax3.set_ylabel("Growth Rate (%)", fontsize=12)
    ax3.axhline(y=0, color="black", linestyle="-", alpha=0.5)

    # 4. Loan size category trends
    ax4 = axes[1, 1]
    for i, col in enumerate(loan_size_cols):
        yearly_data = df.groupby("Year")[col].sum()
        ax4.plot(
            yearly_data.index,
            yearly_data.values,
            label=col,
            marker="o",
            linewidth=2,
            color=colors[i % len(colors)],
        )
    ax4.set_title("Yearly Trends by Loan Size Category", fontsize=14, fontweight="bold")
    ax4.set_xlabel("Year", fontsize=12)
    ax4.set_ylabel("Total Loan Volume", fontsize=12)
    ax4.legend(bbox_to_anchor=(1.05, 1), loc="upper left", fontsize=10)
    ax4.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig(
        os.path.join(FIGURES_DIR, "afdr_statistical_analysis.png"),
        dpi=300,
        bbox_inches="tight",
    )
    plt.show()


def analyze_by_loan_characteristic(df, loan_size_cols):
    # Only run if 'Loan_Characteristic' column exists
    if "Loan_Characteristic" in df.columns:
        df["PeriodTS"] = pd.PeriodIndex(
            df["Year"].astype(str) + "Q" + df["Quarter"].astype(str), freq="Q"
        ).to_timestamp()
        characteristics = df["Loan_Characteristic"].unique()
        for char in characteristics:
            char_data = df[df["Loan_Characteristic"] == char]
            fig, axes = plt.subplots(2, 2, figsize=(16, 12))
            fig.suptitle(
                f"Analysis for Loan Characteristic {char}",
                fontsize=18,
                fontweight="bold",
            )
            # 1. Time series for this characteristic
            ax1 = axes[0, 0]
            total_loans = char_data.groupby("PeriodTS")["All_Loan_Sizes"].sum()
            ax1.plot(
                total_loans.index, total_loans.values, linewidth=2.5, color="#2E86AB"
            )
            ax1.set_title(
                f"Total Loan Volume - Characteristic {char}",
                fontsize=14,
                fontweight="bold",
            )
            ax1.set_xlabel("Year", fontsize=12)
            ax1.set_ylabel("Total Loan Volume", fontsize=12)
            ax1.grid(True, alpha=0.3)
            # 2. Distribution by loan size for this characteristic
            ax2 = axes[0, 1]
            loan_size_totals = char_data[loan_size_cols].sum()
            colors = ["#A23B72", "#F18F01", "#C73E1D", "#592E83", "#2E86AB", "#A23B72"]
            ax2.pie(
                loan_size_totals.values,
                labels=loan_size_cols,
                autopct="%1.1f%%",
                colors=colors,
                startangle=90,
            )
            ax2.set_title(
                f"Loan Size Distribution - Characteristic {char}",
                fontsize=14,
                fontweight="bold",
            )
            # 3. Box plot for this characteristic
            ax3 = axes[1, 0]
            char_melted = char_data[loan_size_cols].melt()
            sns.boxplot(
                data=char_melted, x="variable", y="value", ax=ax3, palette="Set3"
            )
            ax3.set_title(
                f"Loan Distribution - Characteristic {char}",
                fontsize=14,
                fontweight="bold",
            )
            ax3.set_xlabel("Loan Size Category", fontsize=12)
            ax3.set_ylabel("Loan Volume", fontsize=12)
            ax3.tick_params(axis="x", rotation=45)
            # 4. Yearly trends for this characteristic
            ax4 = axes[1, 1]
            for i, col in enumerate(loan_size_cols):
                yearly_data = char_data.groupby("Year")[col].sum()
                ax4.plot(
                    yearly_data.index,
                    yearly_data.values,
                    label=col,
                    marker="o",
                    linewidth=2,
                    color=colors[i],
                )
            ax4.set_title(
                f"Yearly Trends - Characteristic {char}", fontsize=14, fontweight="bold"
            )
            ax4.set_xlabel("Year", fontsize=12)
            ax4.set_ylabel("Total Loan Volume", fontsize=12)
            ax4.legend(bbox_to_anchor=(1.05, 1), loc="upper left", fontsize=10)
            ax4.grid(True, alpha=0.3)
            plt.tight_layout()
            plt.savefig(
                os.path.join(FIGURES_DIR, f"afdr_characteristic_{char}_analysis.png"),
                dpi=300,
                bbox_inches="tight",
            )
            plt.show()


def summary_statistics(df, loan_size_cols):
    print("\n" + "=" * 60)
    print("📊 SUMMARY STATISTICS")
    print("=" * 60)
    print("\n📈 Summary statistics for loan size categories:")
    summary_stats = df[loan_size_cols].describe()
    print(summary_stats)
    print(
        f"\n💰 Total loan volume across all categories: {df['All_Loan_Sizes'].sum():,.0f}"
    )
    print(f"📊 Average loan volume per period: {df['All_Loan_Sizes'].mean():,.0f}")
    print(f"📈 Maximum loan volume in a period: {df['All_Loan_Sizes'].max():,.0f}")
    print(f"📉 Minimum loan volume in a period: {df['All_Loan_Sizes'].min():,.0f}")
    # Percentage distribution
    print("\n📊 Percentage distribution by loan size:")
    total_volume = df["All_Loan_Sizes"].sum()
    for col in loan_size_cols:
        col_total = df[col].sum()
        percentage = (col_total / total_volume) * 100
        print(f"   {col}: {percentage:.1f}% ({col_total:,.0f})")


def save_processed_data(df):
    df.to_csv(os.path.join(FIGURES_DIR, "afdr_explored.csv"), index=False)
    print(
        f"\n✅ Exploration complete! Processed data saved to '{os.path.join('figures', 'afdr_explored.csv')}'"
    )
    print("📊 Visualizations saved as PNG files in the 'figures/' directory")


def main():
    df = load_data()
    loan_size_cols = overview_and_visualizations(df)
    detailed_analysis(df, loan_size_cols)
    analyze_by_loan_characteristic(df, loan_size_cols)
    summary_statistics(df, loan_size_cols)
    save_processed_data(df)


if __name__ == "__main__":
    main()
