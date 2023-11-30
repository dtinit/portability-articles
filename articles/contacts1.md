---
title:  iCloud Contacts to Export and Reimport
datatype: Contacts
sources: iCloud
destinations: ["Google Mail", "Office 365"]
---

# How to copy your Contacts from iCloud to other places using .VCF files and the VCARD standard

## First get an export

If you have contacts in iCloud (which you probably do if you've been using iOS devices or a Mac computer), 
you can export any number of selected contacts.  The instructions for how to select all and export them
can be found in this [Apple support 
article](https://support.apple.com/guide/icloud/import-export-and-print-contacts-mmfba748b2/icloud).  After
the export, you should have a file ending in ".vcf" that is a text format containing VCard items for each
contact you selected.

If your contacts are on a Mac computer but not synchronized to iCloud, you can still get to the point of 
having a VCF file containing interoperable VCard data.  From the Contact app on your Mac, multiselect 
individual contacts or create a list and sort into it the contacts you'd like to port.  Then when you have
the individual items selected, right-click them and choose "Export vCard".  This process will also create a 
.VCF file containing vCard items.

Note that if you follow the instructions to [create a "Contacts Archive"](https://support.apple.com/en-us/HT204055)
from your Contacts app, you will have a format that is
less portable (an .abbu file).  This may be useful as a backup or for copying from one Apple machine to 
another, but less useful for porting to another destination.

## Import somewhere else

A ".vcf" file (generated with either approach above that results in that file format and file extension)
can now be imported to a number of other systems.

 * To import to Google Contacts, first open Google Contacts in your Web Browser, choose Import on the left 
side menu, and use the "Select File" button to import each contact to Google. 

## What this solution can do

This solution is good for migrating one-time to another platform, or bring your data with you one-time
(e.g. when you need all your old iOS contacts available to your work email and your work uses Google or 
Microsoft mail.

## What this solution does not do

This solution is not good for re-importing.  If you try to re-import, it will simply create duplicates, and
that may create confusion about which contact is the more recent.  
