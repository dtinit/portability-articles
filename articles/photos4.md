---
title:  Exporting photos from Flickr
datatype: Photos
sources: Flickr
destinations: ["local backup"]
---

# Export photos from Flickr

## "Request My Flickr Data" download

The official supported way to get your photos from Flickr is using their "Request My Flickr Data" button
on your [flickr account page](https://flickr.com/account).  This button will not get you your data immediately,
but will eventually guide you to download a file containing all of your photos and much other Flickr account
data too:
* Comments on your photos
* Your full descriptions
* Number of 'faves' and 'views' for each photo
* License
* Tags
* Date originally imported to Flickr

The download also includes "Flickrmail" sent and received, testimonials, and comments on sets among other data.
All the data other than the photo files is in JSON files (at least one JSON file per photo plus the others 
miscellaneous files.  

At this point you technically have all your data but it is hard to do anything with.  At least you have a
local backup.

## Moving photos elsewhere

There's an [article by TechAdvisor](https://www.techadvisor.com/article/728495/how-to-move-photos-from-flickr.html) 
that's still pretty accurate about the pros and cons of some other services, and it does describe
how to get your photos elsewhere but it involves the download-to-local process described above.

## What this solution can do

This solution gets all your photos, photo metadata and account metadata into your own hands on your own
device.  The metadata is in a Flickr-specific format in JSON files.

## What this solution does not do

This solution is a complete backup but not a great move solution.
* It does not move your photos directly to another photo hostings service 
* It does not allow you to easily move any photo metadata. Descriptions, tags, sets and dates will all be lost.
