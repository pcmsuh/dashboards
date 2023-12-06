import matplotlib.pyplot as plt

# Set the style of matplotlib to a custom dark theme
plt.style.use('default')
plt.rcParams.update({
    'figure.facecolor': '#262626',  # Dark background
    'axes.facecolor': '#262626',    # Dark axes background
    'axes.edgecolor': '#D9D9D9',    # Light axes edge color
    'axes.labelcolor': '#D9D9D9',   # Light label color
    'xtick.color': '#D9D9D9',       # Light x-tick color
    'ytick.color': '#D9D9D9',       # Light y-tick color
    'grid.color': '#666666',        # Grid color for better visibility
    'text.color': '#D9D9D9',        # Text color for better readability
    'font.family': 'Product Sans'   # Custom font for style
})

# Muted colors for each energy source type
muted_colors = {
    'Solar PV': '#8da0cb',   # Muted blue
    'Geothermal': '#e78ac3', # Muted pink
    'Wind': '#66c2a5',       # Muted green
    'Gas': '#e5c494',        # Muted yellow
    'Nuclear': '#ffd92f',    # Muted gold
    'Coal': '#a6d854',       # Muted lime
}

# Data for the energy sources and their respective costs
energy_sources = [
    'Solar PV—Rooftop Residential', 'Solar PV—Community & C&I', 'Solar PV—Utility-Scale',
    'Solar PV + Storage—Utility-Scale', 'Geothermal', 'Wind—Onshore', 'Wind + Storage—Onshore',
    'Wind—Offshore', 'Gas Peaking', 'Nuclear', 'Coal', 'Gas Combined Cycle'
]
low_cost = [117, 49, 24, 46, 61, 24, 42, 72, 115, 31, 52, 39]
high_cost = [282, 185, 96, 102, 102, 75, 114, 140, 221, 68, 166, 156]

# Map each energy source to its corresponding color
bar_colors = [muted_colors[key] for source in energy_sources for key in muted_colors if key in source]

# Plotting the LCOE graph
plt.figure(figsize=(14, 8))

# Plot bars with muted color-coding
for i, source in enumerate(energy_sources):
    plt.barh(source, high_cost[i] - low_cost[i], left=low_cost[i], color=bar_colors[i], edgecolor='black')

# Adding horizontal grid lines for better readability
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Setting x-axis limits
plt.xlim(0, 300)

# Adding titles and labels
plt.title('Levelized Cost of Energy Comparison', fontsize=16, weight='bold')
plt.xlabel('Levelized Cost of Energy ($/MWh)', fontsize=14)
plt.ylabel('Energy Source', fontsize=14)

# Set the y-axis labels to rotate for better legibility
plt.yticks(rotation=45, fontsize=12)
plt.xticks(fontsize=12)

# Invert y-axis to match the original layout and adjust plot borders
plt.gca().invert_yaxis()
plt.tight_layout()

# Show the final plot
plt.show()
