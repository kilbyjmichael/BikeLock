#!/usr/bin/python

'''Shows what the spinner looks like when a certain word is shown'''

bike_lock_c1 = ['d', 'm', 'r', 'f', 'b', 'l', 'p', 'w', 's', 't']

bike_lock_c2 = ['a', 'i', 'o', 'l', 'e', 'h', 'w', 'r', 'y', 'u']
    
bike_lock_c3 = ['n', 's', 'k', 'o', 'a', 'l', 'e', 'r', 'm', 't']

bike_lock_c4 = ['g', 'k', 'm', 's', 't', 'e', 'p', 'y', 'l', 'd'] # len = 10

def spin_ring(ring, times):
    max = len(ring)
    if times > max:
        return "Spun times must be shorter than the length of the ring."
    else:
      return ring[times:] + ring[:times]

def main():
    print spin_ring(bike_lock_c1, 3)
    print spin_ring(bike_lock_c2, 5)
    print spin_ring(bike_lock_c3, 5)
    print spin_ring(bike_lock_c4, 10)

if __name__ == "__main__": main()
