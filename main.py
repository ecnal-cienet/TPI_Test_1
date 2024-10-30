import numpy as np
import matplotlib.pyplot as plt

# Sample data of students' scores in different subjects
data = {
    'Math': [88, 92, 79, 85, 90],
    'Science': [95, 85, 91, 89, 92],
    'English': [78, 82, 88, 90, 84],
    'History': [70, 75, 80, 85, 77]
}

# Calculate average, max, and min scores for each subject
summary = {}
for subject, scores in data.items():
    average_score = np.mean(scores)
    max_score = np.max(scores)
    min_score = np.min(scores)
    summary[subject] = {
        'average': average_score,
        'max': max_score,
        'min': min_score
    }

# Print summary
print("Summary of Scores:")
for subject, stats in summary.items():
    print(f"{subject}: Average = {stats['average']}, Max = {stats['max']}, Min = {stats['min']}")

# Plotting
plt.figure(figsize=(10, 6))
for subject, scores in data.items():
    plt.plot(scores, label=subject, marker='o')

plt.title("Scores by Subject")
plt.xlabel("Students")
plt.ylabel("Scores")
plt.legend()
plt.grid(True)
plt.show()
