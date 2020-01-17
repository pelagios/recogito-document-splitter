from anchor import Anchor
import json

FROM_CHAPTER = 1
FROM_PARA = 1

TO_CHAPTER = 2
TO_PARA = 2

def isWithin(annotation, from_chapter, from_para, to_chapter, to_para):
  anchor = Anchor(annotation['anchor'])
  if anchor.isValid():
    anchor.isWithin(from_chapter, from_para, to_chapter, to_para)
  else:
    False

with open('./original/annotations.jsonl', 'r') as infile:

  all_annotations = infile.readlines()
  print(f'Read {len(all_annotations)} annotations total')
  as_json = list(map(lambda str: json.loads(str), all_annotations))

  # Keep only annotations on the relevant part
  relevant_annotations = list(filter(lambda a: isWithin(a, 1, 1, 10, 10), as_json))

  print(f'Keeping {len(relevant_annotations)} annotations')