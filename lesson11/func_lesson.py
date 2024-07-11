def say_hello():
    print("Hello")

# say_hello()
# say_hello()
# say_hello()

def say_hello2(name):
    print(f"Hello {name}-san")

say_hello2(name="bob")

def cal_square(width):
    # print(width * width)
    return width * width

result = cal_square(width=10)
print(result)