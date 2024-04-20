import pandas as pd

def format_term(value):
    # Formatear el valor eliminando los decimales si son enteros o limitando los decimales a 2 si hay decimales
    if int(value) == value:
        return str(int(value))
    else:
        return f"{value:.2f}"

def print_min_function(coeficients, variables):
    print("\nFuncion objetivo:")
    print("min", end=" ")
    for i in range(len(coeficients)):
        if i == len(coeficients) - 1:
            print(str(coeficients[i]) + variables[i])
        else:
            print(str(coeficients[i]) + variables[i], end=" + ")


def print_limit_constraints(coeficients, variables):
    print("\nLimites")
    for i in range(len(variables)):
        print("0 <= " + variables[i] + " <= " + coeficients[i])

def print_net_constraints():
    return 1

def main():
    # Leer el archivos csv asociados a la informacion del problema
    table = pd.read_csv("table.csv")
    net = pd.read_csv("net.csv")

    # Calcular el coeficiente de costo unitario de choque (CUCH)
    table['CUCH'] = (table["C_CHOQUE"] - table["C_NORMAL"]) / (table["T_NORMAL"] - table["T_CHOQUE"])
    table['CUCH'] = table["CUCH"].fillna(0)

    # Dejar coeficientes y variables en arrays para futuras soluciones
    coeficients = [format_term(x) for x in table["CUCH"]]
    variables = [f"y{chr(8320 + i)}" for i in range(len(coeficients))]  # Usando Unicode para subíndices

    print_min_function(coeficients, variables)
    print_limit_constraints(coeficients, variables)

main()
