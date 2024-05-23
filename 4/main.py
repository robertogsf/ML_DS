import numpy as np

def cosine_similarity(vector1, vector2):
    # Calcula el producto punto de los dos vectores
    dot_product = np.dot(vector1, vector2)
    
    # Calcula la magnitud (longitud) de cada vector
    magnitude_vector1 = np.sqrt(np.dot(vector1, vector1))
    magnitude_vector2 = np.sqrt(np.dot(vector2, vector2))
    
    # Calcula la similitud del coseno
    cosine_similarity = dot_product / (magnitude_vector1 * magnitude_vector2)
    
    return cosine_similarity

# Vectores de prueba
vector1 = np.array([1, 2, 3])
vector2 = np.array([4, 5, 6])

# Calcula la similitud del coseno
similarity = cosine_similarity(vector1, vector2)

print(f"La similitud del coseno entre {vector1} y {vector2} es {similarity}.")
