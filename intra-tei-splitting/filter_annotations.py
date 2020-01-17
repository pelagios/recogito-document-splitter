from anchor import Anchor
import json

FROM_CHAPTER = 1
FROM_PARA = 1

TO_CHAPTER = 2
TO_PARA = 2

with open('./original/annotations.jsonl', 'r') as infile:

  all_annotations = infile.readlines()
  print(f'Read {len(all_annotations)} annotations total')
  as_json = list(map(lambda str: json.loads(str), all_annotations))

  # Keep only annotations on the relevant part
  relevant_annotations = list(filter(lambda a: Anchor(a['anchor']).isTrue(), as_json))