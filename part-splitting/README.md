# Recogito Document Splitter

Documentation and utility functions for splitting anntotated Recogito documents.

__For the time being, this is for internal use only. There is very little automation.
Functionality may evolve later, if this functionality turns out to be needed more often.__

## Extract single part

1. Download the backup package for the document you want to split
2. Unzip the package contents into the `/original` folder
3. Rewrite the metadata
   - Open `metadata.json` and copy the UUID of the part you want to keep
   - Run `python rewrite_metadata.py -k {uuid}`
   - A modified copy of the metadata file will be stored as `metadata.{uuid}.json`
4. Rename the part file. The script will have re-assigned the ID for the part.
   For convenience, the renaming command will be output to the log. Copy-and-paste
   the command and run it.
4. Rewire the annotations
   - The `rewrite_annotations` utility will filter the original annotations.jsonl file, 
     so that only those for the relevant part are kept, and will rewrite all IDs (document,
     part, annotation, version) as needed
   - For convenience, the rewrite command will be output to the log. Again, copy-and-paste
     and run. 
   - For information: the syntax of the utility is like this: 
   
```
python rewrite_annotations -d {new doc ID} -o {old part UUID} -n {new part UUID}
```


