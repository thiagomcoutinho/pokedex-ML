def prepareDataBase(path):

    import os
    from subprocess import call
    from PIL import Image

    #################################### Accessing Uploaded file ##################################
    os.chdir(path)
    os.chdir('./..')
    os.chdir('./..')
    os.chdir('./media/documents/')  # Changing to uploaded file directory
    files = [f for f in os.listdir(".") if os.path.isfile(f)]
    for f in files:
        file_path = "./" + "1.ppm"  # Rename file to pattern name
        im = Image.open(str(f))
        im.save(file_path)  # Saving file in '.ppm' format, which BIC can work on.

    ################################## Feature Extration with BIC ##################################
    command = "./bic_generator/generatebic " + "./1.ppm" + " ./1.txt"
    call(str(command), shell=True)  # Running BIC feature extractor

    os.chdir(path)  # Returning to current directory
