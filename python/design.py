import string

file = open("xddd.txt", "r", encoding='utf8')


tartalom = file.readlines()
ujszo =''
with open('bruh.txt', 'w', encoding='utf8') as f:
    for sor in tartalom:
        sor = sor.lower().strip()
        ujszo =''
        for letter in sor:
            if letter == 'á':
                ujszo+='a'
            elif letter == 'é':
                ujszo+='e'
            elif letter == 'ú':
                ujszo+='u'
            elif letter == 'ü':
                ujszo+='u'
            elif letter == 'ű':
                ujszo+='u'
            elif letter == 'í':
                ujszo+='i'
            elif letter == 'ó':
                ujszo+='o'
            elif letter == 'ő':
                ujszo+='o'
            elif letter == 'ö':
                ujszo+='o'
            elif letter == ',':
                ujszo+=''
            elif letter in list(string.ascii_lowercase) or letter==' ' or letter == '?' or letter == '!' or letter == '0' or letter == '1'or letter == '2'or letter == '3'or letter == '4'or letter == '5'or letter == '6'or letter == '7'or letter == '8'or letter == '9':
                ujszo+=letter
        if len(ujszo)>15:
            f.write("'"+ujszo+"',"+'\n')






