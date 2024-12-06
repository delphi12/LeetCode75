from collections import defaultdict

def find_most_recurring_pattern(nested_list):
    pattern_counts = defaultdict(int)
    sequences = [' '.join(sublist) for sublist in nested_list]
    print(sequences)
    return " ", 0



nested_list = [["product", "checkout", "help"],
               ["help", "checkout", "product"],
               ["product", "product", "checkout", "help"],
               ["product", "help", "checkout", "product", "checkout","help"]]

pattern, frequency = find_most_recurring_pattern(nested_list)
print(f"The most recurring pattern is: '{pattern}' with a frequency of {frequency}")