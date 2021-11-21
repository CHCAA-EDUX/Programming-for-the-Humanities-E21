def difference(lst1, lst2):
    return list(set(lst1).difference(set(lst2)))

l1 = ['hans', 'grethe']
l2 = ['grethe', 'gert']

d = difference(l1, l2)
print(d)