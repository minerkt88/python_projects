print('-------- Test Script: Running --------')

import spacing
import unittest

# error_message = 'Test did not work as expected.'

# test_list = [['apple','banana','carrot'],['date','egg','fruitcake']]
# result = spacing.getMaxSpacing(test_list,0)
# print(type(result))
# print(result)
# try:
#   if result == 2:
#     pass
#   else:
#     print(error_message)
# except:
#   print(error_message)

class TestAddFunction(unittest.TestCase):

  def test_getMaxSpacing(self):
      print('Testing getMaxSpacing...')

      test_list = [['apple','banana','carrot'],['date','egg','fruitcake']]
      result = spacing.getMaxSpacing(test_list,0)
      self.assertEqual(result, 2)

      test_list = [['apple','banana','carrot'],['date','egg','fruitcake']]
      result = spacing.getMaxSpacing(test_list,0)
      self.assertEqual(result, 2)

if __name__ == '__main__':
    unittest.main()
