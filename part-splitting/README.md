# Recogito Document Splitter

Documentation and utility functions for splitting anntotated Recogito documents.

__For the time being, this is for internal use only. There is very little automation.
Functionality may evolve later, if this functionality turns out to be needed more often.__

## Extract single part

1. Download the backup package for the document you want to split
2. Unzip the package contents into the `/original` folder
3. Manually edit the metadata
   - Remove all parts except the one you want to keep
   - Edit title and other metadata as needed
   - Assign a new ID for the document (for convenience, run `python uuidgen.py`)
   - Assign a new UUID for the remaining document part and rename the document part file
     (for convenience, run `python docidgen.py`)
4. The tricky part: rewiring the annotations
   - The `rewrite_annotations` utility will filter the original annotations.jsonl file, 
     so that only those for the relevant part are kept, and will rewrite all IDs (document,
     part, annotation, version) as needed
   - Run the utility like so: 
   
```
python rewrite_annotations -d {new doc ID} -o {old part UUID} -n {new part UUID}
```
