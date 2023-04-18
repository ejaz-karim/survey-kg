import subprocess
import time
import pandas

def time_api():
    start_time = time.time()

    subprocess.run(['java', '-jar', 'sparql-anything-0.8.1.jar', '-q', 'query7.sparql', '-o', 'survey7.ttl'], check=True)

    subprocess.run(['python', 'data_extraction.py'], check=True)
    subprocess.run(['python', 'data_iteration.py'], check=True)

    end_time = time.time()
    elapsed_time = end_time - start_time

    print('Execution time: {:.2f} seconds'.format(elapsed_time))

def dbr_count():
    with open("survey7.ttl", 'r', encoding="utf-8") as file1, open("survey7_modified.ttl", 'r', encoding="utf-8") as file2:
        lines1 = file1.readlines()
        lines2 = file2.readlines()

    new_lines = [line for line in lines2 if line not in lines1]
    count = 0

    for line in new_lines:
        count = count + 1
    print("dbr:hasResource appears " + str(count) + " times, the expected number is 809")

def check_xlsx_column(column):
    df = pandas.read_excel("surveyExtraction.xlsx")
    data = df.iloc[:, column].astype(str).unique()
    with open("survey7_modified.ttl", "r", encoding="utf-8") as f:
        lines = f.readlines()
        lines = [line.replace('\\"', '"') for line in lines]
        not_present = [x for x in data if all(x not in line for line in lines)]
        if len(not_present) > 0:
            print(f"Not present:")
            for value in not_present:
                print(value)
        else:
            print(f"All data in column {column} is present in the .ttl file")

def main():
    time_api()
    dbr_count()
    check_xlsx_column(0)
    check_xlsx_column(1)
    check_xlsx_column(2)
    check_xlsx_column(3)

if __name__ == '__main__':
    main()