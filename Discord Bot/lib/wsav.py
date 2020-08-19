import pickle
import renderer


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
        h.close()
        #for x in e:
        #    for y in x:
        #        y.draw(x.x, x.y)
        for x in e:
            for y in x:
                y.draw(y.x, y.y, y.id)
                #print(y.x, " ", y.y, " ", y.id)
            
        
        renderer.spawnPlayer()
        print(renderer.player.x)
        print("wsav: Loaded world!")
        
    except Exception as e:
        print("wsav: Load Error -> ", e)

