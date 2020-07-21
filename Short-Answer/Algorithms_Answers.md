#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
    Answer - O(n)
    Justification - The loop will run until a >= n^3.  The variable a increments each time through the loop at a rate of n^2. Since a starts at 0, a will need to increment n times before the condition is met to stop the loop.  Or n^2 (increment value) * n (number of times through the loop) will equal n^3 (condition needed to stop the loop)


b)
    Answer - O(nlog(n))
    Justification - The first loop will run n times.  The number of times the second loop runs will increase as n increases, but not at a slower rate than the rate n increases.  For examples, if n is 3, the inner while loop will only run 2 times. If n is 8 the while loop will only run 3 times.  So the number of loops increases at a fraction of the rate n increases.


c) Answer - O(n) (or O(n + 1) to be precise)

In this recursive algorithm, n will be reduced by 1 and ran through the recursive function until n hits the base case of 0.  Thus the function will run n times, plus an additional time to bring it all the way to zero.

## Exercise II


Understand = Find the lowest floor at which the egg will break (f)
Plan
    1. Go to the floor right in the middle of the building (n//2) and drop an egg
    2. 
        - If the egg breaks consider all floors below the floor you are on and determine the middle point of that group of floors
        - If the egg doesn't break consider all floors above the floor you are on and determine the middle point of that group of floors
    3.  Keep repeating this process until you move only one floor between egg drops.  
    4.  Once you reached the point where you have only moved one floor, if the egg breaks you are on f and the egg will break at all points above that floor.  If the egg doesn't break, the floor above it is f.

Big-O - log(n) - Under this process the worst case scenario for runtime will increase as n increases, but only at a fraction of the rate of n.  This is very similar to a binary search except we won't know the value of f so we will have to continue until we are down to two choices and perform our last egg drop.



