import math

def calculate_series(x, a, eps):
    if x == 0 or a == 0 or eps <= 0:
        raise ValueError("Invalid input: x and a must not be 0, eps must be > 0.")
        
    if a + x <= 0:
        raise ValueError("Domain error: (a + x) must be strictly greater than 0.")

    k = 0
    total_sum = 0.0
    ln_val = math.log(a + x)

    while True:
        numerator = ln_val ** (2 * k)
        denominator = (2 ** k) + math.factorial(k)
        
        term = numerator / denominator
        total_sum += term
        
        if abs(term) < eps:
            break
            
        k += 1

    return total_sum, k + 1

try:
    x_input = 1.5
    a_input = 3.0
    eps_input = 0.0001
    
    result_sum, count = calculate_series(x_input, a_input, eps_input)
    
    print(f"Sum of the series: {result_sum}")
    print(f"Number of terms included: {count}")
    
except ValueError as e:
    print(f"Error: {e}")