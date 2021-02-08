# import matplotlib
# #matplotlib.use('TkAgg')
# import matplotlib.pyplot as plt
# # fig = plt.figure(figsize=(6, 4))
# # ax = fig.add_subplot()
# x = [1,2,3]
# y = x
# # ax.plot(x,y)
# # plt.show

# plt.plot(x,y)
# plt.show()
import matplotlib.pyplot as plt
import numpy as np

# グラフとして描画するデータ
x = np.array([1,2,3,4])
y = np.array([2,3,4,5])

# グラフを描画
x = plt.plot(x, y)
print("---=-----------")
print(x)
print("---=-----------")
plt.show()