from helper import Problema

def main():
    problem = Problema(17, "table.csv", "net.csv")
    problem.calcular_cuch()
    problem.print_min_function()
    problem.print_limit_constraints()
    problem.print_net_constraints()
    problem.print_no_negativity_constraints()
    problem.print_start_ending_constraints()
main()