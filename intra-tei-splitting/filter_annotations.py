from anchor import Anchor
import json
import uuid

DOC_ID = 'r7v03z1i8vw0ag'
PART_ID = '55dce983-015b-446f-b759-f38087047fc2'

FROM_CHAPTER = 39
FROM_PARA = 1

TO_CHAPTER = 44
TO_PARA = 10

OFFSET_CHAPTER = 38

def isWithin(annotation, from_chapter, from_para, to_chapter, to_para):
  anchor = Anchor(annotation['anchor'])
  if anchor.isValid():
    return anchor.isWithin(from_chapter, from_para, to_chapter, to_para)
  else:
    return False

with open('./output/annotations_original.jsonl', 'r') as infile, \
  open(f'./output/annotations.{PART_ID}.jsonl', 'w') as outfile:

  all_annotations = infile.readlines()
  print(f'Read {len(all_annotations)} annotations total')
  as_json = list(map(lambda str: json.loads(str), all_annotations))

  # Keep only annotations on the relevant part
  relevant_annotations = list(filter(lambda a: isWithin(a, FROM_CHAPTER, FROM_PARA, TO_CHAPTER, TO_PARA), as_json))

  for annotation in relevant_annotations:
    # Assign new annotation- and version-UUID
    annotation['annotation_id'] = str(uuid.uuid4())
    annotation['version_id'] = str(uuid.uuid4())
    annotation['anchor'] = Anchor(annotation['anchor']).offset_by(OFFSET_CHAPTER, 0)

    # Replace doc & part ID
    annotation['annotates']['document_id'] = DOC_ID
    annotation['annotates']['filepart_id'] = PART_ID

    outfile.write(f'{json.dumps(annotation)}\n')

  print(f'Keeping {len(relevant_annotations)} annotations')