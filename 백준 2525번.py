hours, m = map(int, input().split())
add_time = int(input())

m += add_time

while m >= 60:
    m -= 60
    hours += 1
    if hours >= 24:
        hours -= 24
        
print("{} {}".format(hours, m))
