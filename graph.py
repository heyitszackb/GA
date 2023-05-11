import matplotlib.pyplot as plt

def graph(x, y, name):
    plt.scatter(x,y)
    plt.xlabel('Generation Number')
    plt.ylabel(name)
    plt.title('Fitness as a function of generation number')
    plt.show()