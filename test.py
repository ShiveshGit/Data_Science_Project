import matplotlib.pyplot as plt

# Given state
data = [[-1.0, -1.0, 1.0, 1.0, -1.0]]

# Flatten the list to make it 1D
data_flat = [item for sublist in data for item in sublist]

# Create histogram
plt.hist(data_flat, bins=[-2, -1, 0, 1, 2], edgecolor='black')

# Set labels
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram of State Values')

# Show the plot
plt.xticks([-1, 0, 1])
plt.show()
