# Initialize a starting list
fruits = ["apple", "banana", "cherry"]
print(f"Original list: {fruits}\n")

# --- 1. ADDING ELEMENTS ---

# append(): Adds an element to the end of the list
fruits.append("orange")
print(f"After append(): {fruits}")

# insert(): Adds an element at a specific index (index, element)
fruits.insert(1, "blueberry")
print(f"After insert(): {fruits}")

# extend(): Appends elements from another iterable (like a list) to the end
more_fruits = ["mango", "grapes"]
fruits.extend(more_fruits)
print(f"After extend(): {fruits}\n")


# --- 2. REMOVING ELEMENTS ---

# remove(): Removes the first occurrence of a specific value
fruits.remove("banana")
print(f"After remove(): {fruits}")

# pop(): Removes and returns the element at a given index (defaults to the last item)
popped_item = fruits.pop(2)
print(f"After pop():    {fruits} (Popped item: '{popped_item}')")


# --- 3. SEARCHING AND COUNTING ---

# index(): Returns the index of the first occurrence of a value
cherry_index = fruits.index("cherry")
print(f"Index of 'cherry': {cherry_index}")

# count(): Returns the number of times a value appears in the list
fruits.append("apple")  # Add a duplicate for demonstration
apple_count = fruits.count("apple")
print(f"Count of 'apple':  {apple_count}\n")


# --- 4. ORDERING AND REVERSING ---

# reverse(): Reverses the order of the elements in place
fruits.reverse()
print(f"After reverse(): {fruits}")

# sort(): Sorts the list in place (alphabetically/numerically)
fruits.sort()
print(f"After sort():    {fruits}\n")


# --- 5. COPYING AND CLEARING ---

# copy(): Returns a shallow copy of the list
fruits_copy = fruits.copy()
print(f"Copied list:     {fruits_copy}")

# clear(): Removes all elements from the list
fruits.clear()
print(f"After clear():   {fruits}")
print(f"Verified copy remains: {fruits_copy}")
