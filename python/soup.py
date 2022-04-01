from bs4 import BeautifulSoup

with open("message_13.html", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "html.parser")


messages = soup.find_all("div", class_="_3-96 _2let")

with open('prompts.txt', 'a', encoding='utf8') as f:
    for text in messages:
        input = text.getText().strip()
        if input != '' and input.count('https') < 1 and "Sipos Bálint" not in input and "Róbert Zahorszki" not in input and "Tibor Vajda" not in input and "(" not in input and ")" not in input and "@" and "/" not in input and len(input) > 15:
            f.write(input+'\n')
