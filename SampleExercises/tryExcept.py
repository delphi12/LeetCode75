
class oddException(Exception):
    items = []

    def __init__(self, i):
        self.items.append(i)

def read_files(file_path1, file_path2):
    try:
        # Reading and printing even lines from the first file
        with open(file_path1, 'r', encoding='utf-8') as file1:
            lines1 = file1.readlines()
            even_lines = [line.strip() for i, line in enumerate(lines1, start=1) if i % 2 == 0]
            print("Even lines from the first file:")
            for line in even_lines:
                print(line)

        # Reading and printing odd lines from the second file
        with open(file_path2, 'r', encoding='utf-8') as file2:
            lines2 = file2.readlines()
            odd_lines = [line.strip() for i, line in enumerate(lines2, start=1) if i % 2 != 0]
            print("Odd lines from the second file:")
            for line in odd_lines:
                print(line)

    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        file1.close()
        file2.close()


file_path1 = 'file1.txt'
file_path2 = 'file2.txt'

read_files(file_path1, file_path2)
