while True:
    mode = input('請輸入遊戲模式: ')
    if 	mode == 'q': #quit
        break
    elif mode == '1':
        print('啟動遊戲模式一')
    elif mode == '2':
        print('啟動遊戲模式二')
    else:
    	print('只能輸入 1/2/q')