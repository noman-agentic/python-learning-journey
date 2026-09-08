import calculator_tools

add_result = calculator_tools.add( 67, 9)
sub_result = calculator_tools.subtract( 56, 47)
print(add_result)
print(sub_result)

from calculator_tools import add
from calculator_tools import subtract

add_result = add(67, 87)
sub_result = subtract(76, 34)
print(add_result)
print(sub_result)

import calculator_tools as calc

add_result = calc.add(67, 87)
sub_result = calc.subtract(87, 34)
print(add_result)
print(sub_result)