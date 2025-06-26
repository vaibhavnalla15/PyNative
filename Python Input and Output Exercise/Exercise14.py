""" Tabular Output from Lists """
# You have two lists: names = ["Alice", "Bob", "Charlie"] and scores = [85, 92, 78].
# Print these lists as a simple table with columns “Name” and “Score”.
# Hints :-
# 1. You’ll need to iterate through both lists simultaneously. You can use zip() to achieve this.
# 2. Then, use f-strings to format each row of the table.

names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]

print(f"{'Name':<10} {'Score':<5}")     # Left-align
print("-" * 16)

for name, score in zip(names, scores):
    print(f"{name:<10} {score:<5}")     # Left-align