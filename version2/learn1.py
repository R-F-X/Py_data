from argparse import ArgumentParser, Namespace

parser = ArgumentParser()

# parser.usage = "Use it like this"
parser.add_argument("a", type=int, help="The base value", default=0)
parser.add_argument("b", type=int, help="The exponent", default=0)
parser.add_argument("-v", "--verbose", action="count",
                    help="Provides verbose version")
# parser.add_argument("s", "--silence", action="store_true",
#                     help="silent version")


args: Namespace = parser.parse_args()
result: int = args.a ** args.b 

match args.verbose:
    case 1:
        print(f"The result is {result}")

    case 2:
        print(f"{args.a} ** {args.b} = {result}")

    case _:
        print(result)    