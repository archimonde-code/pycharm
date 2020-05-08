"""
计算小费：
输入金额和小费率，计算最终的合计金额
"""
try:
    subtotal, gratuity = eval(input("Enter the subtotal and a gratuity rate:"))
    tip = subtotal * (gratuity/100)
    aggregate = subtotal + tip
    print("The tip is %.2f and aggregate is %.2f" % (tip, aggregate))
except TypeError:
    print("Input type error Please try again")


'''
对一个数字的各位数字求和
'''
number = eval(input("Enter a number between 0 and 1000:"))
unit = number % 10
decade = (number // 10) % 10
hundreds = number // 100
print("The sum of the digits is %d" % (unit + decade + hundreds))


"""
复利值：
求存银行6个月后的账户总额
"""
principal = eval(input("Enter the monthly saving amount："))
month = eval(input("Enter the month:"))
account = (principal * month) * ((1 + 0.00417) ** month)
print("After the %d month, The account value is %.2f" % (month, account))
