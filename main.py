import numpy as np
import matplotlib.pyplot as plt

tegangan = np.array([5, 10, 15, 20, 25, 30, 35, 40])
waktu_patah = np.array([40, 30, 25, 40, 18, 20, 22, 15])

def interpolasi_lagrange(t, titik_x, titik_y):
    def polinomial_basis(k, t):
        hasil = 1
        for j in range(len(titik_x)):
            if j != k:
                hasil *= (t - titik_x[j]) / (titik_x[k] - titik_x[j])
        return hasil

    hasil_interpolasi = 0
    for k in range(len(titik_x)):
        hasil_interpolasi += titik_y[k] * polinomial_basis(k, t)
    return hasil_interpolasi

def interpolasi_newton(t, titik_x, titik_y):
    n = len(titik_x)
    koef = np.zeros([n, n])
    koef[:, 0] = titik_y

    for j in range(1, n):
        for i in range(n - j):
            koef[i, j] = (koef[i + 1, j - 1] - koef[i, j - 1]) / (titik_x[i + j] - titik_x[i])

    def basis_newton(t, titik_x, k):
        hasil = 1
        for i in range(k):
            hasil *= (t - titik_x[i])
        return hasil

    hasil_interpolasi = 0
    for k in range(n):
        hasil_interpolasi += koef[0, k] * basis_newton(t, titik_x, k)
    return hasil_interpolasi

t_plot = np.linspace(5, 40, 400)
y_lagrange = np.array([interpolasi_lagrange(t, tegangan, waktu_patah) for t in t_plot])
y_newton = np.array([interpolasi_newton(t, tegangan, waktu_patah) for t in t_plot])
plt.figure(figsize=(12, 6))
plt.plot(t_plot, y_lagrange, label='Interpolasi Lagrange', color='blue')
plt.plot(t_plot, y_newton, label='Interpolasi Newton', color='green')
plt.scatter(tegangan, waktu_patah, color='red', zorder=5)
plt.title('Interpolasi menggunakan Metode Lagrange dan Newton')
plt.xlabel('Tegangan, t (kg/mm2)')
plt.ylabel('Waktu Patah, y (jam)')
plt.legend()
plt.grid(True)
plt.show()
