from Core.AbstractFactory import AbstractFactory


class MatrixStructureFactory(AbstractFactory):

    def _replacements(self, input_str: str):
        input_str = input_str.replace(" ", "")
        input_str = input_str.replace("{", "[")
        input_str = input_str.replace("}", "]")
        chars = set(input_str)
        input_str = input_str.replace("][", "],[")
        if input_str[:2] != "[[":
            input_str = "[[" + input_str[1:]
        if input_str[-2:] != "]]":
            input_str = input_str[-1:] + "]]"
        return input_str




    def _parse_bracket_separator(self, input_str):
        assert input_str.count("[") == input_str.count("]")
        input_str = input_str.
        input_str = input_str.replace(";", ",")



    def _parse_semicolon_seperator(self, input_str):
        pass

    def parse_string(self, input_str):
        input_str = self._replacements(input_str)
        if "[" in input_str:
            return self._parse_bracket_separator(input_str)
        return self._parse_semicolon_seperator(input_str)

    def parse_array(self, input_arr):
        pass

    def create_instance(self, input_to_parse):
        if isinstance(input_to_parse, str):
            return self.parse_string(input_to_parse)
        return self.parse_array(input_to_parse)

