# 
import os
from typing import List, TypeVar

def list_up(path:str) -> None:
    return os.listdir(path)

def write_into_csv(items:List, path:str) -> None:
    with open(path, 'w') as f:
        for item in items:
            f.writelines(item + '\n')

def main() -> None:
    addr:str = r"D:\DevEnv"
    write_into_csv(list_up(addr), './tools/devenv.csv')

if __name__ == '__main__':
    main()