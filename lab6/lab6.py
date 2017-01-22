import turtle

def seq3np1(n): #starts with n and goes until it reaches n=1
    """Print the 3n+1 sequence from n, terminating when it reaches 1."""
    count = 0
    while n!=1:
        count += 1
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
    return count
def graphIterations(i):
    #create turtle and a window
    terp = turtle.Turtle()
    line = turtle.Turtle()
    wn = turtle.Screen()
    #set world coordinates
    wn.setworldcoordinates(0,0,10,10)
    wn.bgcolor('#d4c9e5')
    terp.goto(0,0)
    max_so_far = 0
    for n in range(1,i):
        result = seq3np1(n)
        if result >= max_so_far:
            max_so_far = result
            wn.setworldcoordinates(0,0,i,max_so_far+5)
        if result>100:
            line.goto(n-1,0)
            line.write("The iteration is " + str(result))
        terp.goto(n,result)
        line.goto(n,0)
        terp.dot()
    wn.exitonclick()

def main():
    ans = int(input("Please enter an upper bound for your range: "))
    for start in range(1, ans + 1): #you have to do ans + 1 to incorporate ans in the range
        print("The start value is", start, "with a number of", seq3np1(start), "iterations")
    graphIterations(ans)
        #Understanding this:
        #when start = n, n will run until it reaches 1
        #(the number of times it runs until it reaches 1) - 1 = # of iterations
        #therefore, seq3np1(start) = #number of times it runs until  it reaches 1 - 1
        #^aka count the numbers before 1

main()
