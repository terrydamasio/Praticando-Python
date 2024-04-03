def writeMsg(msg):
    leng = len(msg) + 4
    print('~'*leng)
    print(f"  {msg}")
    print('~'*leng)

writeMsg("Olá, mundo!")