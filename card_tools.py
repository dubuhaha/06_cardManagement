# 记录所有的名片字典
card_list = []


def show_menu():

    """显示菜单"""
    print("*" * 50)
    print("欢迎使用 【名片管理系统】 V 1.0")
    print()
    print("1. 新增名片")
    print("2. 显示全部")
    print("3. 搜素名片")
    print()
    print("0. 退出系统")
    print("*" * 50)


def new_card():

    """新增名片"""
    print("-" * 50)
    print("新增名片")

    # 1. 提示用户输入名片的详细信息
    name_str = input("请输入姓名： ")
    phone_str = input("请输入电话： ")
    qq_str = input("请输入QQ: ")
    email_str = input("请输入邮箱： ")

    # 2. 使用用户输入的信息建立一个名片字典
    card_dict = {"name": name_str,
                 "phone": phone_str,
                 "qq": qq_str,
                 "email": email_str}

    # 3. 将名片字典点击到列表中
    card_list.append(card_dict)

    print(card_list)

    # 4. 提示用户添加成功
    print("添加 %s 的名片成功" % name_str)


def show_all():

    """显示全部名片"""
    print("-" * 50)
    print("显示全部名片")

    # 判断是否存在名片记录，如果没有提示用户并且返回
    if len(card_list) == 0:

        print("当前没有任何的名片记录，请使用新增功能添加名片")

        # return 可以返回一个函数的执行结果
        # 下方的代码不会被执行
        # 如果return 后面没有任何的内容，表示会返回到调用函数的位置
        # 并且不会返回任何的结果
        return

    # 打印表头
    for name in ["姓名", "电话", "QQ", "邮箱"]:
        print(name, end="\t\t")

    print()

    # 打印分隔线
    print("-" * 50)

    # 遍历名片列表依次输出字典信息
    for card_dict in card_list:

        print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"],
                                        card_dict["phone"],
                                        card_dict["qq"],
                                        card_dict["email"]))


def search_card():

    """搜素名片"""
    print("-" * 50)
    print("搜索名片")
