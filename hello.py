

def hello(txt:str)-> str:
    return txt[::-1]


if __name__=="__main__":
    print(hello("Hello"))