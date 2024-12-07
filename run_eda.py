from src.eda import (
    load_data,
    clean_data,
    generate_summary_statistics,
    plot_correlation_heatmap,
    plot_time_series,
    plot_time_series_with_precipitation,
    plot_wind_rose,
    evaluate_cleaning_impact,
    plot_bubble_chart,
)

# 1️⃣ Load the Data
df = load_data('notebooks/benin-malanville.csv')
if df.empty:
    print("Error: Failed to load data.")
else:
    # 2️⃣ Clean the Data
    df_cleaned = clean_data(df)
    if df_cleaned.empty:
        print("Error: DataFrame is empty after cleaning.")
    else:
        # 3️⃣ Generate Summary Statistics
        print("\nSummary statistics:")
        summary = generate_summary_statistics(df_cleaned)

        # 4️⃣ Plot Correlation Heatmap
        print("\nPlotting correlation heatmap...")
        plot_correlation_heatmap(df_cleaned)

        # 5️⃣ Plot Time Series for GHI
        print("\nPlotting GHI time-series...")
        plot_time_series(df_cleaned, 'ghi')

        # 6️⃣ Plot Time Series with Precipitation
        print("\nPlotting Time Series with Precipitation...")
        plot_time_series_with_precipitation(df_cleaned)

        # 7️⃣ Plot Wind Rose
        print("\nPlotting Wind Rose...")
        plot_wind_rose(df_cleaned)

        # 8️⃣ Evaluate Cleaning Impact
        print("\nEvaluating Cleaning Impact...")
        evaluate_cleaning_impact(df_cleaned)

        # 9️⃣ Plot Bubble Chart
        print("\nPlotting Bubble Chart...")
        plot_bubble_chart(df_cleaned)
