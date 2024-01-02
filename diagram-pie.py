import numpy as np
from matplotlib import pyplot as plt

penjualan = (40, 82, 13, 17, 28, 25, 27)
tahun = (2000, 2001, 2002, 2003, 2004, 2005, 2006)

explode = (0, 0, 0, 0, 0, 0, 0)

plt.figure(figsize=(10,5))
plt.pie(penjualan, explode=explode, labels=tahun)
plt.title("Laporan Penjualan Getah Karet")
plt.xlabel("Tahun")
plt.ylabel("Penjualan (dalam kg)")
plt.show()