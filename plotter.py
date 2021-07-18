import matplotlib.pyplot as plt


def plot_learning_curve():
    f = open("learning_curve.txt",'r')
    data =f.readlines()
    mins = []
    maxs = []
    avgs = []
    for line in data:
        listdata = line[:-1].split(' ')
        mins.append(round(float(listdata[2])))
        maxs.append(round(float(listdata[1])))
        avgs.append(round(float(listdata[0])))
    x=list(range(1,len(data)+1))
    plt.plot(x,avgs)
    plt.title("averages")
    plt.show()
    plt.plot(x,mins)
    plt.title("minimums")
    plt.show()
    plt.plot(x,maxs)
    plt.title("maximums")
    plt.show()
    

if __name__ == "__main__":
    plot_learning_curve()