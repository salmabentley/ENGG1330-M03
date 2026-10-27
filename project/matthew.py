from ast import Name
def dead_body():

    print('Investigating wallet...')
    print('Investigate "Red Cross Card" (1)  Investigate credit cards (2)  Investigate ID (3) Photo (4) Quit (5)')
    while True:
        choosing_number = input()
        if choosing_number == '1':
            print('Red Cross Blood Transfusion Service')
            print('Name: Mr.Thomas Vance')
            print('Blood Type: AB+')
            print('Member ID: 0902')
            print('Issue Date: October 26, 2020')
        if choosing_number == '2':
            print('Wealthy Bank')
            print('Credit Card Number: 202610262126')
            print('CVV: 214')
            print('Expiration Date: February 11, 2028')
            print('Name: Thomas Vance')
        if choosing_number == '3':
            print('Permanent Identity Card')
            print('Name: Thomas Vance')
            print('Date of Birth: 01-08-1966')
            print('Gender: Male')
            print('ID Number: K1234567(8)')
        if choosing_number == '4':
            print('Photo of Thomas Vance')
            print('A photo of Thomas Vance and Peter Lang in a suit, smiling at the camera, putting his arm around Peter Lang.')
            print('The photo is dated 1984, and the two men appear to be at a formal event, possibly a graduation ceremony.')
        if choosing_number == '5':
            print('Returning to the previous page...')