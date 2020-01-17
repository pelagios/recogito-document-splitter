# IMPORTANT: this helper ONLY works for the 
# Periegesis annotations - it's NOT a generic 
# anchor parser!!
import re 

class Anchor:

  def __init__(self, str):
    # Example:
    # from=/TEI[1]/text[1]/body[1]/div[1]/div[1]/div[23]/div[2]/p[1]::107;to=/TEI[1]/text[1]/body[1]/div[1]/div[1]/div[23]/div[2]/p[1]::122
    self.start, self.end = str.split(';')
    self.from_path = self.start.split('/')
    self.to_path = self.end.split('/')

    # Strip tags, keep numbers only
    self.from_path = list(map(lambda str: int(re.sub("[^0-9]", "", str)) if '[' in str else str, self.from_path))
    self.to_path = list(map(lambda str: int(re.sub("[^0-9]", "", str)) if '[' in str else str, self.to_path))

  def isWithin(self, from_chapter, from_para, to_chapter, to_para):
    # Chapter is path segment 6, section path segment 7
    self.from_path[6] >= from_chapter and \
    self.from_path[7] >= from_para and \
    self.to_path[6] <= to_chapter and \
    self.to_path[7] <= to_para

  def isValid(self):
    self.start.find('/') > -1 and self.end.find('/') > -1
