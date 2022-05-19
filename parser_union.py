import argparse


def create_parser():
    root_parser = argparse.ArgumentParser(
        prog="""logsunion""",
        description="""Program for JSONL logs union""",
        epilog="""(c) CoolCoderCarl""",
    )

    root_parser.add_argument("first_log")

    root_parser.add_argument("second_log")

    root_parser.add_argument("-o", "--output", dest="output_log")

    return root_parser


if __name__ == "__main__":
    pass
