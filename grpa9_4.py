def ancestry(P, present, past):
    if present == past:
        return [present]
    return [present] + ancestry(P, P[present], past)