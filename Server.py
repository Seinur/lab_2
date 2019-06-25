import socket
sock = socket.socket()
sock.bind(('', 9090))
while True:
    sock.listen(1)
    conn, addr = sock.accept()
    data = conn.recv(1024)
    if not data:
        break
    text = data.decode('utf-8')
    k=0
    newlist = list(text)
    text1 = ""
    if ((ord(newlist[k]) >= ord('a') and ord(newlist[k]) <= ord('z')) or (
            ord(newlist[k]) >= ord('а') and ord(newlist[k]) <= ord('я'))):
        newlist[0] = chr(ord(newlist[0]) - 32)
    while (k < len(newlist)):
        if (newlist[k] == ' '):
            while (newlist[k] == ' '):
                k = k + 1
            if ((ord(newlist[k]) >= ord('a') and ord(newlist[k]) <= ord('z')) or (
                    ord(newlist[k]) >= ord('а') and ord(newlist[k]) <= ord('я'))):
                newlist[k] = chr(ord(newlist[k]) - 32)
        k = k + 1
    for i in newlist:
        text1 += i

    conn.sendall(text1.encode('utf-8'))
    # Заменяем пробелы на звёздочки
    text2 = ""
    newlist = list(str(text1).replace(' ', '*'))
    for i in newlist:
        text2 += i
    text2=text2+"          "
    conn.sendall(text2.encode('utf-8'))


    # Удаляем гласные буквы
    text3 = ""
    k = 0
    for i in newlist:
        if (
                i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'y' or i == 'u' or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'Y' or i == 'U' or i == 'а' or i == 'о' or i == 'у' or i == 'э' or i == 'ы' or i == 'я' or i == 'е' or i == 'ю' or i == 'и' or i == 'ё' or i == 'А' or i == 'О' or i == 'У' or i == 'Э' or i == 'Ы' or i == 'Я' or i == 'Е' or i == 'Ю' or i == 'И' or i == 'Ё'):
            newlist[k] = ''
        text3 += newlist[k]
        k = k + 1
    conn.send(text3.encode('utf-8'))


conn.close()