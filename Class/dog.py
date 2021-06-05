# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   python_29
# FileName:     dog
# Author:      TianChangJun
# Datetime:    2021/6/5 15:55
# Description：
# -----------------------------------------------------------------------------------

class Dog:
    # 一次模拟小狗的简单尝试

    """
        我们将方法__init__() 定义成了包含三个形参：self 、name 和age 。在这个方法的定义中，形参self 必不可少，还必须位于其他形参的前面。为何必须在方法定义中包
        含形参self 呢？因为Python调用这个__init__() 方法来创建Dog 实例时，将自动传入实参self 。每个与类相关联的方法调用都自动传递实参self ，它是一个指向实例本身
        的引用，让实例能够访问类中的属性和方法。我们创建Dog 实例时，Python将调用Dog 类的方法__init__() 。我们将通过实参向Dog() 传递名字和年龄；self 会自动传递
        因此我们不需要传递它。每当我们根据Dog 类创建实例时，都只需给最后两个形参（name 和age ）提供值
    """
    color_1 = "灰色"
    def __init__(self, name, age):
        # 初始化公有属性(公有成员变量)
        self.name = name  # 公有属性
        self.age = age  # 公有属性
        self.color = "黄色"

    def sit(self):
        # 模拟小狗被命令时蹲下
        print(self.name.title() + " is now sitting" + "它的颜色是{}".format(self.color))

    def roll_over(self):
        # 模拟小狗被命令时打滚
        print(self.name.title() + " is now rolling over" + "它的颜色是{}".format(self.color_1))


if __name__ == '__main__':
    myDog = Dog("white", 3)
    print(myDog.name, myDog.age, myDog.color, myDog.color_1)
    myDog.sit()
    myDog.roll_over()
