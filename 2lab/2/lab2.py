def find_sequence_term(x, eps):
    if eps <= 0:
        raise ValueError("Величина eps має бути більшою за 0")

    a_prev = x
    terms = [a_prev]
    for n in range(2, 101):
        a_curr = 2 * a_prev + (16 + x) / (4 + abs(a_prev**3))
        terms.append(a_curr)
        if abs(a_curr - a_prev) < eps:
            return a_curr, n, terms
        a_prev = a_curr
    return None, 100, terms


try:
    x_input = 1.0
    eps_input = 1

    val, index, terms = find_sequence_term(x_input, eps_input)

    print("Перші 10 членів послідовності:")
    for i, t in enumerate(terms[:10], start=1):
        print(f"a_{i} = {t}")

    print()
    if val is not None:
        print(f"a_n = {val}")
        print(f"n = {index}")
    else:
        print("Умова не виконалась за 100 ітерацій.")
except ValueError as e:
    print(f"Помилка: {e}")      ``````````````````````````````````````````````````````````````````````