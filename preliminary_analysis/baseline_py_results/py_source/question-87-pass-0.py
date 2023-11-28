# Print the nodes of the Binary Tree whose height is a Prime number. 
MAX = 100000
graph = [[]for i in range(MAX + 1)]
Prime = [True for i in range(MAX + 1)]
height = [0 for i in range(MAX + 1)]


def SieveOfEratosthenes(): 
    # Create a boolean array "prime[0..n]" and initialize 
    # all entries it as true. A value in prime[i] will 
    # finally be false if i is Not a prime, else true. 
    for i in range(2, MAX + 1): 
        Prime[i] = True
  
    # Print the list of prime numbers and store them in 
    # prime[] 
    p = 2
    while (p * p <= MAX): 
        if (Prime[p] == True): 
            for i in range(p * p, MAX + 1, p): 
                Prime[i] = False
        p += 1
  
    # Print all prime numbers 
    for p in range(2, MAX): 
        if (Prime[p]): 
            print(p)


def height_of_tree(root):
    if root is None:
        return 0
    else:
        left = height_of_tree(root.left)
        right = height_of_tree(root.right)
        if left > right:
            height[root.data] = left + 1
        else:
            height[root.data] = right + 1
        return max(left, right) + 1


def print_nodes_of_height(root, h):
    if root is None:
        return
    if height[root.data] == h:
        print(root.data, end=" ")
    print_nodes_of_height(root.left, h)
    print_nodes_of_height(root.right, h)


def print_nodes_of_height_prime(root, h):
    if root is None:
        return
    if height[root.data] == h:
