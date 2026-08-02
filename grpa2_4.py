def list_mutating_operations(items:list, item1, item2):
 items.sort()
 print (items)

 items.append(item1)

 items.insert(3, item2)

 items.extend(items[:3])

 popped_item=items.pop(4)

 items.remove(item2)

 items[4]=None

 items[::2]=None*len(items[::2])

 del items[-3]

 def list_non_mutating_operations(items:list, item1, item2):
  sorted(items)

  items+[item1]

  items[:3]+[item2]+items[3:]

  items[:4]+items[5:]

  index=items.index(item2)
  items[:index]+items[index+1:]

  items[:3]+ [None]+ items[4:]

  modified = items[::] # make a copy or use items.copy()
  modified[::2] = [None]*len(modified[::2])
  print("modify_slice:",modified)

def do_set_operation(set1, set2, set3, item1, item2):
    # add item1 to set1
    set1.add(item1)
    print(sorted(set1))
    # remove item2 from set1. What if item2 is not in set1?
    set1.discard(item2)
    print(sorted(set1))

    # add elements from set2 to set1
    set1.update(set2)
    print(sorted(set1))

    # remove all elements from set1 that are in set3
    set1.difference_update(set3)
    print(sorted(set1))

    # print the common elements in both set2 and set3 as a sorted list.
    print(sorted(set2 & set3))

    # print all unique elements present in set1, set2 an set3 as a sorted list
    print(sorted(set1 | set2 | set3))

    # print all unique elements that are in set2 but not in set3 as a sorted list
    print(sorted(set2 - set3))

    # print all the non common elements from both set2 and set3
    print(sorted(set2.symmetric_difference(set3)))

    return set1,sorted(set1),sorted(set2),sorted(set3)