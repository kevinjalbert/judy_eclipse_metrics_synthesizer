from xlrd import open_workbook
import argparse

class JudyEclipseMetricsSynthesizer():

  # The list of mutation information from xls file
  names = None
  numberOfMutants = None
  numberOfKilledMutants = None

  # Dictionaries
  mutationScores = {} # [label:score]
  labelsLineNumber = {} # [line:label]

  # Files
  xlsFile = None
  metricsFile = None
  labelFile = None

  def get_mutation_score(self, label):
    for index in range(len(self.names)):
      if self.names[index] == label:
        if self.numberOfMutants[index] == 0:
          return -1  # 100%, no mutations at all
        elif self.numberOfKilledMutants[index] == 0:
          return 0  # 0%, with mutations
        else:
          return self.numberOfKilledMutants[index] / self.numberOfMutants[index]
    return -2  # Did not match anything

  def write_mutation_scores(self):
    libsvmFile = open(self.metricsFile, 'r')
    synthLibsvmFile = open('synth_' + self.metricsFile, 'w')
    lineNumber = 0
    for line in libsvmFile:
      lineNumber += 1

      # Get line number's mutationScore
      if lineNumber in self.labelsLineNumber:

        # Write out the category of the mutationScore
        mutationScore = self.mutationScores[self.labelsLineNumber[lineNumber]]
        if mutationScore >= 0.000000000000 and mutationScore <= 0.333333333333 :
          synthLibsvmFile.write(line.replace('-1', '0', 1))
        elif mutationScore > 0.333333333333 and mutationScore <= 0.666666666666 :
          synthLibsvmFile.write(line.replace('-1', '1', 1))
        elif mutationScore > 0.666666666666 and mutationScore <= 1.000000000000 :
          synthLibsvmFile.write(line.replace('-1', '2', 1))
        else:
          raise Exception("ERROR MUTATION SCORE > 1 OR MUTATION SCORE < 0 ", mutationScore)

    libsvmFile.close()
    synthLibsvmFile.close()

  def create_synth_labels(self):
    # Create synthLabelFile by checking for lineNumber presence
    labelFile = open(self.labelFile, 'r')
    synthLabelFile = open('synth_' + self.labelFile, 'w')
    lineNumber = 0
    for line in labelFile:
      lineNumber += 1
      if lineNumber in self.labelsLineNumber:
        synthLabelFile.write(line)
    labelFile.close()
    synthLabelFile.close()

  def synthesize(self):

    # Open xls file
    book = open_workbook(self.xlsFile)
    sheet = book.sheet_by_index(0)

    # Acquire names, number of mutants and number of mutants killed
    self.names = sheet.col_values(0)
    self.numberOfMutants = sheet.col_values(1)
    self.numberOfKilledMutants = sheet.col_values(2)

    # Read in labels from labelFile
    labelFile = open(self.labelFile, 'r')
    lineNumber = 0
    for label in labelFile:
      lineNumber += 1
      label = label.strip()
      score = self.get_mutation_score(label)
      if not score == None and score >= 0:
        self.mutationScores[label] = score
        self.labelsLineNumber[lineNumber] = label
    labelFile.close()

    # Replace first word on line in libsvmFile with mutation score
    self.write_mutation_scores()

    # Make the new synthLabelFile to reflect the synthLibsvmFile
    self.create_synth_labels()

def main(xlsFile, metricsFile, labelFile):
  synthesizer = JudyEclipseMetricsSynthesizer()

  synthesizer.xlsFile = xlsFile
  synthesizer.metricsFile = metricsFile
  synthesizer.labelFile = labelFile

  synthesizer.synthesize()

# If this module is ran as main
if __name__ == '__main__':

  # Define the argument options to be parsed
  parser = argparse.ArgumentParser(
      description = '',
      version = '')
  parser.add_argument(
      '-x',
      action='store',
      default=None,
      dest='xlsFile',
      help='Input XLS file produced by mutation testing tool Judy')
  parser.add_argument(
      '-m',
      action='store',
      default=None,
      dest='metricsFile',
      help='Input libsvm metrics file')
  parser.add_argument(
      '-l',
      action='store',
      default=None,
      dest='labelFile',
      help='Input libsvm label file')

 # Parse the arguments passed from the shell
  userArgs = parser.parse_args()

  if userArgs.xlsFile == None:
    raise Exception("ERROR NO FILE SPECIFIED", "XLSFILE")
  if userArgs.metricsFile == None:
    raise Exception("ERROR NO FILE SPECIFIED", "METRICSFILE")
  if userArgs.labelFile == None:
    raise Exception("ERROR NO FILE SPECIFIED", "LABELFILE")

  main(userArgs.xlsFile, userArgs.metricsFile, userArgs.labelFile)
