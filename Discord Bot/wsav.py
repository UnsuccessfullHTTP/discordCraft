import pickle


def Save(r, a):
    try:
        h = open(r, "wb")
        pickle.dump(a, h)
        print("wsav: Saved world!")
        h.close()
    except Exception as e:
        print("wsav: Save Error -> ", e)
    

def Load(r):
    try:
        h = open(r, "rb")
        e = pickle.load(h)
        print("wsav: Loaded world!")
        h.close()
        return e
    except Exception as e:
        print("wsav: Load Error -> ", e)

