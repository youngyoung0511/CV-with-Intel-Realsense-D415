import matplotlib.pyplot as plt
import numpy as np

# Updating the labels to "sheets"
x_labels = ['20 sheets - Depth', '20 sheets - Error', '5 sheets - Depth', '5 sheets - Error']
y_values = [56, 24, 40, 16]  # Adjusted y-values

# Creating the bar graph with updated values
plt.figure(figsize=(8, 6))
bars = plt.bar(x_labels, y_values, color=['b', 'orange', 'b', 'orange'])



custom_labels = [476, 24, 440, 16]  # Manually specified labels
for i, bar in enumerate(bars):
    y_offset = -0.05  # Apply the same offset for all bars to lower the labels
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + y_offset, str(custom_labels[i]), ha='center', fontsize=12)


# Adding grid and labels (removed y-axis tick labels)
plt.gca().yaxis.set_ticks([])  # Remove the y-axis ticks

plt.ylabel('Values', fontsize=14)
plt.title('Depth and Adjusted Error Bars for 20 Sheets and 5 Sheets', fontsize=16)
plt.grid(axis='y', linestyle='--')

# Display the graph
plt.tight_layout()
plt.show()
