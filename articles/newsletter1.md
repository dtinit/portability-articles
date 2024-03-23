---
title: Moving Newsletter off Substack
datatype: Newsletter
sources: Substack
destinations: ["Beehiiv", "Buttondown", "Ghost", "WordPress", "Download myself"]
---

# Alternatives

[Beehiiv has a support article](https://support.beehiiv.com/hc/en-us/articles/14966988360215-How-to-migrate-from-Substack-to-beehiiv) 
explaining how to migrate a Substack newsletter to the Beehiiv platform.  The article explains multiple steps rather than an 
all-in-one tool, but that might be a good thing because use cases differ depending on whether a creator wishes to migrate
public newsletter articles or private ones, and free subscribers or premium. 

[Buttondown also supports](https://www.wired.com/story/how-to-migrate-newsletter-substack-to-buttondown/) importing data exported from 
Substack, and importing the entire ZIP file via upload to Buttondown.

[Ghost also builds off exports](https://ghost.org/docs/migration/substack/), and has command-line tools to complete what appears
to be complicated but well-supported migration process.  This includes comments.

[Wordpress supports](https://wordpress.com/support/import-from-substack/) the same approach via its Tools > Import > Substack
menu, importing subscribers as well as content.


## Download data

Substack's export/download tools allow newsletter owners to download in a readable format:

* subscriber lists
* posts
* "related statistics"

We assume (but did not verify) that this does include content files such as videos and podcast files.

## What this solution can do

Whether downloading for backup, uploading to Beehiiv or uplaoding to Buttondown, this solution involves working from Substack's
export formats and download.

This is a complete, although work-intensive and often manual, process for moving a newsletter and subscribers from Substack to Beehiiv.
It is even capable of moving paid subscribers -- using Stripe migration tools.

Migrating just free content into Beehiiv is a simpler more automated process so the length and complexity of the support article 
need not be offputting if the use case is simpler.



## What this solution does not do

Because this solution involves downloading Substack's exports, it relies on having storage space and finding and using the downloads.

We might not have complete information in this article about which other platforms import media files, comments and other
information besides the base HTML posts themselves.  Contributions here are welcome.

The documented Beehiiv solution does not migrate videos, podcast files, paywall placements, photo galleries, comments, and a few more things that can be found in the support article (kudos to Beehiiv for providing excellent detail on this).