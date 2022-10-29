import json
import sys

from lab_python_fp.print_result import print_result
from lab_python_fp.cm_timer import cm_timer_1
from lab_python_fp.sort import sort
from lab_python_fp.random import gen_random
from lab_python_fp.unique import Unique
from lab_python_fp.field import field

path = 'data_light.json'

with open(path, 'r', encoding='utf8') as f:
    data = json.load(f)

# Далее необходимо реализовать все функции по заданию, заменив `raise NotImplemented`
# Предполагается, что функции f1, f2, f3 будут реализованы в одну строку
# В реализации функции f4 может быть до 3 строк

@print_result
def f1(arg):
  return sorted(
    Unique(
      (el['job-name'] for el in list(field(arg, 'job-name'))[0]),
      ignore_case=True
    )
  )

@print_result
def f2(arg):
    return list(filter(lambda el: el[0:11].lower()=='программист', arg))

@print_result
def f3(arg):
  return list(map(lambda el: el + ' с опытом Python', arg))

@print_result
def f4(arg):
  salary = list(gen_random(len(arg), 100000, 200000))
  work = list(zip(arg, salary))
  return list(map(lambda el: el[0] + ', зарплата ' + str(el[1]) + ' руб.', work))

def main():
    print('\tproccess_data.py')
    with cm_timer_1():
        print(f4(f3(f2(f1(data)))))



if __name__ == "__main__":
    main()