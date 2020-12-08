import math
import cmath
import random as rand
import argparse

a = 1

rpn = ""
variables = {}
operators = {
	"quit": {"operands": 0, "function": "exit"},
	"exit": {"operands": 0, "function": "exit"},
	"rand": {"operands": 0, "function": "random"},
	"random": {"operands": 0, "function": "random"},
	"sin": {"operands": 1, "function": "sin"},
	"sine": {"operands": 1, "function": "sin"},
	"cos": {"operands": 1, "function": "cos"},
	"cosine": {"operands": 1, "function": "cos"},
	"tan": {"operands": 1, "function": "tan"},
	"tangent": {"operands": 1, "function": "tan"},
	"sec": {"operands": 1, "function": "sec"},
	"secant": {"operands": 1, "function": "sec"},
	"cosec": {"operands": 1, "function": "cosec"},
	"cosecant": {"operands": 1, "function": "cosec"},
	"cot": {"operands": 1, "function": "cot"},
	"cotangent": {"operands": 1, "function": "cot"},
	"asin": {"operands": 1, "function": "arcsin"},
	"arcsin": {"operands": 1, "function": "arcsin"},
	"arcsine": {"operands": 1, "function": "arcsin"},
	"acos": {"operands": 1, "function": "arccos"},
	"arccos": {"operands": 1, "function": "arccos"},
	"arccosine": {"operands": 1, "function": "arccos"},
	"atan": {"operands": 1, "function": "arctan"},
	"arctan": {"operands": 1, "function": "arctan"},
	"arctangent": {"operands": 1, "function": "arctan"},
	"sinh": {"operands": 1, "function": "sinh"},
	"cosh": {"operands": 1, "function": "cosh"},
	"tanh": {"operands": 1, "function": "tanh"},
	"asinh": {"operands": 1, "function": "arsinh"},
	"arsinh": {"operands": 1, "function": "arsinh"},
	"acosh": {"operands": 1, "function": "arcosh"},
	"arcosh": {"operands": 1, "function": "arcosh"},
	"atanh": {"operands": 1, "function": "artanh"},
	"artanh": {"operands": 1, "function": "artanh"},
	"!": {"operands": 1, "function": "factorial"},
	"abs": {"operands": 1, "function": "absolute"},
	"absolute": {"operands": 1, "function": "absolute"},
	"mod": {"operands": 1, "function": "absolute"},
	"phase": {"operands": 1, "function": "phase"},
	"sqrt": {"operands": 1, "function": "sqrt"},
	"cbrt": {"operands": 1, "function": "cbrt"},
	"ln": {"operands": 1, "function": "ln"},
	"root": {"operands": 2, "function": "root"},
	"log": {"operands": 2, "function": "log"},
	"+": {"operands": 2, "function": "add"},
	"add": {"operands": 2, "function": "add"},
	"plus": {"operands": 2, "function": "add"},
	"-": {"operands": 2, "function": "subtract"},
	"minus": {"operands": 2, "function": "subtract"},
	"subtract": {"operands": 2, "function": "subtract"},
	"*": {"operands": 2, "function": "multiply"},
	"times": {"operands": 2, "function": "multiply"},
	"multiply": {"operands": 2, "function": "multiply"},
	"/": {"operands": 2, "function": "divide"},
	"divide": {"operands": 2, "function": "divide"},
	"^": {"operands": 2, "function": "power"},
	"power": {"operands": 2, "function": "power"},
	"%": {"operands": 2, "function": "modulus"},
	"=": {"operands": 2, "function": "assign"},
	"!=": {"operands": 2, "function": "inequal"},
	"<>": {"operands": 2, "function": "inequal"},
	"==": {"operands": 2, "function": "equal"},
	">": {"operands": 2, "function": "greaterThan"},
	">=": {"operands": 2, "function": "greaterThanOrEqual"},
	"<": {"operands": 2, "function": "lessThan"},
	"<=": {"operands": 2, "function": "lessThanOrEqual"},
	"randint": {"operands": 2, "function": "randint"},
	"hypot": {"operands": 2, "function": "hypotenuse"},
	"hypotenuse": {"operands": 2, "function": "hypotenuse"},
	"C": {"operands": 2, "function": "combination"},
	"comb": {"operands": 2, "function": "combination"},
	"combination": {"operands": 2, "function": "combination"},
	"P": {"operands": 2, "function": "permutation"},
	"perm": {"operands": 2, "function": "permutation"},
	"permutation": {"operands": 2, "function": "permutation"},
}

constants = {
	"pi": cmath.pi,
	"π": "pi",
	"tau": cmath.tau,
	"τ": "tau",
	"e": cmath.e,
	"inf": cmath.inf,
	"∞": "inf",
	"infj": cmath.infj,
	"∞j": "infj",
	"phi": (1+cmath.sqrt(5))/2,
	"φ": "phi",
	"ϕ": "phi",
	"Φ": "phi",
	"em": 0.57721566490153286060651209008240243104215933593992,
	"euler-mascheroni": "em",
	"γ": "em",
	"feigenbaum": 4.669201609102990671853203821578,
	"feigenbaum-one": "feigenbaum",
	"δ": "feigenbaum",
	"feigenbaum-two": 2.502907875095892822283902873218,
	"α": "feigenbaum-two",
	"champernowne": 0.12345678910111213141516
}

def isInt(s):
	try:
		return float(s).is_integer()
	except ValueError:
		return False
	except OverflowError:
		return True

def isFloat(s):
	try:
		float(s)
		return True
	except ValueError:
		return False
	except OverflowError:
		return True

def isNumeric(s):
	try:
		complex(s)
		return True
	except ValueError:
		return False
	except OverflowError:
		return True

def containsNumbers(s):
	if isNumeric(s):
		return True
	else:
		for c in s:
			if isNumeric(c):
				return True
	return False

def extract(s):
	if s in constants.keys():
		while s in constants.keys():
			s = constants[s]
		if not isNumeric(s) or type(s) == bool:
			return s
		else:
			return complex(s)
	else:
		while s in variables.keys():
			s = variables[s]
		if not isNumeric(s) or type(s) == bool:
			return s
		else:
			return complex(s)

def format(s):
	if type(s) == bool:
		return str(s)
	elif isNumeric(s):
		if isInt(s.real):
			r = str(int(s.real))
		else:
			r = str(s.real)
			
		if isInt(s.imag):
			i = str(int(s.imag))
		else:
			i = str(s.imag)
		
		if i == "0":
			return r
		elif r == "0":
			if i == "1":
				return "j"
			else:
				return i + "j"
		else:
			return r + " " + i + "j +"
	else:
		return s

def assign(o, v):
	if not containsNumbers(o[0]) and o[0] not in constants.keys():
		variables[o[0]] = complex(v[1])
		return variables[o[0]], False
	else:
		return "Cannot assign to constant", True

def equal(x, y):
	return x == y, False

def inequal(x, y):
	return x != y, False

def greaterThan(x, y):
	if x.imag == 0 and y.imag == 0:
		return x.real > y.real, False
	else:
		return "Cannot compare complex numbers", True

def greaterThanOrEqual(x, y):
	if x.imag == 0 and y.imag == 0:
		return x.real >= y.real, False
	else:
		return "Cannot compare complex numbers", True

def lessThan(x, y):
	if x.imag == 0 and y.imag == 0:
		return x.real < y.real, False
	else:
		return "Cannot compare complex numbers", True

def lessThanOrEqual(x, y):
	if x.imag == 0 and y.imag == 0:
		return x.real <= y.real, False
	else:
		return "Cannot compare complex numbers", True

def add(x, y):
	return x + y, False

def subtract(x, y):
	return x - y, False
	
def multiply(x, y):
	return x * y, False

def divide(x, y):
	if y == 0:
		return "Cannot divide by zero", True
	else:
		return x / y, False

def power(x, y):
	return x ** y, False

def modulus(x, y):
	return x % y, False

def root(x, y):
	if y.imag == 0 and y.real < 0:
		return complex(0, root(x, -y.real)[0]), False
	else:
		return power(y, divide(1, x)[0])

def sqrt(x):
	return root(2, x)

def cbrt(x):
	return root(3, x)

def log(x, y):
	if x == 0:
		return "Logarithm of 0 is undefined", True
	else:
		return cmath.log(y, x), False

def ln(x):
	if x == 0:
		return "Natural logarithm of 0 is undefined", True
	else:
		return cmath.log(x), False

def sin(x):
	return cmath.sin(x*a), False

def cos(x):
	return cmath.cos(x*a), False

def tan(x):
	return cmath.tan(x*a), False

def sec(x):
	return divide(1, cos(x)[0])

def cosec(x):
	return divide(1, sin(x)[0])

def sec(x):
	return divide(1, tan(x)[0])

def arcsin(x):
	return a*cmath.asin(x), False

def arccos(x):
	return a*cmath.acos(x), False

def arctan(x):
	return a*cmath.atan(x), False

def sinh(x):
	return cmath.sinh(x), False

def cosh(x):
	return cmath.cosh(x), False

def tanh(x):
	return cmath.tanh(x), False

def arsinh(x):
	return cmath.asinh(x), False

def arcosh(x):
	return cmath.acosh(x), False

def hypotenuse(x, y):
	return (x*x + y*y)**(1/2), False

def factorial(x):
	if x.imag == 0:
		r = x.real
		if r < 0:
			return "Factorial argument must be positive", True
		if r == 0:
			return 1, False
		if isInt(r):
			fact = 1
			for i in range(1, int(r)+1):
				fact *= i
			return fact, False
		else:
			return "Factorial argument must be a real integer", True
	else:
		return "Factorial argument must be a real integer", True

def random():
	return rand.random(), False

def randint(x, y):
	return rand.randint(x, y), False

def absolute(x):
	return abs(x), False

def phase(x):
	return cmath.phase(x), False

def combination(n, r):
	nFact, error = factorial(n)
	if error:
		return nFact, error
	rFact, error = factorial(r)
	if error:
		return rFact, error
	nrFact, error = factorial(n-r)
	if error:
		return nrFact, error
	return divide(nFact, rFact * nrFact)

def permutation(n, r):
	nFact, error = factorial(n)
	if error:
		return nFact, error
	nrFact, error = factorial(n-r)
	if error:
		return nrFact, error
	return divide(nFact, nrFact)

def calculate(v, o, term):
	operator = operators[term]
	functionCall = operator["function"] + "("
	for i in range(len(v)):
		value = str(v[i])
		if not isNumeric(value):
			value = "\"" + value + "\""
		functionCall += value
		if i < len(v)-1:
			functionCall += ", "
	functionCall += ")"
	
	if term == "=":
		functionCall = operator["function"] + "(o, v)"
	
	try:
		return eval(functionCall)
	except TypeError:
		error = "Cannot apply " + term + " to "
		for value in v:
			error += format(value) + " "
		return error, True

parser = argparse.ArgumentParser(description = "A command-line reverse Polish notation calculator")
parser.add_argument("-i", "--input", nargs = 1, dest = "input", help = "Specify a input file containing calculations")
parser.add_argument("-a", "--angle", nargs = 1, dest = "angle", help = "Specify the angle unit to use", default = "r", choices = ["r", "d", "g"])
args = parser.parse_args()
inputFilePath = args.input

lines = []
if inputFilePath != None:
	try:
		f = open(inputFilePath[0])
		lines = f.readlines()
		f.close()
	except FileNotFoundError as msg:
		print("Could not read input file " + inputFilePath[0])
		exit()

if args.angle[0] == 'd':
	a = (2*cmath.pi)/360
elif args.angle[0] == 'g':
	a = (2*cmath.pi)/400
else:
	a = 1

while True:
	rpn = ""
	if len(lines) > 0:
		rpn = lines.pop(0).rstrip("\n") + " "
		print("[<] " + rpn)
	else:
		rpn = input("[<] ") + " "
	stack = []
	term = ""
	errors = []
	for c in rpn:
		if c == " " and term != "":
			if containsNumbers(term) and not isNumeric(term):
				errors.append("Cannot mix numbers and letters")
			else:
				if term in operators.keys():
					opCount = operators[term]["operands"]
					if len(stack) < opCount:
						errors.append(term + " does not have enough operands")
					else:
						o = []
						v = []
						for i in range(opCount):
							operand = stack.pop()
							o.insert(0, operand)
							value = extract(operand)
							if not (i == opCount-1 and term == "=") and not isNumeric(value):
								errors.append(operand + " is undefined")
								break
							else:
								v.insert(0, value)
						if errors == []:
							result, error = calculate(v, o, term)
							if error:
								errors.append(result)
							else:
								stack.append(result)
				elif isNumeric(term):
					stack.append(complex(term))
				else:
					stack.append(term)
			term = ""
		elif c != " ":
			term += c
	
	results = []
	
	for item in stack:
		value = extract(item)
		if not isNumeric(value):
			errors.append(item + " is undefined")
		else:
			results.append(item)
	
	if len(results) > 1:
		errors.append("Not enough operators present")
	
	if errors != []:
		for error in errors:
			print("[>] Error: " + error)
	elif results != []:
		print("[>] " + format(extract(results[0])))
	else:
		print("[>] ")
