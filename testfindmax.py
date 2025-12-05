import unittest 
import os

from maxfinder import MaximumFinder

class TestMaxFinder(unittest.TestCase):

  def tearDown(self):

    dir_name = "."
    test = os.listdir(dir_name)

    for item in test:
      if item.endswith(".out"):
        os.remove(item)
      if item.endswith(".in"):
        os.remove(item)


  def test_1_find_max(self):

    file = open("input1.in", "w")
    for number in [4,5,9,1,4,3,16.0]:
      file.write(str(number) + "\n")
    file.close()

    m = MaximumFinder("input1.in")
    m.find_max("test1.out")

    file = open("test1.out")
    result = file.read()
    file.close()

    self.assertEqual(result, "16.0")


  def test_2_find_max(self):

    file = open("input2.in", "w")
    for number in [-5,-3,-2,-1]:
      file.write(str(number) + "\n")
    file.close()

    m = MaximumFinder("input2.in")
    m.find_max("test2.out")

    file = open("test2.out")
    result = file.read()
    file.close()

    self.assertEqual(result, "-1.0")


if __name__ == "__main__":
  unittest.main()
