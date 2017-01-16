def runBic(path):

    import os
    from subprocess import call
    from PIL import Image
    from re import sub
    from sklearn.externals import joblib
    import numpy as np
    from re import sub

    os.chdir('./..')
    os.chdir('./..')
    os.chdir('./media/documents/')
    cwd = os.getcwd()
    files = [f for f in os.listdir(".") if os.path.isfile(f)]
    for f in files:
        file_path = "./" + "1.ppm"
        im = Image.open(str(f))
        im.save(file_path)

    command = "./bic_generator/generatebic " + "./1.ppm" + " ./1.txt"
    call(str(command), shell=True)

    # Open the text file containing feature vectors extracted by BIC
    features = open("./1.txt", "r")
    lines = features.readlines()
    # Empty array to receive data from .txt
    data = np.empty((len(lines), 128), dtype=np.float)
    for l in xrange(0, len(lines)):
        # Feature vector data processing
        f_vector = sub("\n", "", lines[l])
        f_vector = f_vector.split(" ")
        f_vector.remove("")
        f_vector = np.asarray(f_vector)
        f_vector = f_vector.astype(np.float)

    knn = joblib.load("./knn_model/knn_model.pkl")
    f_vector = [f_vector]
    predict = knn.predict(f_vector)
    return predict
