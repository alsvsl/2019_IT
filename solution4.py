import matplotlib.pyplot as plt
import numpy as np

def is_pareto_efficient(x):
    efficiency = np.ones(x.shape[0], dtype = bool) 
    for i, value in enumerate(x):
        efficiency[np.asarray(efficiency)] = np.any(x[efficiency] > value, axis=1)
        efficiency[i] = True
    return efficiency

def get_arguments():
    n = np.random.randint(4, 7)
    m = np.random.randint(3, 5)
    return n, m

if __name__ == '__main__':
    n, m = get_arguments()
    X = np.random.randint(1, 10, (n, m))
    
    efficiency = np.asarray(is_pareto_efficient(X))
    efficient_x = X[efficiency]
    non_efficient_x = X[np.invert(efficiency)]

    _, plots = plt.subplots(ncols=2, subplot_kw=dict(polar=True))

    axis = np.linspace(0,  2 * np.pi, num=len(X[0]) + 1)

    for x in X:
        plots[0].plot(axis, np.append(x, x[0]))

    for x in efficient_x:
        plots[1].plot(axis, np.append(x, x[0]), color='r')

    for x in non_efficient_x:
        plots[1].plot(axis, np.append(x, x[0]), color='g')

    plt.subplots_adjust(wspace=1, )
    plt.show()



