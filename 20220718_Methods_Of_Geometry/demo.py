
def div(n:int, divisor:int, t:int=0) -> int:
    return t if n < divisor else div(n // divisor, divisor, t + 1)

print(div(100, 2))
