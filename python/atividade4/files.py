with open("/home/arthur/Curso-DevOps/python/atividade4/index.txt", 'r') as f:
    file = f.read()
    finder = counter = 0
    file_types = []
    while finder != -1:
        counter = file.find('<h2 class="heading">', counter) + 1
        file_types.append(file[counter+19:file.find('<',counter+20)])
        if file.find('<h2 class="heading">', counter) == -1:
            finder = -1
    
    finder = counter = 0
    for ft in range(0, len(file_types)-1):
        ext_list = []
        finder = 0
        start = file.find(file_types[ft])
        end = file.find(file_types[ft+1])
        file_limit = file[start:end]
        print("\"%s\":" %file_types[ft])
        while finder != -1:
            counter = file_limit.find('<a href="/extension/', counter) + 1
            counter = file_limit.find('.', counter)
            extention = file_limit[ counter : file_limit.find( '<',counter ) ]
            ext_list.append(extention)
            # print("    \"%s\"," %extention)
            if file_limit.find('<a href="/extension/', counter) == -1:
                finder = -1
        print(str(ext_list) + ",")
        # print("],\n")
    
    
