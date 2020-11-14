'''
Eugene Bellau
11/6/2020
AgileUnoModule7
'''
import pdb

import pprint

import my_module

from my_module import my_json_data as my_data

from my_module import my_json_data
# 1. import my_module and the pretty print module
# Add a breakpoint to test data
pdb.set_trace()


# 2. Use the gretting method from my_module to print out your name
greet = my_module.greeting("Eugene")
print(greet)
pdb.set_trace()

# 3. Use the letter_text module to print out a string
letter = my_module.letter_text(name="Sam", amount="10,000", denomination="dollars")
print(letter)
pdb.set_trace()

# 4. Use the my_module.my_json.data and print it out
print(my_json_data)
pdb.set_trace()

# 5. Import the my_json_data as my_data and print out the my_data using pretty print
pprint.pprint(my_data)
pdb.set_trace()
