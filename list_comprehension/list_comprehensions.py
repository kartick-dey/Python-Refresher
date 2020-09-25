def list_comprehension_func():
    actresses_list = ['Disha', 'Deepika', 'Kirara', 'Kareena', 'Dia']
    starts_D = [actress for actress in actresses_list if actress.startswith('D')]
    starts_K = [actress for actress in actresses_list if actress.startswith('K')]
    print('Starts with "D" : ', starts_D)
    print('Starts with "K" : ', starts_K)

list_comprehension_func()