import datetime as dt

hari_ini = dt.date.today()
print(hari_ini)
print(f"hari ini adalah hari = {hari_ini:%A}")

indonesia_merdeka = dt.date(1945,8,17)
print(indonesia_merdeka)
print(f"Indonesia merdeka pada hari = {indonesia_merdeka:%A}")