from typing import List


class Helper:
    def __init__(self) -> None:
        pass

    def write(self, istr: str) -> None:
        with open("./outputs.txt", "w") as file1:
            file1.writelines(istr)

    def read(self) -> List:
        with open("./inputs.txt") as f:
            contents = f.readlines()
            return contents
