# IMPORTANT: this helper ONLY works for the 
# Periegesis annotations - it's NOT a generic 
# anchor parser!!
import re 

class Anchor:

  def __init__(self, str):
    # Example:
    # from=/TEI[1]/text[1]/body[1]/div[1]/div[1]/div[23]/div[2]/p[1]::107;to=/TEI[1]/text[1]/body[1]/div[1]/div[1]/div[23]/div[2]/p[1]::122
    self.str = str

    self.start, self.end = str.split(';')
    self.from_path = self.start.split('/')
    self.to_path = self.end.split('/')

    # Strip tags, keep numbers only
    self.from_path = list(map(lambda str: int(re.sub("[^0-9]", "", str)) if '[' in str else str, self.from_path))
    self.to_path = list(map(lambda str: int(re.sub("[^0-9]", "", str)) if '[' in str else str, self.to_path))

  def isWithin(self, start_chapter, start_section, end_chapter, end_section):
    # Chapter is path segment 6, section path segment 7
    annotation_start_chapter = self.from_path[6]
    annotation_start_section = self.from_path[7]

    annotation_end_chapter = self.to_path[6]
    annotation_end_section = self.to_path[7]

    # Annotation starts after the interval starts
    is_start_after_interval_start = annotation_start_chapter > start_chapter or \
      (annotation_start_chapter == start_chapter and annotation_start_section >= start_section)

    # Annotation ends before the interval ends
    is_start_before_interval_end = annotation_start_chapter < end_chapter or \
      (annotation_start_chapter == end_chapter and annotation_end_section <= end_section)

    # Annotation ends after the interval starts
    is_end_after_interval_start = annotation_end_chapter > start_chapter or \
      (annotation_end_chapter == start_chapter and annotation_end_section >= start_section)

    # Annotation ends before the interval ends
    is_end_before_interval_end = annotation_end_chapter < end_chapter or \
      (annotation_end_chapter == end_chapter and annotation_end_section <= end_section)

    # Start is within the interval
    is_within = is_start_after_interval_start and is_start_before_interval_end \
      and is_end_after_interval_start and is_end_before_interval_end # End is within the interval

    '''
    if is_within:
      print(f'{start_chapter}.{start_section} - {end_chapter}.{end_section} contains')
    else:
      print(f'{start_chapter}.{start_section} - {end_chapter}.{end_section} does NOT contain')
    
    print(self.str)
    '''

    return is_within

  def isValid(self):
    return self.start.find('/') > -1 and self.end.find('/') > -1

  def offset_by(self, chapter, section):
    if (chapter == 0 and section == 0):
      return self.str
    else: 
      offset_start_chapter = self.from_path[6] - chapter
      offset_start_section = self.from_path[7] - section if self.from_path[6] - chapter == 1 else self.from_path[7]
      char_start = self.start.split('::')[1]

      offset_end_chapter = self.to_path[6] - chapter
      offset_end_section = self.to_path[7] - section if self.to_path[6] - chapter == 1 else self.to_path[7]
      char_end = self.end.split('::')[1]
      return f'from=/TEI[1]/text[1]/body[1]/div[1]/div[1]/div[{offset_start_chapter}]/div[{offset_start_section}]/p[1]::{char_start};to=/TEI[1]/text[1]/body[1]/div[1]/div[1]/div[{offset_end_chapter}]/div[{offset_end_section}]/p[1]::{char_end}'
