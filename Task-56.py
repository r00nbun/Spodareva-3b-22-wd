def name(file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as f:
            lst = f.read().lower().translate(str.maketrans('', '', '.,!"\'#$%&()*+-/:;<=>?@\[]^_`{|~}—')).split()
        res = {x:lst.count(x) for x in lst}
        print(max(res, key=res.get))
    except FileNotFoundError:
       return print('Ошибка')
ss = name('11.txt')
