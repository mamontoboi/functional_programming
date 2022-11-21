def vol(r1, r2):
    v1 = 4 / 3 * 3.1415 * r1 ** 3
    v2 = 4 / 3 * 3.1415 * r2 ** 3
    v = v1 - v2
    return round(v, 3)


print(vol(5, 3))

def fibonacci(n):
    fib_1, fib_2 = 1, 1
    for n in range(n):
        fib_1, fib_2 = fib_2, fib_1 + fib_2
    return fib_1, fib_2


print(fibonacci(50))

class Person:
    def __init__(self, id):
        self.id = id
        id = 666


acc = Person(123)
print(acc.id)

import copy

alist = [1, 2, None, (), [],]

print(len(alist))
blist = ["a", "b"]

print(r"\nwoow")

print(type(lambda: None))

print("\n".join(blist))

if 3 in blist:
    print('hey')

print("\x48\x49!")

x = 4.5
y = 2
print(x//y)

set = {1, 2, 3}

if 2 in set:
    print('2')

dc = {1: 2}

if 1 in dc:
    print('dc')

b = blist + [1]
print(b)

kvps ={'1': alist, '2': blist}

thecopy = copy.deepcopy(kvps)

kvps['1'][0] = 5

sum = kvps['1'][0] + thecopy['1'][0]

print(sum)

foo = {}
print(len(foo))  # 0

#
# PUT
# The PUT method requests that the target resource create or update its state with the state defined by the
# representation enclosed in the request. A distinction from POST is that the client specifies the target location on
# the server.

# POST
# For example, it is used for posting a message to an Internet forum, subscribing to a mailing list, or completing an
# online shopping transaction

# GET
# The GET method requests that the target resource transfer a representation of its state. G
# ET requests should only retrieve data and should have no other effect.

# CONNECT
# The CONNECT method requests that the intermediary establish a TCP/IP tunnel to the origin server
# identified by the request target.
#
# All general-purpose web servers are required to implement at least the GET and HEAD methods,
# and all other methods are considered optional by the specification.