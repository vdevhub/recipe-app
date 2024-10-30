import matplotlib.pyplot as plt
import base64
from io import BytesIO
from collections import Counter
import numpy as np


def get_graph():
    # create a BytesIO buffer for the image
    buffer = BytesIO()

    # create a plot with a bytesIO object as a file-like object. Set format to png
    plt.savefig(buffer, format="png")

    # set cursor to the beginning of the stream
    buffer.seek(0)

    # retrieve the content of the file
    image_png = buffer.getvalue()

    # encode the bytes-like object
    graph = base64.b64encode(image_png)

    # decode to get the string as output
    graph = graph.decode("utf-8")

    # free up the memory of buffer
    buffer.close()

    # return the image/graph
    return graph


def plot_bar_chart(recipes):
    if not recipes:  # Check if there are no recipes
        return "No recipes available to display the bar chart."

    difficulties = [recipe.difficulty for recipe in recipes]
    difficulty_counts = Counter(difficulties)

    plt.switch_backend("AGG")
    plt.figure(figsize=(10, 6))
    plt.bar(difficulty_counts.keys(), difficulty_counts.values(), color="skyblue")
    plt.xlabel("Difficulty Levels")
    plt.ylabel("Number of Recipes")
    plt.title("Number of Recipes by Difficulty Level")
    plt.xticks(rotation=45)

    plt.tight_layout()
    graph = get_graph()
    plt.close()
    return graph


def plot_pie_chart(recipes):
    if not recipes:  # Check if there are no recipes
        return "No recipes available to display the pie chart."

    cooking_times = [recipe.cooking_time for recipe in recipes]

    time_ranges = ["0-30 mins", "31-60 mins", "61+ mins"]
    time_counts = [0, 0, 0]

    for time in cooking_times:
        if time <= 30:
            time_counts[0] += 1
        elif time <= 60:
            time_counts[1] += 1
        else:
            time_counts[2] += 1

    plt.switch_backend("AGG")
    plt.figure(figsize=(8, 8))
    plt.pie(time_counts, labels=time_ranges, autopct="%1.1f%%", startangle=140)
    plt.title("Distribution of Recipes by Cooking Time")
    plt.axis("equal")

    graph = get_graph()
    plt.close()
    return graph


def plot_line_chart(recipes):
    if not recipes:  # Check if there are no recipes
        return "No recipes available to display the line chart."

    # Aggregate cooking time by difficulty
    difficulty_data = {}
    for recipe in recipes:
        if recipe.difficulty in difficulty_data:
            difficulty_data[recipe.difficulty].append(recipe.cooking_time)
        else:
            difficulty_data[recipe.difficulty] = [recipe.cooking_time]

    # Calculate average cooking time for each difficulty
    average_cooking_time = {
        difficulty: np.mean(times) for difficulty, times in difficulty_data.items()
    }

    # Prepare data for plotting
    difficulties = list(average_cooking_time.keys())
    avg_cooking_times = list(average_cooking_time.values())

    plt.switch_backend("AGG")  # Use the 'agg' backend for non-GUI environments
    plt.figure(figsize=(10, 6))  # Set figure size.

    # Create a line plot
    plt.plot(difficulties, avg_cooking_times, marker="o", linestyle="-", color="b")
    plt.title("Average Cooking Time by Difficulty")  # Set title.
    plt.xlabel("Difficulty Level")  # Set x-axis label.
    plt.ylabel("Average Cooking Time (minutes)")  # Set y-axis label.
    plt.xticks(rotation=45)  # Rotate x-axis labels if necessary.
    plt.grid(True)  # Enable grid for better readability.

    plt.tight_layout()  # Adjust layout.
    chart = get_graph()  # Convert the plot to a base64-encoded image.
    plt.close()  # Close the figure.
    return chart  # Return the image.
