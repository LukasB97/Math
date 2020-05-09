from src.Algebra.Structures.Function import TranscendentalFunctionMapping
from src.Algebra.Structures.Function.Operation import OperatorMapping
from src.Algebra.Structures.Function.Parser.Replacements import replace_with
from src.Algebra.Structures.Function.Variable import Variable


class FunctionStringParser:

    def parse_string(self, definition_string: str):
        definition_string = self.preprocess_string(definition_string)
        return self.build_definition_list(definition_string)  #

    @staticmethod
    def _parse_number(is_number, current_number, current_char) -> (bool, bool, str):
        finished = False
        if current_char.isnumeric() or (current_char in [",", "."] and is_number):
            current_number += current_char
            is_number = True
        elif is_number:
            is_number = False
            finished = True
        return finished, is_number, current_number

    def build_definition_list(self, definition_string: str):
        definition = list()
        is_number = False
        number = ""
        for i in range(len(definition_string)):
            parsing_finished, is_number, number = self._parse_number(is_number, number, definition_string[i])
            if parsing_finished:
                definition.append(float(number))
                number = ""
            if definition_string[i] in OperatorMapping.operator_mapping:
                definition.append(definition_string[i])
            elif definition_string[i].isalpha():
                definition.append(Variable(definition_string[i]))
            elif definition_string[i] in ["(", ")"]:
                definition.append(definition_string[i])
        if is_number:
            definition.append(float(number))
        return definition

    def preprocess_string(self, definition_string: str) -> str:
        new_definition = ""
        for i in range(len(definition_string)):
            c = definition_string[i]
            if c in replace_with:
                new_definition += replace_with(c)
            else:
                new_definition += c
        new_definition = self.replace_transcendental_functions(new_definition)
        return new_definition

    @staticmethod
    def replace_transcendental_functions(definition_string):
        for expression, replacement in TranscendentalFunctionMapping.replacement.items():
            definition_string = definition_string.replace(expression, replacement)
        return definition_string
