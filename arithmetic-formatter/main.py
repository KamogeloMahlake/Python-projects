def arithmetic_arranger(problems, show_answers=False):
    top = []
    bottom = []
    line = []
    answer = []
    output = []
    if len(problems) > 5:
        return 'Error: Too many problems.'
    else:
        try:
            for i in problems:
                x, op, y =i.split()
                length = max(len(x), len(y)) + 2
                if op not in ["+", "-", "*", "/"]:
                    return f"Error: Operator must be '+' ,'-', '*', '/'."
                elif x.isdigit() == False or y.isdigit() == False:
                    return f"Error: Numbers must only contain digits."
                elif len(x) > 4 or len(y) > 4:
                    return f"Error: Numbers cannot be more than four digits."
                else:
                    x = int(x)
                    y = int(y)
                    top.append(f"{x:{length}}")
                    bottom.append(f"{op} {y:{length - 2}}")
                    line.append('-' * length)
                    if show_answers == True:
                        match op:
                            case "+":
                                ans = x + y
                            case "-":
                                ans = x - y
                            case "*":
                                ans = x * y
                            case "/":
                                try:
                                    ans = x / y
                                except ZeroDivisionError:
                                    return f"cannot divide by zero"
                        answer.append(f"{ans: {length}}") 
        except ValueError:
            return f"Error: Incorrect Format, for example 'x + y'."
    output.append("    ".join(top))
    output.append("    ".join(bottom))
    output.append("    ".join(line))
    if show_answers == True:
        output.append("    ".join(answer))
    return "\n".join(output) 

def main():
    problems = [] 
    try:
        i = int(input("Input how many problems you want to enter: "))
        while i > 0:
            problem = input("Input a arithmetic problem: ")
            problems.append(problem)
            i -= 1
    except ValueError:
        print("Enter correct number: ")
        pass


    else:
        while True:
            get_answer = input("Do you want an anwser?YES(Y) OR NO(N) ")
            if get_answer.lower() in ["yes", "y"]:
                print(arithmetic_arranger(problems, True))
                break
            elif get_answer.lower() in ["no", "n"]:
                print(arithmetic_arranger(problems))
                break
            else:
                pass

if __name__ == "__main__":
    main()
    
