import re
from pathlib import Path

import pandas as pd


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "input",
        help="Path to logs file")
    parser.add_argument(
        "output",
        help="Path to output csv file")
    return parser.parse_args()


def main():
    args = get_args()
    columns=(
            'epoch', 'step', 'batches_seen', 'lr', 'ms/batch', 'loss', 'ppl')
    df = DataFrame(columns=columns)
    number_pattern = re.compile('[0-9\.]+')
    with open(Path(args.input)) as f:
        for line in f:
            number_strings = number_pattern.findall(line)
            numbers = [
                float(s) if '.' in s else int(s) for s in number_strings]
            new_row = dict(zip(columns, numbers))
            df.append(new_row)
    df.to_csv(args.output)

            

if __name__ == '__main__':
    main()
