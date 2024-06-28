import random


# This class is used to generate a code to be added in saved image names while converting a PDF into images
class CodeGenerator:
    numbers: list = [x for x in range(10)]
    @staticmethod
    def generate_code(length: int):
        code = ''
        for i in range(length):
            code += str(random.choice(CodeGenerator.numbers))
        return code