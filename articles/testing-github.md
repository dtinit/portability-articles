---
datatype: Notes
title:  Transfering Evernote content anywhere
destinations: ["Bear", "OneNote", "Joplin", "Zoho", "Notion"]
sources: Evernote
---

# Evernote and Interoperability

Evernote does not appear to make any effort to allow you to port your data to or from other systems.
Its online help articles are unhelpful-to-wrong.  [This 
article](https://help.evernote.com/hc/en-us/articles/208314308-Import-content-from-other-apps-into-Evernote), 
for example, explains that you can import from other notes apps exports - but the only format that
the app seems to support is the custom ENEX format, or files ending in ".enex".  

Similarly, Evernote does not export into a format that is usable by other apps.  PCMag investigated this
at length and [reported on the difficulties](https://www.pcmag.com/picks/ditching-evernote-here-are-your-top-alternatives) 
of porting to OneNote, Joplin, Zoho, Bear, and Notion.  Several of these have features specifically for
importing from Evernote.

## Evernote to Bear

Moving notes to Bear from Evernote works in HTML format, though poorly - it loses images.  Better is to 
use Bear's feature in the File menu to "Import From" > "Evernote", and import ENEX files, which preserves images in the notes.
As the PCMag article accurately reported, Bear loses all the folder structure of Evernote's notes, because
Bear does not use folders.  A pretty workable approach may be to tag all your notes in Evernote before exporting:

* In the Evernote app, select all the notes in an folder
* From the right-mouse button menu (Context menu?) choose "Edit tags"
* Apply a tag to all of the items
* Export them all as one ENEX file
* Import into Bear using "Import From" > "Evernote"

As a result, the notes will preserve images and tags.
