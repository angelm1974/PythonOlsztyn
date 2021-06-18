def nazwane_arg(w, **kwargs):
    #print(kwargs.get('kosc', 'brak argumentu'))
    print(kwargs[0])

nazwane_arg(1, kosc=23, slon=22)