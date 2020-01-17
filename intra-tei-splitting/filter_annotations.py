from anchor import Anchor
import json
import uuid

DOC_ID = 'q25vx8179944yk'
PART_ID = '9d62ed7a-ef9b-4e89-a885-0e61a2cab8a0'

FROM_CHAPTER = 1
FROM_PARA = 1

TO_CHAPTER = 5
TO_PARA = 5

def isWithin(annotation, from_chapter, from_para, to_chapter, to_para):
  anchor = Anchor(annotation['anchor'])
  if anchor.isValid():
    return anchor.isWithin(from_chapter, from_para, to_chapter, to_para)
  else:
    return False

with open('./original/annotations.jsonl', 'r') as infile, \
  open(f'./original/annotations.{PART_ID}.jsonl', 'w') as outfile:

  all_annotations = infile.readlines()
  print(f'Read {len(all_annotations)} annotations total')
  as_json = list(map(lambda str: json.loads(str), all_annotations))

  # Keep only annotations on the relevant part
  relevant_annotations = list(filter(lambda a: isWithin(a, FROM_CHAPTER, FROM_PARA, TO_CHAPTER, TO_PARA), as_json))

  for annotation in relevant_annotations:
    # Assign new annotation- and version-UUID
    annotation['annotation_id'] = str(uuid.uuid4())
    annotation['version_id'] = str(uuid.uuid4())

    # Replace doc & part ID
    annotation['annotates']['document_id'] = DOC_ID
    annotation['annotates']['filepart_id'] = PART_ID

    outfile.write(f'{json.dumps(annotation)}\n')

  print(f'Keeping {len(relevant_annotations)} annotations')