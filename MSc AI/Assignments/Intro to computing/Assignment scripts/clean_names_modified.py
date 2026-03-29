# clean_names.py

# Function to process a list of names: remove duplicates, sort alphabetically, and convert to uppercase
def process_names(names):
    names = [name.upper() for name in names]  # Convert all names to uppercase for consistency
    unique_names = list(set(names))  # removes duplicates but doesn't preserve order
    unique_names.sort()  # sorts alphabetically
    return unique_names 

# Test list with duplicates and inconsistent capitalisation
test_names = ["Alice", "bob", "alice", "Charlie", "BOB", "dave", "Eve", "charlie"]

print("Original list:", test_names)
print("Processed list:", process_names(test_names))
