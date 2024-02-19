import math
import numpy as np
import pandas as pd

def dot(vec1,vec2):
    total=0
    for i in range(0,len(vec1)):
        total+=vec1[i]*vec2[i]
        
    return total

def cosine(vec1,vec2):
    return dot(vec1,vec2)/math.sqrt(dot(vec1,vec1)*dot(vec2,vec2))

def cosine_allpair(data):
    similarity = []
    for docA in data:
        for docB in data:
            result = cosine(list(docA), list(docB))
    return similarity