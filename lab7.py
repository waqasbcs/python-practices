import matplotlib.pyplot as plt

labels = ['apple', 'banana', 'orange', 'peach', 'watermelon', 'stabeery']
sizes = [12, 15, 20, 19, 18, 25]

plt.pie(sizes, labels=labels, autopct='%1.1f%%')

plt.title("Fruits")

plt.show()



