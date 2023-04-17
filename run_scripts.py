import subprocess
import time

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

def main():
    time_api()
    dbr_count()
if __name__ == '__main__':
    main()