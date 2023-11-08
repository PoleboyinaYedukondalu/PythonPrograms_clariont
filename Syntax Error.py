# simple example for SyntaxError :

def syError():
    try:
        "print('Hello, World!')"=code
        print(code)  
    except SyntaxError as e:
        print(f"SyntaxError: {e}")
syError()
