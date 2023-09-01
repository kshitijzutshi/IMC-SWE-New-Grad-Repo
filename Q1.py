"""
push n -> push n to TOP of stack
pop -> pop the TOP element of stack
inc i j -> Add j to bottom stack[:i] elements of stack
"""

"""
Addition Fns :

1. empty -> return True if empty else false
2. peek -> return top element of stack
3. sum -> return sum of all elements in stack

"""

def is_empty(stack):
    if len(stack) == 0:
        return True
    else:
        return False
def peek(stack):
    return stack.pop()
def stack_sum(stack):
    f = lambda l: l[0] if len(l) == 1 else l[0] + f(l[1:])
    sum_stack = f(list)
    return sum_stack
def push_n():
    pass
def pop_n(stack):
    return stack.pop()
def inc_i_j(i, j, stack):
    pass
    # stack = lambda x: x[]

# stack = []
# ops = ['push 4', 'push 5', 'inc 2 1', 'pop']

# for op in ops:
#     op_arr = op.split(" ")
#     if op_arr[0] == "push":
#         stack.append(op_arr[1])
#         print(stack)
#     elif op_arr[0] == "inc":
#         inc_i_j(op_arr[1], op_arr[2], stack)
#         print(stack)
#     elif op_arr[0] == "pop":
#         pop_n(stack)
#         print(stack)
#     elif op_arr[0] == "empty":
#         is_empty(stack)
#         print(stack)
#     elif op_arr[0] == "peek":
#         peek(stack)
#         print(stack)
#     elif op_arr[0] == "sum":
#         stack_sum(stack)
#         print(stack)
    
# print(stack)

a = 2
b = 1
c = [2,3,4,5]
d = 1
for i in range (c[2:][0], len(c[2:])):
    c[i]=c[i]+d
print(c)
