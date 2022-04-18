from calendar import c
import csv

from numpy import cov

file = open("daten.csv")

csvreader = csv.reader(file)
header = next(csvreader)
print(header)

rows = []

for row in csvreader:
    rows.append(row)

daten = []


for i in rows:
    if i[0] == "2022-04-17":
        daten.append(i)

betten_frei = []
betten_belegt = []
covid = []
covid_beatmet = []

for i in daten:
    betten_frei.append(i[7])
    betten_belegt.append(i[8])
    covid.append(i[5])
    covid_beatmet.append(i[6])

betten_frei = [int(i) for i in betten_frei]
betten_belegt = [int(i) for i in betten_belegt]
covid = [int(i) for i in covid]
covid_beatmet = [int(i) for i in covid_beatmet]

betten_gesamt = []
counter = 0
for i in betten_frei:
    betten_gesamt.append(betten_frei[counter] + betten_belegt[counter])
    counter = counter +1



covidprozent = []
counter = 0
for i in betten_gesamt:
    covidprozent.append(covid[counter] / i)
    counter = counter +1

print(covidprozent)
counter = 0
for i in covidprozent:
    
    covidprozent[counter] = covidprozent[counter] *100
    covidprozent[counter] = round(covidprozent[counter], 2)
    counter = counter + 1
print(covidprozent)
alarm = 0
counter = 0
for i in covidprozent:
    counter = counter +1
    if i > 50.0:
        alarm = alarm+1
covidprozent.sort()
print(covidprozent[-1])

if alarm == 0:
    print("In keinem von " + str(counter) + " Landkreisen sind mehr als 50% der Intensivbetten durch Covid-Positive Patienten belegt.")
else:
    print("In " + str(alarm) + " von " + str(counter) + " Landkreisen sind mehr als 50% der Intensivbetten durch Covid-Positive Patienten belegt.")



