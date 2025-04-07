import numpy as np
import time

def scalar_vector_addition(vector, scalar):
    """Performs scalar-vector addition using scalar operations."""
    result = []
    for element in vector:
        result.append(element + scalar)
    return result

def vector_vector_addition(vector1, vector2):
    """Performs vector-vector addition using scalar operations."""
    result = []
    for i in range(len(vector1)):
        result.append(vector1[i] + vector2[i])
    return result

def vector_addition_numpy(vector1, vector2):
    """Performs vector-vector addition using NumPy's vectorized operations."""
    return np.array(vector1) + np.array(vector2)

def scalar_addition_numpy(vector, scalar):
  """Performs scalar-vector addition using numpy's vectorized operations"""
  return np.array(vector) + scalar

# Simulation Parameters
vector_size = 1000000
scalar_value = 5
vector1 = list(range(vector_size))
vector2 = list(range(vector_size, 2 * vector_size))

# Scalar Operations
start_time_scalar_vector = time.time()
result_scalar_vector = scalar_vector_addition(vector1, scalar_value)
end_time_scalar_vector = time.time()
scalar_vector_time = end_time_scalar_vector - start_time_scalar_vector

start_time_scalar_vector_np = time.time()
result_scalar_vector_np = scalar_addition_numpy(vector1, scalar_value)
end_time_scalar_vector_np = time.time()
scalar_vector_time_np = end_time_scalar_vector_np - start_time_scalar_vector_np

start_time_scalar_vector_np = time.time()
result_scalar_vector_np = scalar_addition_numpy(vector1, scalar_value)
end_time_scalar_vector_np = time.time()
scalar_vector_time_np = end_time_scalar_vector_np - start_time_scalar_vector_np

start_time_scalar_vector_np = time.time()
result_scalar_vector_np = scalar_addition_numpy(vector1, scalar_value)
end_time_scalar_vector_np = time.time()
scalar_vector_time_np = end_time_scalar_vector_np - start_time_scalar_vector_np

start_time_vector_vector = time.time()
result_vector_vector = vector_vector_addition(vector1, vector2)
end_time_vector_vector = time.time()
vector_vector_time = end_time_vector_vector - start_time_vector_vector

# Vectorized Operations (NumPy)
start_time_vector_vector_np = time.time()
result_vector_vector_np = vector_addition_numpy(vector1, vector2)
end_time_vector_vector_np = time.time()
vector_vector_time_np = end_time_vector_vector_np - start_time_vector_vector_np

# Performance Analysis
print(f"Scalar-Vector Addition (Scalar): {scalar_vector_time:.4f} seconds")
print(f"Scalar-Vector Addition (NumPy): {scalar_vector_time_np:.4f} seconds")
print(f"Vector-Vector Addition (Scalar): {vector_vector_time:.4f} seconds")
print(f"Vector-Vector Addition (NumPy): {vector_vector_time_np:.4f} seconds")

speedup_vector_vector = vector_vector_time / vector_vector_time_np
speedup_scalar_vector = scalar_vector_time / scalar_vector_time_np

print(f"Vector-Vector Speedup (NumPy): {speedup_vector_vector:.2f}x")
print(f"Scalar-Vector Speedup (NumPy): {speedup_scalar_vector:.2f}x")