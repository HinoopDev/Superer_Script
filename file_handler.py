import error

def get(file:str)->str:
    try: 
        with open(file, "r") as f: content = f.read()
    except FileNotFoundError: 
        print(error.FileNotFound(file))
        content = ""
    return content

def push(file:str, content:str)->None:
    try: 
        with open(file, "w") as f: print(f.write(content))
    except FileNotFoundError: print(error.DirNotFound(file))