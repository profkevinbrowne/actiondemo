
class MaximumFinder:

  def __init__(self, filename):
    self.file = open(filename)
    self.lines = self.file.readlines()
    self.file.close()

  def find_max(self, output_filename):
    numbers = [float(line) for line in self.lines]
    output_file = open(output_filename, "w")
    output_file.write(str(min(numbers)))
    output_file.close()

