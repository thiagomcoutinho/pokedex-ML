def predictClass(path):

    import os
    import numpy as np
    from re import sub
    from .knn_model_train import knn_model_train

    knn = knn_model_train(path)  # Trainning knn-model with features.txt

    os.chdir(path)
    os.chdir('./..')
    os.chdir('./..')
    os.chdir('./media/documents/')
    # Open the text file containing feature vectors extracted by BIC
    features = open("./1.txt", "r")
    lines = features.readlines()
    for l in xrange(0, len(lines)):  # Parsing feature vector into memory
        # Feature vector data processing
        f_vector = sub("\n", "", lines[l])
        f_vector = f_vector.split(" ")
        f_vector.remove("")
        f_vector = np.asarray(f_vector)
        f_vector = f_vector.astype(np.float)

    f_vector = [f_vector]  # Preparing data structure to model
    predict = knn.predict(f_vector)  # Classification with knn
    return predict
