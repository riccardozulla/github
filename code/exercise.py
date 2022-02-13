from typing import Sequence

def sum (x: float, y: float) -> float:
    return x+y

def count (data: Sequence[float]) -> int:
    count=0
    for _ in data:
        count+=1
    return count

x=1.3
y=4.1

print(sum(x, y))
data = (1,2,3,4,5,6,7,8,9)
print(count(data))
