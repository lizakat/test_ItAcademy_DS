def cosine_similarity(vec1, vec2):

    if len(vec1) == 0 or len(vec2) == 0:
        print("One of the vectors is empty")
        return
    if len(vec1) != len(vec2):
        print("The vectors have different lengths")
        return

    scalar_product = sum(a * b for a, b in zip(vec1, vec2))

    magnitude_vec1 = (sum(a ** 2 for a in vec1))**0.5
    magnitude_vec2 = (sum(b ** 2 for b in vec2))**0.5

    if magnitude_vec1 == 0 or magnitude_vec2 == 0:
        print("One of the vectors has zero magnitude")
        return

    cosine_sim = scalar_product / (magnitude_vec1 * magnitude_vec2)
    print(cosine_sim)


vec1 = [-7, 4, 10]
vec2 = [2, 5, 6]
cosine_similarity(vec1, vec2)
