def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1

for num in count_up_to(15):
    print(num)

#this function generate the values to 15
