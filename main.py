import argparse

if __name__ == "__main__":
    # Argument parser to parse command line args
    parser: argparse.ArgumentParser = argparse.ArgumentParser(
        prog="Hello Program", description="A program that says hello to you"
    )
    # Receive name as string
    parser.add_argument("name", type=str, help="Your name")
    # Parse arguments and print name to stdout
    args: argparse.Namespace = parser.parse_args()
    print("Hello " + args.name)
