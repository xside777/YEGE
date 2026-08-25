for x in '123456789ABCDEFGHI':
    s=int(f'76{x}79645',19)+int(f'35{x}42',19)+int(f'332{x}6',19)
    if s%18==0:
        print(x,s//18)
