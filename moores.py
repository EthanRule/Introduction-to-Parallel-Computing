import matplotlib.pyplot as plt

components = [3000, 1000000, 40000000, 700000000, 6000000000, 90000000000]
# 1993 - 2005
flops = [235.79, 235.79, 235.79, 614.4, 1830.4, 1830.4, 3207, 12288, 12288, 40960, 40960, 91750]

# plt.plot(components)
# plt.yscale('log')
# plt.show()
avg = sum(flops)/12
plt.title(avg)
plt.plot(flops)
plt.yscale('log')
plt.show()

