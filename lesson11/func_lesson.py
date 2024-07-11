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

def cal_tri(width=100, height=100):
    return (width * height) / 2

result = cal_tri(width=10, height=5)
print(result)

result = cal_tri()
print(result)