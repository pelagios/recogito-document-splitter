# A utility to re-write the annotations.jsonl file for splitting documents.
# Takes the following input arguments
# -d the new document ID
# -o the old document part UUID
# -n the new document part UUID
import argparse
import json
import uuid
import random
import string

parser = argparse.ArgumentParser(description = 'Re-writes the metadata.json file document splitting')
parser.add_argument('-k', help="the part ID to keep")
args = parser.parse_args()

new_docid = ''.join(random.choices(string.ascii_lowercase + string.digits, k = 14))
old_partid = args.k
new_partid = str(uuid.uuid4())

with open('./original/metadata.json', 'r') as infile, \
  open(f'./original/metadata.{new_partid}.json', 'w') as outfile:

  meta = json.loads(infile.read())

  # Generate a new random doc ID
  meta['id'] = new_docid

  # Filter parts
  meta['parts'] = list(filter(lambda p: p['id'] == old_partid, meta['parts']))

  # Replace part ID and filename
  meta['parts'][0]['id'] = new_partid
  meta['parts'][0]['file'] = f'{new_partid}.xml'
  
  outfile.write(f'{json.dumps(meta, indent=2)}')

  print(f'Wrote results to ./original/metadata.{new_partid}.json')
  print(f'Original part UUID to keep: {old_partid}')
  print(f'New doc ID: {new_docid}')
  print(f'New part ID: {new_partid}')

  print()
  print('Rename file with:')
  print(f'mv ./original/parts/{old_partid}.xml ./original/parts/{new_partid}.xml')

  print()
  print('Rewrite annotations with:')
  print(f'python rewrite_annotations.py -d {new_docid} -o {args.k} -n {new_partid}')