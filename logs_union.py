import json


def create_sorted_file(
    path_to_first_log: str, path_to_second_log: str, path_lo_result_log: str
):
    with open(path_to_first_log) as fl:
        log1 = fl.read()

    with open(path_to_second_log) as sl:
        log2 = sl.read()

    union_data = log1 + log2

    union_list = [json.loads(json_line) for json_line in union_data.splitlines()]

    sorted_list = sorted(union_list, key=lambda k: k["timestamp"])

    with open(path_lo_result_log, "w") as outfile:
        for entry in sorted_list:
            json.dump(entry, outfile)
            outfile.write("\n")


if __name__ == "__main__":
    pass
