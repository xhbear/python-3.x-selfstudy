# 靠右的直角三角形
# 输入图形高度
daInput = int(input('Enter height of triangle: '))
x = daInput
space = ' '; 
logo = '@';
val_space = x - 1;
val_logo = 1; 

while (x > 0):
    space = space * val_space
    logo = logo * val_logo
    print ('{}{}'.format(space, logo))
    val_space -= 1
    val_logo += 1
    x -= 1

