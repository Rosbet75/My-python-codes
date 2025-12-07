student_scores = [123,4254,452,2341,7345,234,4652,3546,324,5,676,2345,2345,42,2345]

sum = 0
for score in student_scores:
    sum += score

print(sum)

print(f"valor maximo: {max(student_scores)}")
print(f"valor minimo: {min(student_scores)}")


max_score = 0

for score in student_scores:
    if score > max_score:
        max_score = score


print(f"my max alghorithm score says: {max_score}")

#gauss challenge
sum = 0
for i in range(1,101):
    sum += i
print(sum)