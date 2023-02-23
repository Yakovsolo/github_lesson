def add(x: int, y: int) -> int:
    return x + y

def sub(x: int, y: int) -> int:
    return x - y
    
def prod(x: int, y: int) -> int:
    return x * y
    
def div(x: int, y: int) -> float:
    return x / y

def hello(txt:str)-> str:
    return txt[::-1]


if __name__=="__main__":
    print(hello("Hello"))
