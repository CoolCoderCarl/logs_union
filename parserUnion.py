import argparse


def createParser():
    root_parser = argparse.ArgumentParser(
        prog='''logsunion''',
        description='''Program for JSON lines logs union''',
        epilog='''(c) CoolCoderCarl'''
    )

    root_parser.add_argument('first_log')

    root_parser.add_argument('second_log')

    root_parser.add_argument('-o', '--output', dest='output_log')

    return root_parser