# Recogito Document Splitter

Documentation and utility functions for splitting anntotated Recogito documents.

This project contains to sub-folders:

## part-splitting

Helper code to split one multipart-document into multiple documents, having one part each.
Handles generation of new document- and document-part IDs, as well as re-writing of data.

## intra-tei-splitting

Helper code to split an annotated single-part TEI document into a document that contains 
multiple TEI files. Handles generation of IDs, re-writing of annotations, as well as 
splitting of the TEI DOM.

__For the time being, this is for internal use only. There is very little automation.
Functionality may evolve later, if this functionality turns out to be needed more often.__
