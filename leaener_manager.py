# -*- coding:utf-8 -*-
# @author zhouwei
# @date 2023/2/8 14:26
# @file leaener_manager.py

# 所有功能函数都是操作学员信息，所有存储所有学员信息应该是一个全局变量，数据类型为列表
infos = []


# 定义功能界面函数
def info_print():
    print('请选择功能--------------')
    print("1、添加学员")
    print("2、删除学员")
    print("3、修改学员")
    print("4、查询学员")
    print("5、显示所有学员")
    print("6、退出系统")
    print("-" * 20)


def add_info():
    """
    添加学员
    需求分析：
        1、接收用户输入学员信息，并保存
        2、判断是否添加学员信息
            2.1、如果学员姓名已经存在，则报错提示
            2.2、如果学员姓名不存在，则准备字典，将用户输入的数据追加到字典，再列表追加字典数据
        3、对应的if条件成立的位置调用该函数
    :return:
    """
    # 接收用户输入学员信息
    new_id = input('请输入学号：')
    new_name = input('请输入姓名：')
    new_tel = input('请输入手机号：')

    # 声明info是全局变量
    global infos
    # 检测用户输入的姓名是否存在，存在则报错
    for info in infos:
        if new_name == info['name']:
            print('该用户已经存在！！！')
            return

    # 如果用户输入的姓名不存在，则添加该学员信息
    info_dict = {}
    # 将用户输入的数据添加到字典
    info_dict['id'] = new_id
    info_dict['name'] = new_name
    info_dict['tel'] = new_tel
    # 将这个学员的字典数据追加到列表
    infos.append(info_dict)
    print(infos)


def del_info():
    """
    删除学员
    需求分析：
        1、用户输入目标学员姓名
        2、检查这个学员是否存在
            2.1、如果存在，则列表删除这个数据
            2.2、如果不存在，则提示”该用户不存在“
        3、对应的if条件成立的位置调用该函数
    :return:
    """
    # 1、用户输入要删除的学员姓名
    del_name = input('请输入要删除的学员姓名：')
    global infos
    # 2、判断学员是否存在，如果存在则删除，如果不存在则报错
    for info in infos:
        if del_name == info['name']:
            infos.remove(info)
            print(f'用户{del_name}已经被删除')
            break
    else:
        print('该用户不存在')
    print(infos)


# 系统功能需要循环使用，直到用户输入6，才退出系统
# 如果用户输入1-6以外的数据，则需要提示用户 输入错误
while True:
    # 1、显示功能界面
    info_print()

    # 2、用户输入功能序号
    user_num = int(input("请输入功能序号："))

    # 3、按照用户输入的功能序号，执行不同的功能
    if user_num == 1:
        add_info()
    elif user_num == 2:
        del_info()
    elif user_num == 3:
        print('修改')
    elif user_num == 4:
        print('查询')
    elif user_num == 5:
        print('显示所有')
    elif user_num == 6:
        print('退出系统')
    else:
        print('输入功能序号有误，请重新输入')
