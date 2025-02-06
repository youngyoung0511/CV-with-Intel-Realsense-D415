import matplotlib.pyplot as plt

# Data provided by the user
x_labels = ['20', '19', '18', '17', '16', '15', '14', '13', '12', '11',
            '10', '9', '8', '7', '6', '5', '4', '3', '2', '1']
y_values = [476, 482, 487, 496, 498, 494, 497, 494, 497, 496, 496, 485, 470, 450, 428, 440, 474, 530, 560, 680]

# Adjusting figure size to be wider
plt.figure(figsize=(14, 6))

# Plotting the graph with the x-axis in reverse order and grid
plt.plot(x_labels, y_values, marker='o', linestyle='-', color='b')

# Adding labels and title with larger font size
plt.xlabel('Chapters', fontsize=18)
plt.ylabel('Values', fontsize=18)

# Rotate x-axis labels for better readability and add grid
plt.xticks(rotation=45, fontsize=15)
plt.yticks(fontsize=15)
plt.grid(True)

# Display the graph with tighter layout
plt.tight_layout()
plt.show()
