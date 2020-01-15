# A utility to re-write the annotations.jsonl file for splitting documents.
# Takes the following input arguments
# -d the new document ID
# -o the old document part UUID
# -n the new document part UUID
import argparse
import json
import uuid

parser = argparse.ArgumentParser(description = 'Re-writes the annotations.jsonl file document splitting')
parser.add_argument('-d', help="the new document ID")
parser.add_argument('-o', help="the original document part UUID")
parser.add_argument('-n', help="the new document part UUID")
args = parser.parse_args()

docid = args.d
old_part = args.o
new_part = args.n 

with open('./original/annotations.jsonl', 'r') as infile, \
  open(f'./original/annotations.{new_part}.jsonl', 'w') as outfile:

  all_annotations = infile.readlines()
  print(f'Read {len(all_annotations)} annotations total')
  as_json = list(map(lambda str: json.loads(str), all_annotations))

  # Keep only annotations on the relevant part
  relevant_annotations = list(filter(lambda a: a['annotates']['filepart_id'] == old_part, as_json))
  print(f'Keeping {len(relevant_annotations)} for part {old_part}')

  for annotation in relevant_annotations:
    # Generate random annotation and version UUIDs
    annotation['annotation_id'] = str(uuid.uuid4())
    annotation['version_id'] = str(uuid.uuid4())

    # Rewrite doc and part ID
    annotation['annotates']['document_id'] = docid
    annotation['annotates']['filepart_id'] = new_part

    outfile.write(f'{json.dumps(annotation)}\n')

  print(f'Wrote results to ./original/annotations_{new_part}.jsonl')