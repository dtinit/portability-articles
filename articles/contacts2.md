---
title:  Google Contacts export and import
datatype: Contacts
sources: Google Contacts
destinations: ["Apple Contacts"]
---

# Google Contacts - VCard (VCF) for import to Apple/iCloud Contacts

## How to Export and edit

The documented way to export contacts from Google Contacts for importing to iOS
is well-described in this [simple Google article](https://support.google.com/contacts/answer/7199294).
It will walk you through selecting contacts on a Web page to choosing an appropriate
export format.  The one to pick if you're moving contacts to an iOS device is 
the VCF file format which contains VCard data.

## Importing to MacOS and iCloud

Once your VCF file is ready, there are a number of options to transfer them somewhere else.
 * To add them to your MacOS Contacts app, you can just open the file, it should default to
opening in Contacts.app and prompt you to add them.  You'll be prompted to review duplicates and
the app will _update_ duplicate Contacts rather than actually create duplicates.

If you want to instead add these to an iCloud account and you don't have MacOS (for example, 
you wish to make these contacts available on an iPhone without connecting your iPhone to the Google 
account that had those contacts), you can also upload the VCF file to iCloud.  From
your [iCloud Contacts](https://www.icloud.com/contacts/) page, while logged into the iCloud account, 
use the "+" button and choose to "Import Contact".  You can then upload the VCF file that google created.
This import approach will _create duplicate_ contacts in your contacts account, so if you think
you may have duplicates and you do have the MacOS Contacts.app, that approach is preferable.

## What this solution can do

Any time you find that you've got addresses available on Google Mail but they're not available
in your MacOS Contacts, the Google export --> open with Contacts.app process is quick and won't 
flood your contacts db with duplicates. 

The VCF file with VCARD entries is a widely-accepted Internet Standard, so it may also be 
appropriate for importing into other destinations.

