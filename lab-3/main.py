from lab_python_fp.field import field
from lab_python_fp.random import gen_random
from lab_python_fp.unique import Unique
from lab_python_fp.sort import sort, sort_lambda
from lab_python_fp.print_result import print_result
from lab_python_fp.cm_timer import cm_timer_1, cm_timer_2

from time import sleep

def main():
  print('\t<!----field----!>')
  example = [
    {'title': 'Кровать'},
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'},
    {'title': 'Торшер', 'price': 100, 'color': 'black'},
    {'title': 'бумага. Поле price - None', 'price': None, 'color': 'black'},
    {'titleNone': 'None. Оба поля для выборки - None', 'price': None, 'color': None},
  ]
  for item in field(example, 'title', 'price'):
    print(item)
  print('\n')

  print('\t<!----random----!>')
  for item in gen_random(6, 10, 15):
    print(item)
  print('\n')

  print('\t<!----unique----!>')
  uniq_example = [1, 1, 1,4,3,4,3,3,3,3,3, 1, 1, 2, 2, 2, 2, 2]
  uniq_example_lower_strings = ["hello", "Hello", "hellO", "hi", "Hi"]
  uniq = Unique(uniq_example)
  print(f"-->test 1. ignore_case: {uniq.ignore_case()}")
  for item in uniq:
    print(item)

  uniq_str = Unique(uniq_example_lower_strings, ignore_case = True)
  print(f"\n-->test 2. ignore_case: {uniq_str.ignore_case()}")
  for item in uniq_str:
    print(item)
  print('\n')

  print('\t<!----sort----!>')
  sort_example = [4, -30, 100, -100, 123, 1, 0, -1, -4]
  print(sort(sort_example))
  print(sort_lambda(sort_example))

  print('\n\t<!----print_decorator_example----!>')
  @print_result
  def print_decorator_example1():
    return 1
  @print_result
  def print_decorator_example2():
      return 'iu5'
  @print_result
  def print_decorator_example4():
      return {'a': 1, 'b': 2}
  @print_result
  def print_decorator_example3():
      return [1, 2]
  print_decorator_example1()
  print_decorator_example2()
  print_decorator_example3()
  print_decorator_example4()

  print('\n<!----cm_timer----!>')
  with cm_timer_1():
      sleep(1)
  with cm_timer_2():
      sleep(1.5)

  print('\n<!----process_data----!>')


if __name__ == "__main__":
  main()