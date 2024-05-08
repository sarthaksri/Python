import random
import math

def evaluate_solution(solution):
    clauses = [((not solution[0]) or solution[3]),
               (solution[2] or solution[1]),
               ((not solution[2]) or (not solution[3])),
               ((not solution[3]) or (not solution[1])),
               ((not solution[0]) or (not solution[3]))]
    return sum(clauses)

def movegen(solution):
    var_index = random.randint(0, len(solution)-1)
    solution_copy = solution[:]
    solution_copy[var_index] = not solution_copy[var_index]
    return solution_copy

def accept_bad_move(delta, temperature):
    if delta < 0:
        return True
    probability = math.exp(-delta / temperature)
    return random.random() < probability

def simulated_annealing():
    T=500
    cooling_factor=50
    current_solution=[True,True,True,True]
    current_energy=evaluate_solution(current_solution)
    best_solution=current_solution[:]
    best_energy=current_energy
    while T>0:
        for _ in range(cooling_factor):
            new_solution=movegen(current_solution)
            new_energy=evaluate_solution(new_solution)
            delta=new_energy-current_energy
            if delta>0 or accept_bad_move(delta, T):
                current_solution=new_solution[:]
                current_energy=new_energy
                if new_energy>best_energy:
                    best_solution=new_solution[:]
                    best_energy=new_energy
        T-=1
    return best_solution

random.seed(42)
best_solution=simulated_annealing()
print("Best Solution:",best_solution)
print("Clauses satisfied:",evaluate_solution(best_solution))