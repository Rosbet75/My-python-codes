import random
from random import choice

friends = ["Alice",  "Bob", "Charlie", "David", "Emanuel"]


num = len(friends)

# choice = random.randint(0, num - 1)

# print(friends[choice])
print(random.choice(friends))

friends.extend(["ernesto", "aleman", "Carie"])

print(random.choice(friends))