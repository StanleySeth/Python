#Functions with parameters
#They are values that get passed as arguments given to function inside of the parenthesis


def greeting(name):
    print(f"{name} Hello There.")

greeting("Stanley")
greeting("Seth")
greeting("Stanley")


print("==========================================================")
def message(name):
    print(f"Hello {name}. We shall be having a general meeting on date...Please avail yourself.Thank you")

message("Mark")
message("Melvin")

print("==========================================================")
def Addition(x, y):
    sum = x + y
    print(f"The sum of the numbers is:", sum)

Addition(50, 90)
