text = ''
choice = ''
msg = ''

while choice != 0:
    choice = input("\n Do you want to encrypt or decrypt the message?\n 1. encrypt\n 2. decrypt \n 0. exit program. ")

    if choice == '1':
        msg = input('\nEnter message for encryption: ')
        for i in range(0, len(msg)):
            text = text + chr(ord(msg[i]) + 3)

        print(text + '\n\n')
        text = ''

    if choice == '2':
        msg = input('\nEnter message to decrypt: ')
        for i in range(0, len(msg)):
            text = text + chr(ord(msg[i]) - 3)

        print(text + '\n\n')
        text = ''