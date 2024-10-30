# TPI_Test_1
This is TPI Test Repo #1

## Analysis of Student Scores
This script analyzes student performance across different subjects, providing a summary of scores and a visual representation of the data.

### Data:

The script uses a dictionary data to store student scores in various subjects: Math, Science, English, and History. Each subject maps to a list of scores representing individual student performance.

### Calculations:

#### Summary Statistics:

The code iterates through each subject in the data dictionary.
For each subject, it calculates the average, maximum, and minimum scores using np.mean(), np.max(), and np.min() functions from the NumPy library.
These statistics are stored in a new dictionary called summary, where each subject maps to another dictionary containing its average, maximum, and minimum scores.
Printing Summary:

The code then neatly prints the calculated summary statistics for each subject, making it easy to interpret the data.
Visualization:

The script utilizes the Matplotlib library to generate a line plot visualizing student scores.
Each line on the plot represents a different subject, with markers indicating individual student scores.
The plot is labeled with a title, axis labels, a legend for clarity, and a grid for better readability.
Key Features:

Clear Data Structure: The use of dictionaries effectively organizes the data, making it easy to access and process.
Concise Calculations: NumPy functions simplify the calculation of summary statistics.
Informative Visualization: The plot provides a clear visual comparison of student performance across subjects.
Potential Improvements:

Error Handling: Implementing error handling mechanisms, such as checking for empty score lists, would enhance the robustness of the script.
User Input: Allowing users to input their own data or specify subjects of interest would increase the script's interactivity and usefulness.
Advanced Visualizations: Exploring other visualization types, such as bar charts or box plots, could provide additional insights into the data.