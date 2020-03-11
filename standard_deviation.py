import math
import statistics
#### Steps
numbers =[1,2,3,4,5]
# get mean
num_mean  = sum(numbers)/len(numbers)
# subtract and square mean from each
nss = []
for num in numbers:
    new = num - num_mean
    new = new ** 2
    nss.append(new)
sub_sqr = [(num - num_mean)**2 for num in numbers]
print(f'check {nss}{sub_sqr}')
# Square root of mean from those ^
new_mean = sum(sub_sqr)/len(sub_sqr)
std_dev = math.sqrt(new_mean)
print(f'manual calc {std_dev}')
print(f'lib calc {statistics.stdev(numbers)}')