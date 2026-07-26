# 1. Create a starting dictionary
user = {"name": "Alice", "age": 25, "role": "Admin"}

# 2. Get data safely (Returns None instead of crashing if key doesn't exist)
email = user.get("email")  # None
city = user.get("city", "Unknown")  # Returns "Unknown" (default value)

# 3. View keys, values, and pairs (Returns dynamic view objects)
all_keys = user.keys()  # dict_keys(['name', 'age', 'role'])
all_values = user.values()  # dict_values(['Alice', 25, 'Admin'])
all_pairs = user.items()  # dict_items([('name', 'Alice'), ...])

# 4. Add or update items in bulk
user.update({"role": "Superadmin", "status": "Active"})

# 5. Set default value (Adds key only if it does NOT already exist)
user.setdefault("status", "Offline")  # Keeps "Active" because it exists
user.setdefault("theme", "Dark")  # Adds "theme": "Dark"

# 6. Remove and return specific items
removed_role = user.pop("role")  # Removes 'role', returns 'Superadmin'
last_item = user.popitem()  # Removes and returns last inserted pair

# 7. Copy the dictionary (Shallow copy)
user_backup = user.copy()

# 8. Clear all items from a dictionary
user.clear()  # user becomes {}

# 9. Create a new dictionary from a list of keys
new_dict = dict.fromkeys(["id", "score", "level"], 0)  # {'id': 0, 'score': 0, 'level': 0}

# Print results to verify
print("Final user dict:", user)
print("Backup dict:", user_backup)
print("Fromkeys dict:", new_dict)
