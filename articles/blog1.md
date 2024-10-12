---
title: Moving a blog from WordPress to Ghost
datatype: Blog
sources: WordPress
destinations: ["Ghost"]
---

# Using Ghost's WordPress plugin

Ghost has an advanced approach to [migrating to Ghost from WordPress](https://ghost.org/docs/migration/wordpress/), and have written a plugin
to make this happen smoothly.  It still requires exporting data to a computer and re-uploading it, but Ghost's plugin helps access and format the data for a better transfer.


## What this solution does not do

According to Ghost's guide, "Keep in mind that a migration from WordPress will not include custom fields, metadata, shortcodes, custom post types & taxonomies, or binary files. Just posts, pages, text, and images."

Also note that the user must fix URLs manually.