from matplotlib import pyplot as plt

# load csv file
with open("measure_time.csv", "r", encoding="utf-8") as f:
    header = f.readline()
    data = f.readlines()

# extract data
x = [int(line.split(",")[1]) for line in data]
y = [line.split(",")[0] for line in data]

# plot data
plt.figure(figsize=(20, 8))
plt.barh(y, x)
plt.xlabel("Time (ns)")
plt.ylabel("Function")
plt.title("Execution Time")
plt.show()
plt.savefig("measure_time.png")
