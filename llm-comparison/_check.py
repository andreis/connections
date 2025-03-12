import csv

def verify_csv_files(inputs_file, results_file):
    """Verifies that the sorted words in each row of the two CSV files are identical."""

    with open(inputs_file, 'r') as f_inputs, open(results_file, 'r') as f_results:
        reader_inputs = csv.reader(f_inputs)
        reader_results = csv.reader(f_results)

        for row_num, (row_inputs, row_results) in enumerate(zip(reader_inputs, reader_results)):
            sorted_inputs = sorted(row_inputs)
            sorted_results = sorted(row_results)

            if sorted_inputs != sorted_results:
                print(f"Error: Rows {row_num + 1} do not match.")
                print(f"  Inputs: {sorted_inputs}")
                print(f"  Results: {sorted_results}")
                return False

        print("Verification successful: All rows match.")
        return True

# Usage
inputs_file = '_inputs.csv'
results_file = '_results.csv'
verify_csv_files(inputs_file, results_file)