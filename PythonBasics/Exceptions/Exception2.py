ItemsInCart = 0
#2 items will be added to cart

if ItemsInCart != 2:
    pass

assert(ItemsInCart == 0)

try:
    with open('filelog.txt', 'r') as reader:
        reader.read()
except:
    print("Some how i reached this block because there is a failure in try block")


try:
    with open('filelog.txt', 'r') as reader:
        reader.read()
except Exception as e:
    print(e)

finally:
    print("cleaning up resources.. This execute always")