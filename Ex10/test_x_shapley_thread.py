from tkinter.ttk import LabeledScale
from x_shapley import x_shapley
import matplotlib.pyplot as plt

def build_graph(lst_thread: list(), lst_regular: list()):
    x = [10000,20000,30000]
    plt.ylim(1,20)
    plt.xlim(9000,32000)
    plt.plot(x, lst_regular, label="Regular list", color='green', linestyle='dashed', linewidth = 3,
            marker='o', markerfacecolor='blue', markersize=12)
    plt.plot(x, lst_thread, label="Thread list", color='yellow', linestyle='dashed', linewidth = 3,
            marker='o', markerfacecolor='black', markersize=12)    
    plt.xlabel('len(X)')
    plt.ylabel('second(s)')
    plt.title('Comparison of running times')
    
    plt.legend(loc='best')
    plt.show()




if __name__ == "__main__":
    import time 
    x_func = x_shapley()
    agents = ["a","b","c"]
    X = [{'': 0, 'a': 0, 'b': 0, 'c': 100, 'ab': 0, 'ac': 100, 'bc': 100, 'abc': 100}]
    for i in range(10000):
        X.append(X[0])
    # print(X)
    lst_thread = []
    lst_regular = []

    # q1 -> 10001
    print("explation of len(X) = 10001")
    print("get_explanation_with_threads end in:")
    start = time.perf_counter()
    x_func.get_explanation_with_threads(X, agents)
    end = time.perf_counter()
    lst_thread.append(round(end-start,2))
    print(f'{lst_thread[0]} second(s)')
    x_func.get_explanation(X, agents)
    start = time.perf_counter()
    print("get_explanation end in:")
    lst_regular.append(round(start-end,2))
    print(f'{lst_regular[0]} second(s)')

    # q2 -> 20002
    for i in range(10000):
        X.append(X[0])
    print("explation of len(X) = 20001")
    print("get_explanation_with_threads end in:")
    start = time.perf_counter()
    x_func.get_explanation_with_threads(X, agents)
    end = time.perf_counter()
    lst_thread.append(round(end-start,2))
    print(f'{lst_thread[1]} second(s)')
    x_func.get_explanation(X, agents)
    start = time.perf_counter()
    print("get_explanation end in:")
    lst_regular.append(round(start-end,2))
    print(f'{lst_regular[1]} second(s)')


    # q3 -> 30003
    for i in range(10000):
        X.append(X[0])
    print("explation of len(X) = 30001")
    print("get_explanation_with_threads end in:")
    start = time.perf_counter()
    x_func.get_explanation_with_threads(X, agents)
    end = time.perf_counter()
    lst_thread.append(round(end-start,2))
    print(f'{lst_thread[2]} second(s)')
    x_func.get_explanation(X, agents)
    start = time.perf_counter()
    print("get_explanation end in:")
    lst_regular.append(round(start-end,2))
    print(f'{lst_regular[2]} second(s)')
    build_graph(lst_thread=lst_thread,lst_regular=lst_regular)