import numpy as np

D1=[1.0, 0.5, 0.3, 0, 0, 0]
D2=[0.5, 1.0, 0, 0, 0, 0]
D3=[0, 1.0, 0.8, 0.7, 0, 0]
D4=[0, 0.9, 1.0, 0.5, 0, 0]
D5=[0, 0, 0 ,1.0, 0, 1.0]
D6=[0, 0, 0, 0, 0.7, 0]
D7=[0.5, 0, 0.5, 0, 0, 0.9]
D8=[0, 0.6, 0, 1.0, 0.3, 0.2]
q=[0,0,0.7,0,0.3]

'''
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

u =np.vstack((D1,D2,D3,D4,D5,D6,D7,D8))


def nearest_neighbor(vector1, vector2):
    cosine_similarity_list = []
    for i in range(len(vector2)):
        cosine_similarity_list.append(cosine_similarity(vector1, vector2[i]))
    return cosine_similarity_list.index(max(cosine_similarity_list))

print("The nearest neighbor is:",nearest_neighbor(q,u))






