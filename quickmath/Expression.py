import random
import math


# GENERATE RANDOM EXPRESSION WITH AN EXPRESSION TREE RECURSIVELY
# LEFT, OPERATOR, RIGHT
class Expression(object):
  OPERATIONS = ['+', '-', '*']

  GROUP_PROB = 0.5

  MIN_NUM, MAX_NUM = 0, 20

  def __init__(self, max_num_of_numbers, max_depth, depth):
    if max_depth is None:
      max_depth = math.log(max_num_of_numbers, 2) - 1

    if depth < max_depth and random.randint(0, max_depth) > depth:
      self.left = Expression(max_num_of_numbers, max_depth, depth + 1)
    else:
      self.left = random.randint(Expression.MIN_NUM, Expression.MAX_NUM)

    if depth < max_depth and random.randint(0, max_depth) > depth:
      self.right = Expression(max_num_of_numbers, max_depth, depth + 1)
    else:
      self.right = random.randint(Expression.MIN_NUM, Expression.MAX_NUM)

    self.grouped = random.random() < Expression.GROUP_PROB
    self.operator = random.choice(Expression.OPERATIONS)

  def __str__(self):
    s = '{0!s} {1} {2!s}'.format(self.left, self.operator, self.right)
    if self.grouped:
      return '({0})'.format(s)
    else:
      return s
