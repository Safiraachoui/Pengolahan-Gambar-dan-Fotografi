import numpy as np
from matplotlib import pyplot as plt

# membuat diagram grafik garis menggunakan python
# Data for plotting
penjualan = (40, 82, 13, 17, 28, 25, 27)
tahun = (2000, 2001, 2002, 2003, 2004, 2005, 2006)

# untuk menampilkan gambar grafik ke layar.
# memberikan ukuran pada output dengan urutan panjang x lebar

plt.figure()
plt.bar(tahun,penjualan)
plt.title("Laporan Penjualan Getah Karet")
plt.xlabel("Tahun")
plt.ylabel("Penjualan (dalam kg)")
plt.grid()
plt.show()