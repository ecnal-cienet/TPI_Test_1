import numpy as np
import matplotlib.pyplot as plt

# Sample data of students' scores in different subjects
data = {
    'Math': [88, 92, 79, 85, 90],
    'Science': [95, 85, 91, 89, 92],
    'English': [78, 82, 88, 90, 84],
    'History': [70, 75, 80, 85, 77]
}

def calculate_summary(data):
    """
    Calculates the average, max, and min scores for each subject.

    Args:
        data (dict): A dictionary where keys are subject names and values are lists of scores.

    Returns:
        dict: A dictionary where keys are subject names and values are dictionaries containing 
              the average, max, and min scores.
    """
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
    return summary

# Calculate summary using the function
summary = calculate_summary(data)

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
