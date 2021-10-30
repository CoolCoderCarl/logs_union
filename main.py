import sys
import parserUnion
import logsUnion

if __name__ == '__main__':
    parser = parserUnion.createParser()
    namespace = parser.parse_args(sys.argv[1:])

    logsUnion.createSortedFile(namespace.first_log, namespace.second_log, namespace.output_log)
