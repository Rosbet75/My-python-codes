def my_function():
    print("hello world")
    print("hello again")
    print("hello again again")

my_function()

def calculate_love_score(*args):
    love = "love"
    true = "true"
    true_sum = 0
    love_sum = 0
    for x in args:
        for i in x:
            if i in love:
                love_sum += 1
            if i in true:
                true_sum += 1
    print(f"{true_sum}{love_sum}")

calculate_love_score("James Carl", "Brandon Von Daugh")