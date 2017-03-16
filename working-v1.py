# 靠右的直角三角形
# 输入图形高度
Height = int(input('Enter height of triangle: '))
Counter = 0
while (Height > 0):
    Height -= 1
    Counter += 1
    Space = ' ' * Height
    Logo = '#' * Counter
    print (Space, Logo)
    
