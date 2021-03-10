def arithmetic_arranger(problems, result=False):
    count = 1

    if len(problems) > 5:
        return "Error: Too many problems."

    line_1 = ""
    line_2 = ""
    dash_line = ""
    ans_line = ""

    for problem in problems:
        chars = problem.split()

        try:
            num1 = int(chars[0])
            operator = chars[1]
            num2 = int(chars[2])
        except Exception:
            return "Error: Numbers must only contain digits."

        if len(chars[0]) > 4 or len(chars[2]) > 4:
            return "Error: Numbers cannot be more than four digits."

        if operator == '+':
            answer = num1 + num2
        elif operator == '-':
            answer = num1 - num2
        else:
            return "Error: Operator must be '+' or '-'."

        width = max(len(chars[0]), len(chars[2])) + 2

        line_1 += str(num1).rjust(width)
        line_2 += operator + str(num2).rjust(width-1)
        dash_line += str("-" * width)
        ans_line += str(answer).rjust(width)

        if count < len(problems):
            line_1 += "    "
            line_2 += "    "
            dash_line += "    "
            ans_line += "    "

        count += 1

    if result:
        arranged_problems = f"{line_1}\n{line_2}\n{dash_line}\n{ans_line}"
    else:
        arranged_problems = f"{line_1}\n{line_2}\n{dash_line}"

    return arranged_problems
