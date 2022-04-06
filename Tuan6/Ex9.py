import numpy as np
import math
D1=[0 ,4, 0, 0, 0, 2, 1, 3]
D2=[3 ,1, 4, 3, 1, 2, 0, 1]
D3=[3, 0, 0, 0, 3, 0, 3, 0]
D4=[0, 1, 0, 3, 0, 0, 2, 0]
D5=[2, 2, 2, 3, 1, 4, 0, 2]
def Cosine_Similarity(u,v):
    return np.dot(u,v)/(np.linalg.norm(u)*np.linalg.norm(v))
'''
def cosine_similarity(vector1, vector2):
    dot_product = 0.0
    normA = 0.0
    normB = 0.0
    for a, b in zip(vector1, vector2):
        dot_product += a * b
        normA += a ** 2
        normB += b ** 2
    if normA == 0.0 or normB == 0.0:
        return None
    else:
        return dot_product / ((normA ** 0.5) * (normB ** 0.5))
    

'''
print("D1-D2:",Cosine_Similarity(D1,D2))
print("D1-D3:",Cosine_Similarity(D1,D3))





