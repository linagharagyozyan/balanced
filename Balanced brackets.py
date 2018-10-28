
def is_matched(input):
    opening = '({['
    closing = ')}]'
    balance = {opening[0]:closing[0],
               opening[1]:closing[1],
               opening[-1]:closing[-1]}
    my_stack = []

    for k in input:
        if k in opening:
            my_stack.append(balance[k])
        elif k in closing:
            if not my_stack or k != my_stack.pop():
                return False
    return not my_stack

print is_matched("asd[][]{{}}sd")
