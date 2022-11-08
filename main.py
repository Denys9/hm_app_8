def str():
   try:

       num = (input('nums - '))
       split_list = num.split(' ')
       inted_list =[eval(i) for i in split_list]
       negative = []
       positive = []
       print(f'Max: {max(inted_list)}\nMin: {min(inted_list)}')
       for i in inted_list:
            if i > 0:
                positive.append(i)
            if i < 0:
               negative.append(i)
       print(f'positive: {positive}\nnegative: {negative}')
   except Exception as ex:
        print(f'Error: {ex}')


str()