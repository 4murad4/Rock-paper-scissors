import random
import time

print('Oyun başlayır...')

time.sleep(3)

def oyna():
    istifadecininXali = 0
    komputerinXali = 0

    for i in range(3):
        siyahi = ['daş' , 'kağız' , 'qayçı', 'das', 'kagiz', 'qayci']
        istifadecininSecimi = input('Bunlardan birini seçin: daş, kağız, qayçı\n')
        komputerinSecimi = random.choice(siyahi)

        if istifadecininSecimi == 'daş' or istifadecininSecimi == 'das':
            if komputerinSecimi == 'kağız' or komputerinSecimi == 'kagiz':
                print('Kompüter qalib gəldi')
                komputerinXali += 1
            elif komputerinSecimi == 'qayçı'or komputerinSecimi == 'qayci':
                print('Siz qalib gəldiniz')
                istifadecininXali += 1
            elif komputerinSecimi == 'daş' or komputerinSecimi == 'das': 
                print('Bərabərlik')
        elif istifadecininSecimi == 'kağız' or istifadecininSecimi == 'kagiz':
            if komputerinSecimi == 'qayçı' or komputerinSecimi == 'qayci':
                print('Kompüter qalib gəldi')
                komputerinXali += 1
            elif komputerinSecimi == 'daş' or komputerinSecimi == 'das':
                print('Siz qalib gəldiniz')
                istifadecininXali += 1
            elif komputerinSecimi == 'kağız' or komputerinSecimi == 'kagiz':
                print('Bərabərlik')
        elif istifadecininSecimi == 'qayçı' or istifadecininSecimi == 'qayci':
            if komputerinSecimi == 'daş' or komputerinSecimi == 'das':
                print('Kompüter qalib gəldi')
                komputerinXali += 1
            elif komputerinSecimi == 'kağız' or komputerinSecimi == 'kagiz':
                print('Siz qalib gəldiniz')
                istifadecininXali += 1
            elif komputerinSecimi == 'qayçı' or komputerinSecimi == 'qayci':
                print('Bərabərlik')

    if komputerinXali > istifadecininXali:
        print(f'Kompüter turu qazandı\n Ümumi hesab: {komputerinXali}:{istifadecininXali}') 
    elif istifadecininXali > komputerinXali:  
        print(f'Siz turu qazandınız\n Ümumi hesab: {istifadecininXali}:{komputerinXali}') 
    else:
        print(f'Heç kəs turu qazanmadı,bərabərlik\n Ümumi hesab: {komputerinXali}:{istifadecininXali}')

    yeniOyun = input('Yenidən oynamaq istəyirsiniz? hə/yox\n')
    if yeniOyun == 'hə' or yeniOyun == 'he':
        oyna() 

oyna()