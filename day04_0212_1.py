import random
drinks = ['위스키', '와인', '소주', '고량주']
foods = ['초콜릿', '치즈', '삽겹살', '양꼬치']

while True:
    menu = input(f'다음 술중에 고르세요.\n1) {drinks[0]}   2) {drinks[1]}   3) {drinks[2]}   4) {drinks[3]}   5) 아무거나  6)종료 : ')
    if menu == '1':
        print(f'{drinks[0]}에 어울리는 안주는 {foods[0]} 입니다')
    elif menu == '2':
        print(f'{drinks[1]}에 어울리는 안주는 {foods[1]} 입니다')
    elif menu == '3':
        print(f'{drinks[2]}에 어울리는 안주는  {foods[2]}입니다')
    elif menu == '4':
        print(f'{drinks[3]}에 어울리는 안주는 {foods[3]} 입니다')
    elif menu == '5':
        random_index = random.randint(0, len(drinks)-1)
        print(f'{drinks[random_index]}에 어울리는 안주는 {foods[random_index]} 입니다')
    elif menu == '6':
        print(f'다음에 또 오세요')
        break