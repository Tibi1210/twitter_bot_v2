from bs4 import BeautifulSoup

with open("message_1.html", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "html.parser")


boxes = soup.find_all(
    "div", class_="pam _3-95 _2pi0 _2lej uiBoxWhite noborder")
namebox = []
messagebox = []

combo = []
all = []

for items in boxes:
    namebox.append(items.find_all("div", class_="_3-96 _2pio _2lek _2lel"))
    messagebox.append(items.find_all("div", class_="_3-96 _2let"))

for i in range(2, len(namebox)):
    combo.append(namebox[i][0].getText().strip())
    combo.append(messagebox[i][0].getText().strip())
    all.append(combo)
    combo = []

i = 0
for elem in all:
    if elem[1].__contains__('Róbert Zahorszki') or elem[1].__contains__('Sipos Bálint') or elem[1].__contains__('Tibor Vajda'):
        del all[i]
    i += 1


elozo = all[0][0]
zipped = []
str = ''
with open('test.txt', 'w', encoding='utf8') as f:
    for i in range(len(all)-1, 0, -1):
        if all[i][0] == elozo:
            str += all[i][1]+" "
        else:
            f.write(str.strip()+"\n")
            elozo=all[i][0]
            str = all[i][1]+" "
