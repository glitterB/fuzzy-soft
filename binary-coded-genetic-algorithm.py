from math import log2, ceil
from random import random, randint
from typing import List

#calculating string length
def string_length(xmin: float, xmax: float, error: float) -> int:
    """
    Calculates the number of bits needed to represent a variable within a given range and precision.
    
    Parameters:
    - xmin (float): Minimum value of the variable.
    - xmax (float): Maximum value of the variable.
    - error (float): Desired precision (smallest distinguishable difference).
    
    Returns:
    - int: Number of bits required.
    """
    if xmax <= xmin:
        raise ValueError("xmax must be greater than xmin.")
    if error <= 0:
        raise ValueError("Error (precision) must be greater than 0.")
    
    return ceil(log2((xmax - xmin) / error))

#Generation of strings
def binary_string(length: int) -> str:
    """
    Generates a random binary string of a given length.
    
    Parameters:
    - length (int): Length of the binary string to generate.
    
    Returns:
    - str: A random binary string composed of '0's and '1's.
    """
    if length < 0:
        raise ValueError("Length must be non-negative.")
    
    return ''.join(str(randint(0, 1)) for _ in range(length))

#Fitness evaluation
def decode_binary(xmin: float, xmax: float, l: int, bin_str: str) -> float:
    """
    Decodes a binary string to a real number within the range [xmin, xmax].

    Parameters:
    - xmin (float): Minimum of the variable range.
    - xmax (float): Maximum of the variable range.
    - l (int): Length of the binary string.
    - bin_str (str): Binary string representing the variable.

    Returns:
    - float: Decoded real value.
    """
    if len(bin_str) != l:
        raise ValueError("Binary string length does not match specified bit length.")
    if not all(c in '01' for c in bin_str):
        raise ValueError("Binary string must only contain 0s and 1s.")
    
    decoded_value = int(bin_str, 2)
    precision = (xmax - xmin) / ((2 ** l) - 1)
    return xmin + decoded_value * precision

#Tournament selection
def reproduction(mating_pool: List[str], fitness_pool: List[float], q: int = 2) -> List[str]:
    """
    Performs tournament selection to generate a new mating pool.

    Parameters:
    - mating_pool (List[str]): List of binary strings (individuals).
    - fitness_pool (List[float]): Corresponding fitness values for each individual.
    - q (int): Tournament size (number of candidates per tournament). Default is 2.

    Returns:
    - List[str]: New mating pool selected via tournament.
    """
    if q <= 0:
        raise ValueError("Tournament size q must be positive.")
    if len(mating_pool) != len(fitness_pool):
        raise ValueError("Mating pool and fitness pool must be of the same length.")

    new_mating_pool = []
    pool_size = len(mating_pool)

    for _ in range(pool_size):
        selected_indices = [randint(0, pool_size - 1) for _ in range(q)]
        selected_fitnesses = [fitness_pool[i] for i in selected_indices]
        best_index_in_selected = selected_indices[selected_fitnesses.index(max(selected_fitnesses))]
        new_mating_pool.append(mating_pool[best_index_in_selected])

    return new_mating_pool


#Single point crossover
def single_point_crossover(mating_pool: List[str]) -> List[str]:
    """
    Performs single-point crossover on a mating pool.

    Parameters:
    - mating_pool (List[str]): List of binary strings representing individuals.

    Returns:
    - List[str]: New population (children) after crossover.
    """
    if len(mating_pool) % 2 != 0:
        raise ValueError("Mating pool size must be even for pairwise crossover.")

    l = len(mating_pool[0])
    if l < 2:
        raise ValueError("Binary string length must be at least 2 for crossover.")

    # Ensure all strings are of the same length
    if not all(len(ind) == l for ind in mating_pool):
        raise ValueError("All individuals must have the same length.")

    children = []
    half = len(mating_pool) // 2

    for i in range(half):
        parent_1 = mating_pool[i]
        parent_2 = mating_pool[-(i + 1)]
        crossover_point = randint(1, l - 1)

        child_1 = parent_1[:crossover_point] + parent_2[crossover_point:]
        child_2 = parent_2[:crossover_point] + parent_1[crossover_point:]
        
        children.append(child_1)
        children.append(child_2)

    return children

#Mutation
def mutation(mating_pool: List[str], p_mutation: float = 0.01) -> List[str]:
    """
    Applies bit-flip mutation to each bit of each individual in the mating pool.

    Parameters:
    - mating_pool (List[str]): List of binary strings (individuals).
    - p_mutation (float): Probability of flipping each bit. Default is 0.01.

    Returns:
    - List[str]: Mutated mating pool.
    """
    mutated_pool = []

    for individual in mating_pool:
        mutated = ''
        for bit in individual:
            if random() < p_mutation:
                mutated += '0' if bit == '1' else '1'
            else:
                mutated += bit
        mutated_pool.append(mutated)

    return mutated_pool
#-----------------------------------------------------------------------------

# Objective Function - maximize f(x) = sqrt(x)
x = lambda a: a**0.5
xmin = 1
xmax = 16
error = 1

# Calculate string length
l = string_length(xmin, xmax, error)

# GA parameters
initial_population = 6
generations = 20
mutation_rate = 0.01

# Initialize population
mating_pool = [binary_string(l) for _ in range(initial_population)]

# Track best solution
best_solution = None
best_fx = float('-inf')
best_bin = ""

# Begin Genetic Algorithm
for gen in range(generations):
    x_values = []
    fx_values = []

    for sol in mating_pool:
        decoded = decode_binary(xmin, xmax, l, sol)
        fitness_value = x(decoded)  # Maximization: use f(x) directly
        x_values.append(decoded)
        fx_values.append(fitness_value)

        # Track best solution so far
        if fitness_value > best_fx:
            best_fx = fitness_value
            best_solution = decoded
            best_bin = sol

    # Reproduction, Crossover, Mutation
    mating_pool = reproduction(mating_pool, fx_values)
    mating_pool = single_point_crossover(mating_pool)
    mating_pool = mutation(mating_pool, p_mutation=mutation_rate)

# Final Output
print("Best Binary String: ", best_bin)
print("Decoded x Value: ", best_solution)
print("Maximum f(x): ", best_fx)