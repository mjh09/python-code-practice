def addBorder(picture):
    cnt = len(picture)

    if cnt > 0:
        new_pic = []
        ast_cnt = len(picture[0]) + 2
        ast_str = "*" * ast_cnt
    else:
        return picture

    for i in range(cnt + 2):
        if i == 0:
            new_pic.insert(i, ast_str)
        elif i == cnt + 1:
            new_pic.insert(i, ast_str)
        else:
            concat_string = '*' + picture[i-1] + "*"
            new_pic.insert(i, concat_string)
    return new_pic
