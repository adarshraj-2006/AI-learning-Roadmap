'''mod.py'''

def mult(*args):
    resu=1

    for num in args:
        resu *= num
        print(f"The answer is {resu}")
def add(*args):
    resu=0
    for num in args:
        resu += num
        print(f"The answer is {resu}")
def use():
    print("This is a module containing multiplication and addition functions.")

