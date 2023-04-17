import os
import time

start_time = time.time()

os.system('java -jar sparql-anything-0.8.1.jar -q query7.sparql -o survey7.ttl')

os.system('python data_extraction.py')
os.system('python data_iteration.py')

end_time = time.time()
elapsed_time = end_time - start_time

print('Execution time: {:.2f} seconds'.format(elapsed_time))
