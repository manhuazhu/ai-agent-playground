"""Summarize reaction-time data by experimental group."""
import csv
import statistics
from collections import defaultdict

DATA_PATH = "data/reaction_times.csv"


def load_groups(path):
    groups = defaultdict(list)
    with open(path, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            groups[row["group"]].append(float(row["response_time_ms"]))
    return groups


def main():
    groups = load_groups(DATA_PATH)
    for name, values in groups.items():
        print(f"{name}: n={len(values)}, mean={statistics.mean(values):.1f} ms")


if __name__ == "__main__":
    main()
