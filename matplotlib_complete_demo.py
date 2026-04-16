import matplotlib.pyplot as plt

names = ['Amit', 'Rahul', 'Priya', 'Sneha', 'Arjun']
marks = [75, 85, 90, 80, 70]

plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.plot(names, marks, color='blue', alpha=0.7)
plt.grid(True)
plt.title('Line Plot')

plt.subplot(2, 2, 2)
plt.scatter(names, marks, color='green', alpha=0.5)
plt.title('Scatter Plot')

plt.subplot(2, 2, 3)
plt.bar(names, marks, color='orange', alpha=0.8)
plt.title('Bar Graph')

plt.subplot(2, 2, 4)
plt.hist(marks, color='purple', alpha=0.6)
plt.title('Histogram')

plt.tight_layout()
plt.show()