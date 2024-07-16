T = int(input())
while T > 0:
    N, V1, V2 = map(int, input().split())
    elevator_time = (N *2) / V2
    stair_time = (N * 1.4142135623730951) / V1
    
    if elevator_time < stair_time:
        print("Elevator")
    else:
        print("Stairs")
    
    T -= 1

