from argparse import ArgumentParser, Namespace

# from https://www.youtube.com/watch?v=idq6rTYqvkY

# from https://www.youtube.com/watch?v=aGy7U5ItLRk

parser = ArgumentParser()

parser.add_argument("square", help="Squares a given number", type=int, default=0)
# parser.add_argument("-v", "--verbose", 
#                     help="Provides a verbose description", 
#                     action="store_true")
# parser.add_argument("-v", "--verbose", 
#                     help="Provides a verbose description", 
#                     type=int, 
#                     choices=[0, 1, 2])

parser.add_argument("-v", "--verbose", 
                    help="Verbose desc. Use '-vv' for extra verbose", 
                    action="count")
args: Namespace = parser.parse_args()
result: int = args.square ** 2 

if args.verbose == 1:
    print(f"the result is {result}")
elif args.verbose == 2:
    print(f"{args.square} ** {args.square} = {result}")
else:
    print(result)

# if args.verbose:
#     print(f"{args.square} squared is: {args.square ** 2}")

# else: 
#     print(args.square ** 2)