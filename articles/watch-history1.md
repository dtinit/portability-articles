---
title:  Transferring your Instagram post/video viewing history elsewhere 
datatype: "Viewing History"
sources: Instagram
destinations: ["Download myself", "Google Drive", "Dropbox"], 
---

# Instagram "Download your information" for posts/videos you've viewed

Instagram offers reasonably fast access to your data via your Profile page.  It’s a substantial package of information, available for download or transfer either in HTML or JSON format. 

Follow these links:

* A “More” link on the bottom left of the Instagram Web interface 
* leads to a “Settings” link 
* Settings includes a link to “Accounts Center”. 
* Accounts Center page has a link to “Your information and permissions”
* This page has a link to “Download your information”
* The popup has a button for “Download or transfer information”
* Select your account
* Select "All available information"
* Select "Download to device" or "Transfer to destination"

## Downloading your own data

The option to "download to device" is followed by options for date range, data format and media quality. The HTML data format option provides static pages that are easier for most people to navigate - just open the file in a Web browser after it's downloaded. 

After finalizing the data request, the process to bundle up your data happens asynchronously. Instagram sends an email with a link back to “Download your information” and the Download link. The Download link provides a ZIP file that your operating system is likely to be able to easily open, showing quite a few directories of files.

A few notes on what is and isn’t available:

* Includes a list of links for Web sites you’ve visited from within an Instagram app.
* Includes recent searches, contacts, followers, following, 
* Includes a list of ads you’ve seen but only author and date (no link to ad information)
* Includes lists of posts viewed, and videos viewed (but no links to posts/videos).  Note that this is filed under the folders ads_information/ads_and_topics.

The files for posts viewed and videos watched provide only author and timestamp.  As far as we can tell, the timestamp associated a post or video you’ve viewed is the _time of viewing_.  This, combined with the author of the post or video, does not provide a way to reconstruct WHICH of tht author's posts or videos you watched. 

Note that the he file containing of liked posts DOES include links to those posts - filed in the folder “your_instagram_activity”.

The availability of the download is pretty quick, depending on how much data is on your account and how much you request.  In our tests we received emails in a couple minutes.

The JSON downloads appear to have all the same data (which means this also doesn’t have links to Instagram posts or videos  you’ve viewed, only the author and timestamp) but it does have the data in a machine readable format which may be useful for some projects.

## Transferring - cloud backup

In addition to providing a way to download this information, Instagram also offers a way to transfer the same information (in ZIP file format) to Google Drive or Dropbox.  These sites may be useful locations to get at part of this information without downloading it all to your own device, or providing a backup of certain important account information.  

The information transferred to a cloud location will not be publically available at that location, unless you’ve configured that drive or cloud storage to be publicly visible. 

## What it does not do? 

Instagram “Download your information” does not provide access to URLs of posts or videos you have viewed.

The transfer options are effective for copying your account information to a static location in the cloud that acts like a backup or a simple file storage.  That is to say, the transfer options provided by Instagram do not allow you to move  your Instagram posts, followers or other material contents of your account to another social media service where those posts will be served.  
