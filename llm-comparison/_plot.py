import csv
import os
import matplotlib.pyplot as plt


def parse_csv(file_name):
    with open(file_name, "r") as f:
        reader = csv.reader(f)
        csv_data = list(reader)

    res = list()
    for row in csv_data:
        if len(row) != 16:
            raise ValueError(f"Row {row} has {len(row)} columns, expected 16")
        line = list()
        for i in range(4):
            line.append(
                tuple(sorted(word.lower().strip() for word in row[i * 4 : i * 4 + 4]))
            )
        res.append(line)

    return res


def count_identical_lines(a, b):
    return sum(
        int(
            all(
                a_group == b_group
                for a_group, b_group in zip(sorted(a_line), sorted(b_line))
            )
        )
        for a_line, b_line in zip(parse_csv(a), parse_csv(b))
    )


def analyze_all_csvs():
    correct_results_file = "_results.csv"
    return {
        f.removesuffix(".csv"): count_identical_lines(f, correct_results_file)
        for f in os.listdir(".")
        if f.endswith(".csv") and f not in ("_results.csv", "_inputs.csv")
    }


def plot_results(results):
    """Plots the results in a horizontal bar chart and saves to file."""
    model_names = sorted(results.keys(), reverse=True)
    success_counts = [results[model] for model in model_names]

    plt.figure(figsize=(10, 6))
    plt.barh(model_names, success_counts)

    plt.axvline(x=10, color="gray", linestyle=":", alpha=0.7)

    plt.ylabel("Models")
    plt.xlabel("Correct Answers (out of 10)")
    plt.title("Connections Puzzle Performance")
    plt.xlim(0, 11)
    plt.xticks(range(0, 11))

    plt.savefig("plot.png", bbox_inches="tight", dpi=300)
    plt.close()


plot_results(analyze_all_csvs())
