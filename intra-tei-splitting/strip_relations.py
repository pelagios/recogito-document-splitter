import json

with open('./original/annotations.jsonl', 'r') as infile, \
  open(f'./original/annotations-no-relations.jsonl', 'w') as outfile:

  annotations = infile.readlines()
  as_json = list(map(lambda str: json.loads(str), annotations))

  for annotation in as_json:
    if 'relations' in annotation:
      del annotation['relations']

    outfile.write(f'{json.dumps(annotation)}\n')

  print(f'Processed {len(as_json)} annotations')