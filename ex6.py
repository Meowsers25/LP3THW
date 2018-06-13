# variable
types_of_people = 10

# variable
x = f"There are {types_of_people} types of people."

# 2 more variables
binary = "binary"
do_not = "don't"

# string inside a string
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

# 2 more strings inside a string
print(f"I said: {x}")
print(f"I also said: '{y}'")

# boolean variable
hilarious = False

# string inside a string
joke_evaluation = "Isn't that joke so funny?! {}"

# example of .format()
print(joke_evaluation.format(hilarious))

# 2 more variables
w = "This is the left side of..."
e = "a string with a right side."

# concat
print(w + e)