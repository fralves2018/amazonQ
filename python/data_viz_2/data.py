import matplotlib.pyplot as plt # type: ignore
import numpy as np # type: ignore

# function that plots a pie chart with the usage of the most popular programming languages
def plot_pie_chart():
    # Data
    labels = ['Python', 'JavaScript', 'Java', 'C#', 'PHP', 'C++', 'C', 'TypeScript', 'Shell', 'Ruby']
    sizes = [29.8, 14.8, 10.8, 7.7, 4.7, 4.4, 3.6, 2.3, 2.3, 1.9]

    # Plot
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.title('Most Popular Programming Languages')
    plt.show()

# Call the function to display the pie chart
if __name__ == "__main__":
    plot_pie_chart()
