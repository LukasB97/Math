from typing import List

from src.Algebra.Structures.Function.Operator import OperatorMapping
from src.Algebra.Structures.Function.Operator.ComputationalGraphPart import ComputationalGraphPart
from src.Algebra.Structures.Function.Variable import Variable


class FunctionParser:

    @classmethod
    def parse_brackets(cls, definition_input: list) -> List[ComputationalGraphPart]:
        definition = list()
        last_end = 0
        while "(" in definition_input[last_end:]:
            start = definition_input.index("(", last_end)
            end_index = cls.get_bracket_section(definition_input, start)
            definition += definition_input[last_end:start]
            last_end = start + end_index + 1
            definition.append(cls.parse_list(definition_input[start + 1: end_index]))
        definition += definition_input[last_end + 1:]
        assert "(" not in definition and ")" not in definition
        return definition

    @classmethod
    def parse_string(cls, definition_string: str):
        definition_string = cls.preprocess_string(definition_string)
        definition = cls.build_definition_list(definition_string)
        if "(" in definition_string:
            definition = cls.parse_brackets(definition)
        definition = cls.build_section_graph(definition)
        return definition[0]

    @classmethod
    def parse_list(cls, definition):
        if "(" in definition:
            definition = cls.parse_brackets(definition)
        definition = cls.build_section_graph(definition)
        return definition[0]

    @classmethod
    def build_definition_list(cls, definition_string: str):
        definition = list()
        is_number = False
        number = ""
        for i in range(len(definition_string)):
            if definition_string[i].isnumeric() or (definition_string[i] in [",", "."] and is_number):
                number += definition_string[i]
                is_number = True
            elif is_number:
                is_number = False
                definition.append(float(number))
                number = ""
            elif definition_string[i] in OperatorMapping.operator_mapping:
                definition.append(definition_string[i])
            elif definition_string[i].isalpha():
                definition.append(Variable(definition_string[i]))
            elif definition_string[i] in ["(", ")"]:
                definition.append(definition_string[i])
        if is_number:
            definition.append(float(number))
        return definition

    @classmethod
    def preprocess_string(cls, definition_string: str) -> str:
        definition_string = definition_string.replace(" ", "")
        definition_string = cls.preprocess_multiply(definition_string)
        return definition_string

    @classmethod
    def preprocess_multiply(cls, definition_string: str) -> str:
        for i in range(len(definition_string) - 1):
            if definition_string[i].isalpha():
                if definition_string[i + 1].isalnum() or definition_string[i + 1] == "(":
                    definition_string = cls.preprocess_multiply(
                        definition_string[:i + 1] + "*" + definition_string[i + 1:])
                    break
            if definition_string[i] == ")":
                if definition_string[i + 1].isalnum() or definition_string[i + 1] == "(":
                    definition_string = cls.preprocess_multiply(
                        definition_string[:i + 1] + "*" + definition_string[i + 1:])
                    break
        return definition_string


    @classmethod
    def get_highest_priority_operation_index(cls, definition: list):
        for i in range(len(OperatorMapping.operator_priority)):
            if OperatorMapping.operator_priority[i] in definition:
                return definition.index(OperatorMapping.operator_priority[i])
        raise RuntimeError(definition)

    @classmethod
    def build_section_graph(cls, definition: list):
        assert "(" not in definition
        while len(definition) > 1:
            highest_priority = cls.get_highest_priority_operation_index(definition)
            op = cls.build_operation(*definition[highest_priority - 1: highest_priority + 2])
            definition[highest_priority] = op
            del definition[highest_priority + 1]
            del definition[highest_priority - 1]
        assert len(definition) == 1
        return definition[0]


    @classmethod
    def build_operation(cls, left_op, operation, right_op):
        return OperatorMapping.operator_mapping[operation](left_op, right_op)




    @classmethod
    def get_bracket_section(cls, definition: list, start_index):
        """
        :param definition:
        :param start_index:
        :return: index of the bracket, closing the secction that was opened by the start index
        """
        assert definition[start_index] == "("
        opening_count = 1
        closing_count = 0
        for i in range(start_index + 1, len(definition)):
            if definition[i] == "(":
                opening_count += 1
            elif definition[i] == ")":
                closing_count += 1
            if opening_count == closing_count:
                return i
        raise ValueError("Invalid Format: " + str(definition))
