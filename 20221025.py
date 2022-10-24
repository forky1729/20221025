import matplotlib.pyplot as plt
import numpy as np

#рисует белое всё
fig, ax = plt.subplots(figsize=(8,5),dpi = 200)

#Чтение данных из файлов data.txt и settings.txt
settings = np.loadtxt("settings.txt", dtype=float)
data_array = np.loadtxt("data.txt", dtype=int)

#Перевод показаний АЦП в Вольты, номеров отсчётов в секунды
volts = data_array * 3.3 / 256
time = np.arange(len(volts))
time = time * settings[0]
total_time = settings[0] * len(volts)

#Настройки цвета и формы линии, размера и цвета маркеров, частоты отображений маркеров и легенды
plt.ylabel('Напряжение, В',fontsize=12)
plt.xlabel('Время, с',fontsize=12)

#Текст с временем зарядки и разрядки
plt.text(650,190,"Время заряда = 4 с",fontsize=10)
plt.text(650,170,"Время разряда = 4 с",fontsize=10)

#Наличие сетки (главной и дополнительной), настройка ее цвета и стиля
plt.grid(which='major',color='#A0A0A0')
plt.minorticks_on()
plt.grid(which='minor',color='#E0E0E0', linestyle = '--')

#Название графика, с настройками его месторасположения и переносом текста на следующую строку, если текст слишком длинный
plt.title('Процесс заряда и разряда конденсатора в RC-цепи',fontsize=12, loc='center', fontweight='bold', style='italic', family='monospace')

plt.plot(time, volts, linestyle = '-', linewidth=1, color='#CD2EB8', label = "U(t)")
plt.plot(time[::20], volts[::20], marker='.', ms = 5, color='#CD2EB8')

plt.legend(loc = "best") 
plt.show()

#Сохранение графика в файл в формате .svg
fig.savefig("U_t.svg")
