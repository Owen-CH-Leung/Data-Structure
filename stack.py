def factorial(n):
    global result
    if n == 1:
        print('Reached base case n = 1')
        result = 1
        return result
    else:
        print(f"Calling function n = {n}")
        result = n * factorial(n-1)
        print(f"Result for n = {n} : {result}")
        return result

if __name__ == '__main__':
    factorial(9)