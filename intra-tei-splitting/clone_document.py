# Creates a valid 'clone' of the document by rewriting document-, part-, annotation- and version IDs.
import json
import uuid
import random
import string

new_docid = ''.join(random.choices(string.ascii_lowercase + string.digits, k = 14))
new_partid = str(uuid.uuid4())

with open('./original/metadata.json', 'r') as infile, \
  open(f'./original/metadata.{new_partid}.json', 'w') as outfile:

  meta = json.loads(infile.read())

  old_part_id = meta['parts'][0]['id']

  # Generate a new random doc ID
  meta['id'] = new_docid

  # TODO Generate a new part ID

  # TODO write cloned meta file

  # TODO rename/copy part file

  # TODO rewrite annotations

