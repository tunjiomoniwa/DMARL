import numpy as np
import matplotlib.pyplot as plt

def plot_learning_curve(x, scores, epsilons, filename):
    fig = plt.figure()
    ax1 = fig.add_subplot(111, label="1")
    ax2 = fig.add_subplot(111, label="2", frame_on=False)

    ax1.plot(x, epsilons, color="C0")
    ax1.set_xlabel("Training Steps", color="C0")
    ax1.set_ylabel("Epsilon", color="C0")
    ax1.tick_params(axis='both', color="C0")
    
    n = len(scores)
    running_avg = np.empty(n)
    for i in range(n):
        running_avg[i] = np.mean(scores[max(0, i-100): i+1])
    
    ax2.scatter(x, running_avg, color="C1")
    ax2.axes.get_xaxis().set_visible(False)
    ax2.yaxis.tick_right()
    ax2.set_ylabel('Score', color="C1")
    ax2.yaxis.set_label_position('right')
    ax2.tick_params(axis='y', color="C1")

    plt.show()
    plt.savefig(filename)
