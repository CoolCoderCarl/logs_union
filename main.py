import sys

import logs_union
import parser_union

if __name__ == "__main__":
    parser = parser_union.create_parser()
    namespace = parser.parse_args(sys.argv[1:])

    logs_union.create_sorted_file(
        namespace.first_log, namespace.second_log, namespace.output_log
    )
