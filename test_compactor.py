import compactor

if __name__ == '__main__':
    comp = compactor.Compactor('py_intro')
    comp.compress(path_content=['..\\py_intro', 'compactor.py'], pwd='1234')
    print(comp)
