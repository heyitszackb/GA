import matplotlib.pyplot as plt

def graph(x, y):
    plt.scatter(x,y)
    plt.xlabel('Generation Number')
    plt.ylabel('Fitness')
    plt.title('Fitness as a function of generation number')
    plt.show()