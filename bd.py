import pyodbc
import matplotlib.pyplot as plt
from itertools import chain
db = pyodbc.connect('Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:/access_to_python/bd.accdb;')
dbc = db.cursor()
dbc.execute('SELECT bd.ClientID,Avg(bd.SaveSum), Avg(bd.Cost) FROM bd GROUP BY bd.ClientID;')
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.grid(True, color = 'black', lw = 0.2)
ax.set_ylabel('ID клиента', fontsize=15)
ax.set_xlabel('Итоговая сумма (с учётом вычета страховой)', fontsize=15)
rows = [row for row in dbc.fetchall()]
item=list(chain(*rows))
clientid=item[0::3]
save=item[1::3]
cost=item[2::3]
xs=range(len(clientid))
new=[]
for i in range(len(cost)):
    x=int(cost[i]-save[i])
    new.append(x)
ax.barh(xs,cost, height = 0.2, color = 'orange',label = 'Сумма сделки')
ax.barh(xs,new, height = 0.2, color = 'lime',label = 'Сумма сделки с вычетом страховой суммы')
plt.yticks(xs, clientid)
plt.legend(loc='upper right')