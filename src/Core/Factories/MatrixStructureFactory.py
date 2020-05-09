import re

from src.Core.AbstractFactory import AbstractFactory


class MatrixStructureFactory(AbstractFactory):

    @staticmethod
    def parse_string(input_str: str):
        input_str = input_str.replace(" ", "")
        input_str = input_str.replace(";", ",")
        input_str = re.sub('[{(]+', '[', input_str)
        input_str = re.sub('[})]+', ']', input_str)
        input_str = input_str.replace("],[", "];[")
        input_str = input_str.replace("[[", "[")
        input_str = input_str.replace("]]", "]")
        rows = input_str.split(";")
        for i in range(len(rows)):
            rows[i] = rows[i][1:-1].split(",")
            rows[i] = [float(x) for x in rows[i]]
        return rows

    def parse_array(self, input_arr):
        pass

    def create_instance(self, input_to_parse):
        if isinstance(input_to_parse, str):
            return self.parse_string(input_to_parse)
        return self.parse_array(input_to_parse)
