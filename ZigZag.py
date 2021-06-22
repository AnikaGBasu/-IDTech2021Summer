import turtle as t

t.speed(10)

def zigzag(length, depth):
  if depth < 1:
    #this is the base case
    return
  elif depth == 1:
    if depth % 2 == 0:
      t.color("blue")
    else:
      t.color("orange")

    t.left(90)
    t.fd(length/2)
    t.right(90)
    t.fd(length)
    t.back(length)
    t.right(90)
    t.fd(length)
    t.right(90)
    t.fd(length)
    t.back(length)
    t.right(90)
    t.fd(length/2)
    t.right(90)
  else:

    t.left(90)
    t.fd(length / 2)
    t.right(90)
    t.fd(length)
    t.left(45)

    zigzag(length/2, depth-1)

    if depth % 2 == 0:
      t.color("blue")
    else:
      t.color("orange")

    t.right(45)
    t.back(length)
    t.right(90)
    t.forward(length)
    t.left(90)
    t.back(length)
    t.left(45)

    zigzag(length/2, depth-1)


    if depth % 2 == 0:
      t.color("blue")
    else:
      t.color("orange")

    t.right(45)
    t.fd(length)
    t.left(90)
    t.fd(length / 2)
    t.right(90)

def main():
  depth = int(input("What depth do you want? "))
  t.pensize(3)
  t.speed(0)
  zigzag(200, depth)

main()

t.done()