import os
import pathlib
import time
import psutil
import subprocess
import sys


def load_test_file(file_path):
    with open(file_path, encoding='utf-8') as file:
        return file.read().strip().splitlines()


DIR = pathlib.Path(__file__).parent.resolve()
tests = os.path.join(DIR, 'tests')
try:
    n_tests = len(os.listdir(tests)) // 2
    open('grouping_files.py', encoding='utf-8')
except FileNotFoundError:
    print('-' * 69, '\nОШИБКА 404')
    print('Папка с тестами должна называться - tests, а файл с кодом - my_code.py', '-' * 69, sep='\n')
    raise

python_version = 'python3' if sys.platform in {'linux', 'linux2', 'darwin'} else 'py'

for i in range(1, n_tests + 1):
    process = psutil.Process(os.getpid())
    start_time = time.time()

    test_data = load_test_file(os.path.join(tests, str(i)))
    correct = load_test_file(os.path.join(tests, f'{str(i)}.clue'))

    result_bytes = subprocess.run([python_version, "my_code.py"], input='\n'.join(test_data).encode('utf-8'),
                                  capture_output=True, encoding='utf-8').stdout
    result = result_bytes.strip().splitlines()

    if result != correct:
        print(f"Test#{i} Input:")
        print('\n'.join(test_data))
        print(f"Test#{i} Expected Output:")
        print('\n'.join(correct))
        print(f"Test#{i} Actual Output:")
        print('\n'.join(result))

    assert result == correct, f"Test#{i}\n{'-' * 69}\nexpect:{repr(correct)}\nresult:{repr(result)}\n"

    end_time = time.time()
    elapsed_time = end_time - start_time
    memory_usage = process.memory_info().rss / 1024 / 1024
    print(
        f'Тест №{i} пройден(✓), время выполнения: {elapsed_time:.2f} секунд, использовано памяти: {memory_usage:.2f} MB')
    time.sleep(0.5)