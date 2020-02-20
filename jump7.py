for i in range(1,101):
    count = 0
    if i%7 == 0:
        count = 1
    else:
        j=str(i)
        for k in j:
            if k == '7':
                count = 1
                break
    if count == 0:
        print(i)

