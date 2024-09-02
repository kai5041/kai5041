import os

from sys import argv
from hashlib import sha256


def compare_hash(hash1, hash2):
    return hash1 == hash2


if __name__ == "__main__":
    if len(argv) == 1:
        print("Usage:\n  hck.py hash <archive>\nor\n  hck.py compare <hash> <archive>")
        exit(1)

    cmd = argv[1]

    match (cmd):
        case "hash":
            if len(argv) < 3:
                print("Provide an archive")
                exit(1)

            folder = argv[2]
            try:
                print(sha256(open(folder, "rb").read()).hexdigest())
            except FileNotFoundError:
                print(f"{folder} does not exist")
                exit(1)

        case "compare":
            if len(argv) < 4:
                print("Provide a hash and an archive")
                exit(1)
            
            hash = argv[2]
            src = argv[3]
            try:
                print(compare_hash(hash, sha256(open(src, "rb").read()).hexdigest()))
            except FileNotFoundError:
                print(f"{src} does not exist")
                exit(1)

        case unknown:
            print(f"{unknown} is not a valid command")
            exit(1)
