from test_framework import generic_test


def majority_search(stream):
    majority_count = 0
    current_char = None
    for char in stream:
        if current_char == char or current_char is None:
            current_char = char
            majority_count += 1
        else:
            majority_count -= 1
            if majority_count == 0:
                current_char = None
        
    return current_char


def majority_search_wrapper(stream):
    return majority_search(iter(stream))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("majority_element.py",
                                       'majority_element.tsv',
                                       majority_search_wrapper))
