import matplotlib.pyplot as plt

# Data provided by the user
x_labels = ['20', '19', '18', '17', '16', '15', '14', '13', '12', '11',
            '10', '9', '8', '7', '6', '5', '4', '3', '2', '1']
y_values = [476, 482, 487, 496, 498, 494, 497, 494, 497, 496, 496, 485, 470, 450, 428, 440, 474, 530, 560, 680]

#[680,560,530,474,440,428,450,470,485,496,496,497,494,497,494,498,496,487,482,476]


# Plotting the graph with the x-axis in reverse order
plt.figure(figsize=(10, 6))
plt.plot(x_labels, y_values, marker='o', linestyle='-', color='b')

# Adding labels and title
plt.xlabel('Chapters', fontsize=12)
plt.ylabel('Values', fontsize=12)
#plt.title('13 time ', fontsize=14)                                                                                                                                                                                                                                                                                                                                                         # Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Display the graph
plt.tight_layout()
plt.show()
