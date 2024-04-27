def calPoints(operations):
    new_arr = []
    for op in operations:
            if op == 'C':
                new_arr.pop()
            elif op == 'D':
                new_score = 2 * new_arr[len(new_arr) - 1]
                new_arr.append(new_score)  
            elif op == "+":
                new_score = new_arr[len(new_arr) - 1] + new_arr[len(new_arr) - 2]
                new_arr.append(new_score)
            else:
                new_arr.append(int(op))
    return print(sum(new_arr))
            
        
        


calPoints(["5","2","C","D","+"])