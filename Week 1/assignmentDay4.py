#1 Create a set with the following elements:10,20,30,40,50
new_set ={10,20,30,40,50}
print(new_set)

#2 Add the element 60 to the set
new_set.add(60)
print(new_set)

#3 Remove the element 20 from the set
new_set.remove(20)
print(new_set)

#4 Check of the element 30 is in the set
n={30}
check = n.issubset(new_set)
print(check) #True

#5 Find the length of the set.
print(len(new_set))

#6 Create two sets and perform following operations
set1={1,2,3,4}
set2={3,4,5,6}
#union
set_union=set1.union(set2)
print(set_union)

#intersection
set_intersection = set1.intersection(set2)
print(set_intersection)

#difference
set_diff1= set1.difference(set2)
print(set_diff1)
set_diff2= set2.difference(set1)
print(set_diff2)

#symmetric_difference
diff=set1.symmetric_difference(set2)
print(diff)

#subset
check_subset1 = set1.issubset(set2)
print(check_subset1) #False
check_subset2 = set2.issubset(set1)
print(check_subset2) #False

#superset
check_super1= set1.issuperset(set2)
print(check_super1) #False
check_super2= set2.issuperset(set1)
print(check_super2) #False

#disjoint
check_dis = set1.isdisjoint(set2)
print(check_dis) #False

#7 Given the set my_set={1,2,3} add the number 4 to the set
my_set={1,2,3}
my_set.add(4)
print(my_set)

#8 Given the set my_set={1,2,3,4} remove the number 2 from the set
my_set={1,2,3,4}
my_set.remove(2)
print(my_set)

#9 Given two set1={1,2,3} and set2={3,4,5} find union
set1={1,2,3}
set2={3,4,5}
uni =set1.union(set2)
print(uni)

#10 Given two sets find the intersection
set1={1,2,3}
set2={2,3,4}
inter=set1.intersection(set2)
print(inter)

#11 Find maximum and minimum value in a set
s={1,2,3,4}
maxi = max(s)
print(maxi)
mini = min(s)
print(mini)