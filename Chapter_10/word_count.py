filename = 'alice.txt'
# alice.txt = '../pcc_2e/chapter_10/alice.txt'

def count_words(filename):
    """Count number of words in a file"""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
        # print(f"Sorry, the file {filename} does not exist.")
    else:
        # Count the approximate number of words in the file.
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")

# filename = '../pcc_2e/chapter_10/alice.txt'
# count_words(filename)
filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    count_words(filename)