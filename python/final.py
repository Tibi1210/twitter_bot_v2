
file = open("test.txt", "r", encoding='utf8')


tartalom = file.readlines()

with open('final.txt', 'w', encoding='utf8') as f:
    for sor in tartalom:
        sor = sor.strip()
        if sor != '' and sor.count('https') < 1 and "Sipos Bálint" not in sor and "Róbert Zahorszki" not in sor and "Tibor Vajda" not in sor and "(" not in sor and ")" not in sor and "@" not in sor and len(sor) > 20:
            f.write("'"+sor+"'"+',\n')


file.close()
