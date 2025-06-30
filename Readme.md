Problem Summary:
You have 2 eggs and 100 floors.

You want to minimize the maximum number of drops in the worst case.

Goal: Find the critical floor F such that the egg breaks if dropped from above F, and does not break from F or below.

With 2 eggs, the idea is to:

Use the first egg to reduce the search space smartly.

If it breaks, use the second egg to do a linear search from the last safe floor.

To minimize the worst-case drops:

Drop the first egg from floor x, then x-1, then x-2, ..., until 100 is covered.

Why decreasing steps? To balance both the linear search and total number of drops.

The equation to find the minimal number of drops k is:x + (x-1) + (x-2) + ... + 1 >= 100
=> x(x + 1)/2 >= 100
So, we compute the smallest x such that x(x + 1)/2 >= 100
