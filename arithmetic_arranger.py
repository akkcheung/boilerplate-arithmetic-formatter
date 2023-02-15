import re

def arithmetic_arranger(problems, solve = False):

  if(len(problems) > 5):
    return "Error: Too many problems."

  first = ""
  second = ""
  lines = ""
  sumx = ""

  for problem in problems:

    firstNumber = problem.split(" ")[0]
    operator = problem.split(" ")[1]
    secondNumber = problem.split(" ")[2]

    if not (firstNumber.isdigit() and secondNumber.isdigit()):
      return "Error: Numbers must only contain digits."
    if (re.search("[/]", operator) or re.search("[*]", operator)):
      return "Error: Operator must be '+' or '-'."

    if (len(firstNumber) > 4 or len(secondNumber) > 4):
      return "Error: Numbers cannot be more than four digits."

    sum = ""
    if (operator == "+"):
      sum = str(int(firstNumber) + int(secondNumber))
    elif (operator == "-"):
      sum = str(int(firstNumber) - int(secondNumber))
   
    length = max(len(firstNumber), len(secondNumber)) + 2
    top = str(firstNumber).rjust(length)
    bottom = operator + str(secondNumber).rjust(length - 1)
    line = ""
    res = str(sum).rjust(length)

    for s in range(length):
      line += "-"

    if problem != problems[-1]:
      first += top + '    '
      second += bottom + '    '
      lines += line + '    '
      sumx += res + '    '
    else:
      first += top
      second += bottom
      lines += line
      sumx += res

  if solve:
    string = first + "\n" + second + "\n" + lines + "\n" + sumx
  else:
    string = first + "\n" + second + "\n" + lines 
  return string


  return arranged_problems
