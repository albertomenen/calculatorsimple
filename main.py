from art import logo


#Sumar
def add(n1,n2):
  return n1 + n2

#Restar

def substract (n1,n2):
  return n1 - n2

#Multiplicar

def multiply(n1, n2):
  return n1 * n2

#Dividir

def divide(n1,n2):
  return n1 / n2


operations ={
  "+": add,
  "-": substract,
  "*": multiply,
  "/": divide

}

def calculator():
  print (logo)

  num1 = float(input("Cual es el primer numero?"))
  for symbol in operations:
    print(symbol)

  should_continue = True

  while should_continue:
    operation_symbol = input("Escoge una de las operaciones: ")

    num2 = float(input("Cual es el siguiente numero?"))

    calculation_function = operations [operation_symbol]

    answer = calculation_function(num1,num2)

    print (f"{num1} {operation_symbol} {num2} = {answer}")
  if input ("Teclea 's' para continuar operando con {answer} o teclea 'n' para empezar un nuevo calculo ") == "s":
    num1 = answer
  else :
    should_continue = False
    calculator()

calculator()
