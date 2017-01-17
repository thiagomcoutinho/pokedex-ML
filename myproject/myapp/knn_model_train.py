def knn_model_train(path):
    import os
    import numpy as np
    from re import sub
    from sklearn.ensemble import BaggingClassifier
    from sklearn.neighbors import KNeighborsClassifier

    ############################## DATA IMPORT AND PROCESSING ##############################
    # Open the text file containing feature vectors extracted by BIC
    os.chdir(path)
    features = open("./features.txt", "r")
    lines = features.readlines()
    # Create vector of target with -1's
    target_vector = np.full((len(lines), 1), -1, dtype=np.float)
    # Empty array to receive data from .txt
    data = np.empty((len(lines), 128), dtype=np.float)
    for l in xrange(0, len(lines)):
        # Feature vector data processing
        f_vector = sub("\n", "", lines[l])
        f_vector = f_vector.split(" ")
        f_vector = np.asarray(f_vector)
        f_vector = f_vector.astype(np.float)
        # Parsing the class number to target vector
        target_vector[l] = f_vector[-1]
        # Filling data with feature vector without last element(class number)
        data[l] = np.delete(f_vector, len(f_vector)-1)

    #################################### KNN MODEL SELECTION #################################
    # Instance of classifier
    model = BaggingClassifier(KNeighborsClassifier(n_neighbors=7, algorithm='ball_tree', metric='manhattan'),
                              n_estimators=10, max_samples=0.7, max_features=0.5)
    #################################### KNN MODEL TRAINNING #################################
    # Fitting the model using all data
    model.fit(data, target_vector.ravel())
    return model
