import argparse


def analyze_logs(log_file):
    """Reads a log file and counts 'ERROR' occurrences."""
    error_count = 0
    with open(log_file, "r") as file:
        for line in file:
            if "ERROR" in line:
                error_count += 1
    print(f"Total Errors Found: {error_count}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Analyze log files for errors.")
    parser.add_argument("log_file", help="Path to the log file")
    args = parser.parse_args()
    analyze_logs(args.log_file)
