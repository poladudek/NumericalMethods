import numpy as np 

matrix_A1 = np.array([5.8267103432, 1.0419816676, 0.4517861296, -0.2246976350, 0.7150286064,
1.0419816676, 5.8150823499, -0.8642832971, 0.6610711416, -0.3874139415,
0.4517861296, -0.8642832971, 1.5136472691, -0.8512078774, 0.6771688230,
-0.2246976350, 0.6610711416, -0.8512078774, 5.3014166511, 0.5228116055,
0.7150286064, -0.3874139415, 0.6771688230, 0.5228116055, 3.5431433879])

matrix_A1 = matrix_A1.reshape(5, 5)

matrix_A2 = np.array([5.4763986379, 1.6846933459, 0.3136661779, -1.0597154562, 0.0083249547,
1.6846933459, 4.6359087874, -0.6108766748, 2.1930659258, 0.9091647433,
0.3136661779, -0.6108766748, 1.4591897081, -1.1804364456, 0.3985316185,
-1.0597154562, 2.1930659258, -1.1804364456, 3.3110327980, -1.1617171573,
0.0083249547, 0.9091647433, 0.3985316185, -1.1617171573, 2.1174700695])

matrix_A2 = matrix_A2.reshape(5, 5)

vector_b = np.transpose(np.array([-2.8634904630, -4.8216733374, -4.2958468309, -0.0877703331, -2.0223464006]))


x = np.linalg.solve(matrix_A1, vector_b) 
y = np.linalg.solve(matrix_A2, vector_b)
print(f"\n\nWynik rownania A1x = b: x = {x}\n")
print(f"Wynik rownania A2x = b: x = {y}")
print("-----\n\n")


#generowanie losowego wektora o wymiarze 5 na 1
gaussian_vector = np.random.normal(loc=0, scale=1, size=5)

#ustawianie skali aby uzyskac oczekiwana norme
scale = np.random.uniform(1e-5, 1e-7)

initial_norm = np.linalg.norm(gaussian_vector)

gaussian_vector /= initial_norm
gaussian_vector *= scale

final_norm = np.linalg.norm(gaussian_vector)

gaussian_vector = np.transpose(gaussian_vector)

#wygenerowane zaburzenie:
print(f"Losowo wygenerowane zaburzenie delta b := {gaussian_vector}\n")
print(f"Jego norma euklidesowa := {final_norm}\n\n")
print("-----\n\n")


#nowy wektor z zaburzeniem
vec_b_with_gaussian_vec = np.add(vector_b, gaussian_vector)

x = np.linalg.solve(matrix_A1, vec_b_with_gaussian_vec)
y = np.linalg.solve(matrix_A2, vec_b_with_gaussian_vec)

print(f"Wynik rownania A1x = b' (z zaburzeniem wektora wyrazow wolnych): x = {x}\n")
print(f"Wynik rownania A2x = b' (z zaburzeniem wektora wyrazow wolnych): x = {y}\n\n")
print("-----\n\n")


#sprawdzanie uwarunkowania 
err_A1 = np.linalg.cond(matrix_A1, 2)
err_A2 = np.linalg.cond(matrix_A2, 2)
print(f"Uwarunkowanie macierzy A1: {err_A1}, uwarunkowanie macierzy A2: {err_A2}\n\n")
