a = {}  # 空字典
b = {'spam': 2, 'eggs': 3}  # 两项目字典
c = {'food': {'ham': 1, 'eggs': 2}}  # 嵌套
d = dict.fromkeys(['a', 'b'])  # 其他构造技术
e = dict(zip(['a', 'b', 'c'], [1, 2, 3]))  # 关键字对应的对、键列表
f = dict(name='Bob', age=14)
print(b['eggs'])  # 以键进行索引运算,\
print(c['food']['ham'])
print('a' in d)  # 成员关系：键存在测试
print(b.keys())  # 方法：键
print(b.values())  # 值
print(b.items())  # 键 + 值
print(b.copy())  # 副本
print(b.get('egg', 'error'))  # 默认
print(b.update(b))  # 合并
print(b.pop('eggs'))  # 删除等
print(len(d))  # 长度(储存的元素的数目)
b['eggs'] = 'items'  # 新增/修改键，删除键
print('新增/修改键，删除键:', b)
del b['eggs']  # 根据键删除条目
print('根据键删除条目后:', b)
print('字典视图：\n', list(b.keys()))  # 字典视图
print(b.keys() & c.keys())
