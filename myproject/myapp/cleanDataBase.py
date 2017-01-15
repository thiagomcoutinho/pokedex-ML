def cleanDataBase(path):
    import os
    os.chdir('./..')
    os.chdir('./..')
    os.chdir('./media/documents/')
    files = [f for f in os.listdir(".") if os.path.isfile(f)]
    for f in files:
        os.remove(f)