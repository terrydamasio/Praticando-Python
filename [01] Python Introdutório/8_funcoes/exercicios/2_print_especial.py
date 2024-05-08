def writeMsg(msg):
    leng = len(msg) + 4
    print('~'*leng)
    print(f"  {msg}")
    print('~'*leng)

def main():
    writeMsg("Olá, mundo!")
    
if __name__ == '__main__':
    main()