import pandas as pd

class Problema:
    def __init__(self, finishing, table_file, net_file):
        self.table = pd.read_csv(table_file, index_col="TAREA")
        self.net = pd.read_csv(net_file)
        self.finish = finishing
        self.coeficients = []
        self.variables = []

    def calcular_cuch(self):
        self.table['CUCH'] = (self.table["C_CHOQUE"] - self.table["C_NORMAL"]) / (self.table["T_NORMAL"] - self.table["T_CHOQUE"])
        self.table['CUCH'] = self.table["CUCH"].fillna(0)
        self.coeficients = [self.format_term(x) for x in self.table["CUCH"]]
        self.variables = [f"y{chr(0x249C + i)}" for i in range(len(self.coeficients))]

    def format_term(self, value):
        if int(value) == value:
            return str(int(value))
        else:
            return f"{value:.2f}"

    def print_min_function(self):
        print("\nFuncion objetivo:")
        print("min", end=" ")
        for i in range(len(self.coeficients)):
            if i == len(self.coeficients) - 1:
                print(str(self.coeficients[i]) + self.variables[i])
            else:
                print(str(self.coeficients[i]) + self.variables[i], end=" + ")

    def print_limit_constraints(self):
        print("\nLimites")
        time_difference = self.table["T_NORMAL"] - self.table["T_CHOQUE"]
        time_difference = time_difference.values
        for i in range(len(self.variables)):
            print(f"0 {chr(0x2264)} {self.variables[i]}  {chr(0x2264)} {str(time_difference[i])}")

    def print_net_constraints(self):
        print("\nRestricciones de red:")
        i = 0
        for index, row in self.net.iterrows():
            origin = row['ORIGEN']
            destination = row['DESTINO']
            task = row['TAREA']
            if task in self.table.index:
                start_time = f"x{chr(8320 + origin)} + {self.table.loc[task, 'T_NORMAL']}"
                print(f"x{chr(8320 + destination)} {chr(0x2265)} {start_time} - y{chr(0x249C + i)}")
                i += 1
            else:
                start_time = f"x{chr(8320 + origin)} + 0"
                print(f"x{chr(8320 + destination)} {chr(0x2265)} {start_time}")

    def print_no_negativity_constraints(self):
        print("\nCondicion de no negatividad:")
        unique_nodes = set()
        for i in range(len(self.net)):
            origin = self.net.loc[i, 'ORIGEN']
            destination = self.net.loc[i, 'DESTINO']
            unique_nodes.add(origin)
            unique_nodes.add(destination)
        for idx, node in enumerate(unique_nodes):
            if idx == len(unique_nodes) - 1:
                print(f"x{chr(8320 + node)} {chr(0x2265)} 0")
            else:
                print(f"x{chr(8320 + node)}", end=", ")

        self.unique_nodes = unique_nodes


    def print_start_ending_constraints(self):
        print("\nRestricciones de inicio y terminacion:")
        print(f"x{chr(8320)} = 0, x{chr(8320 + len(self.unique_nodes))} {chr(0x2264)} {self.finish}")



