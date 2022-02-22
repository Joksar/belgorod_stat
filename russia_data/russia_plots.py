import matplotlib.pyplot as plt
import numpy as np
from russia_data.russian_data import *

"""Изменение численности населения в Российской Федерации"""
fig, ax = plt.subplots(figsize=(18,8))
x = russia_total_pop.keys()
y = russia_total_pop.values()
ax.plot(x, y, color='red', linestyle='-', marker='o')
ax.set_ylabel('Численность')
ax.set_xlabel('Год')
ax.set_title('Изменение численности населения в Российской Федерации')
#ax.set_yticks(np.arange(1500000, 1600000, 5000))
current_values = plt.gca().get_yticks()
plt.gca().set_yticklabels(['{:.0f}'.format(x) for x in current_values]) ###Возьми отсюда для полного отображения чисел
plt.grid()
fig.savefig('./russia_pop_change.png')
plt.show()

"""Соотношение городского и сельского населения в Российской Федерации"""
fig, ax = plt.subplots(figsize=(10,8))
labels = 'Городское население', 'Сельское население'
data = [russia_city_res[2020], 100 - russia_city_res[2020]]
ax.pie(data, labels=labels, autopct='%.2f%%', shadow=False, startangle=90)
ax.axis('equal')
ax.set_title('Соотношение городского и сельского населения Российской Федерации')
fig.savefig('./russia_city_rural_comp.png')
plt.show()


"""Динамика роста населения в Российской Федерации"""
fig, ax = plt.subplots()
x = russia_pop_chng.keys()
y = russia_pop_chng.values()
ax.bar(x, y,)
ax.set_xlabel('Год')
ax.set_ylabel('Кол.во человек')
ax.set_title('Динамика роста населения в Российской Федерации')
plt.grid()
fig.savefig('./russia_pop_growth.png')
plt.show()

"""Миграционные изменения в Курской области"""
fig, ax = plt.subplots()
x = kursk_migr_chng.keys()
y = kursk_migr_chng.values()
ax.bar(x, y, color='red')
ax.set_xlabel('Год')
ax.set_ylabel('Кол.во человек')
ax.set_title('Миграционные изменения в Курской области')
ax.set_xticks(list(x))
plt.grid()
fig.savefig('./kursk_migration.png')
plt.show()


"""Соотношение населения по трудоспособности"""
fig = plt.figure(figsize=(14,8))
ax1 = fig.add_subplot(1,2,1)
ax2 = fig.add_subplot(1,2,2)
labels = 'Моложе трудоспособ.', 'Трудоспособные', 'Старше трудосп.'
y = russia_labour_pop_2020.values()
x = russia_labour_pop_2020.keys()
ax1.pie(y, labels=labels, autopct='%.2f%%', shadow=False, startangle=90)
ax1.axis('equal')
ax1.set_title('Соотношение по основным возрастным группам \nРоссийской Федерации в %')
ax2.bar(labels, y)
ax2.set_title('Численность населения Российской Федерации\nпо основным возрастным группам \n тыс.человек')
# current_values = ax2.get_yticks()
# ax2.set_yticklabels(['{:.0f}'.format(x) for x in current_values])
ax2.set_yticks(np.arange(0,100000,5000))
plt.grid()
fig.savefig('./russia_labor_comp.png')
plt.show()

"""Соотношение полов на 2020 год."""
fig = plt.figure(figsize=(16,8))
ax1 = fig.add_subplot(1,2,1)
ax2 = fig.add_subplot(1,2,2)
labels = 'Мужчины', 'Женщины'
y = russia_men_female_2020.values()
x = russia_men_female_2020.keys()
ax1.pie(y, labels=labels, autopct='%.2f%%', shadow=False, startangle=90)
ax1.axis('equal')
ax1.set_title('Соотношение полов в \nРоссийской Федерации')
ax2.bar(labels, y)
ax2.set_title('Число мужчин и женщин в Российской Федерации \nтыс.человек')
ax2.set_yticks(np.arange(0,100000,5000))
plt.grid()
fig.savefig('./russia_gender_compare.png')
plt.show()
#
"""Популяционная пирамида Российской Федерации"""
fig, axes = plt.subplots(ncols=2, sharey=True, figsize=(16, 6))
y = range(0, len(russia_men_by_age.keys()))
x_men = russia_men_by_age.values()
x_women = russia_women_by_age.values()
axes[0].barh(y, x_men, align='center', color='red')
axes[0].set(title='Мужчины')
axes[1].barh(y, x_women, align='center', color='blue')
axes[1].set(title='Женщины')
axes[1].grid()
axes[0].set(yticks=y, yticklabels=list(russia_men_by_age.keys()))
current_values = axes[0].get_xticks()
axes[0].set_xticklabels(['{:.0f}'.format(x) for x in current_values])
axes[1].set_xticklabels(['{:.0f}'.format(x) for x in current_values])
axes[0].invert_xaxis()
axes[0].set_xlabel('Численность')
axes[1].set_xlabel('Численность')
axes[0].set_ylabel('Возраст')
axes[0].grid()
fig.savefig('./russia_pop_pyramid.png')
plt.show()



