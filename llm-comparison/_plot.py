import csv
import os
import matplotlib.pyplot as plt


def parse_connections_output(output_string):
    """Parses the comma-separated output from the LLM."""
    parts = output_string.split(",")
    if len(parts) != 16:
        return None
    categories = []
    for i in range(4):
        category_words = sorted(
            [word.lower().strip() for word in parts[i * 4 : i * 4 + 4]]
        )
        categories.append(category_words)
    return categories


def compare_categories(llm_categories, correct_categories):
    """Compares LLM's categories to the correct categories, ignoring order."""
    if llm_categories is None:
        return False
    correct = True
    for correct_words in correct_categories:
        found = False
        for llm_words in llm_categories:
            if sorted(llm_words) == sorted(correct_words):
                found = True
                break
        if not found:
            correct = False
            break
    return correct


def analyze_results(model_files, correct_results_file):
    """Analyzes the results from the CSV files."""
    results = {}
    with open(correct_results_file, "r") as f:
        reader = csv.reader(f)
        correct_data = list(reader)

    for model_file in model_files:
        model_name = os.path.splitext(os.path.basename(model_file))[0]
        results[model_name] = {"correct": 0, "total": 0}

        with open(model_file, "r") as f:
            reader = csv.reader(f)
            llm_data = list(reader)

        for i, llm_output in enumerate(llm_data):
            if i >= len(correct_data):
                break
            correct_categories = parse_connections_output(",".join(correct_data[i]))
            llm_categories = parse_connections_output(",".join(llm_output))

            if compare_categories(llm_categories, correct_categories):
                results[model_name]["correct"] += 1
            results[model_name]["total"] += 1

    return results


def plot_results(results):
    """Plots the results in a bar chart."""
    model_names = list(results.keys())
    success_rates = [
        results[model]["correct"] / results[model]["total"] for model in model_names
    ]

    plt.bar(model_names, success_rates)
    plt.xlabel("Models")
    plt.ylabel("Success Rate")
    plt.title("Connections Puzzle Performance")
    plt.ylim(0, 1)
    plt.show()


# Usage
model_files = [
    f
    for f in os.listdir(".")
    if f.endswith(".csv") and f not in ("_results.csv", "_inputs.csv")
]
correct_results_file = "_results.csv"
analysis_results = analyze_results(model_files, correct_results_file)
plot_results(analysis_results)
