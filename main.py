# Scope Resolution

# variable scope = where a variable and accessible
# scope resolution = (LEGB) Local -> Enclosed -> Global -> Built-in

# ------------
# Local

def func1():
    x = 1
    print(x)

def func2():
    x = 2
    print(x)

func1()
func2()

# ------------
# Enclosed

def func3():
    y = 3

    def func4():
        print(y)
    func4()

func3()

# ------------
# Global

def func5():
    print(z)

def func6():
    print(z)

z = 5

func5()
func6()

# ------------
# Built-in

from math import e

def func7():
    print(e)

func7()