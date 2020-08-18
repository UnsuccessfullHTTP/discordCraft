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
        #for x in e:
        #    for y in x:
        #        y.draw(x.x, x.y)
        for x in e:
            for y in x:
                y.draw(y.x, y.y)
            break
        return e
        '''
        global player
        player = block(block.player, 4*16, 480-((8*16)+1))
        '''
    except Exception as e:
        print("wsav: Load Error -> ", e)

