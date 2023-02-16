password = input('Введите пороль :')
is_numeric = False
is_upper = False
is_lower = False
is_spec = False

for tap in password :
    if tap.isnumeric():
        is_numeric = True
    elif tap.islower():
        is_lower = True
    elif tap.isupper():
        is_upper = True
    elif tap in "#%&@$^*":
        is_spec = True

if len(password)>6 and is_numeric and is_upper and is_lower and is_spec:
    print('Пароль : Надежный ')
else:
    print('Пароль не очень надежный , попробуйте еще раз')

