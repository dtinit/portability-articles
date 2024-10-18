---
title: Exporting and browsing your X's interaction activity
datatype: Likes & Favorites
sources: X
destinations: Download myself
---

# X’s “Download an archive of your data” for posts you’ve interacted with

X offers a very well documented and reasonably fast process to export your data from the service.

It is necessary to highlight that the export of data for users is intended so that they can verify and analyze all the information corresponding to them. Due to logical circumstances, it is not possible to export X's information to another service that belongs to the social network category directly (as happens with other applications with a different purpose of use such as taking notes apps).

This [official X article](https://help.x.com/en/managing-your-account/accessing-your-x-data) provides information on how to carry out the process on the various platforms and the type of information relevant to the user that will be downloaded. Among the most notable information we can observe the following:

- Username, email address, phone numbers, numbers associated with your account, etc.
- Account history such as your logging history, as well as the places you’ve been while using X.
- Apps connected to your X account and browsers and mobile devices associated to it as well.
- Account activity (such as your posts, repost, likes), and your interests and Ads data.

<aside>
💡 It should be noted that according to the article attached above, when the user deactivates their account and there is no activity in it for 30 days, the account and the information pertinent to that user is completely deleted. So if you plan to deactivate your account, we suggest that you first carry out the process of exporting your data.

</aside>

To start the process we go to our **profile** (by tapping on our profile icon) if we are on a mobile device. When we are on the website, we tap or click on the **More** section in the main navigation menu located at the bottom left of the timeline.

Once the previous step is completed, the remaining steps of the process are similar regardless of the device and operating system in use. The next thing is to enter the **Settings and privacy** section. Later we go to Your Account and here we will have an option called **Download an archive of your data**, which we will click or tap.

Subsequently, it is necessary to wait for X to finish exporting the information of the user who requested the download. According to my own experience, this process ends in a couple of days, which is fast taking into account my own experiences with other social media services.

## Download formats in .zip file

Once the process of downloading the information by X is completed, in the same section Download an archive of your data, we will be shown the option to download a **.zip file**. It is worth mentioning that it is the only format in which X allows downloading.

## Files inside .zip file

When unzipping the .zip file we will find two folders (**assets** and **data**) and a **Your archive.html** file.

The html file allows us to see a general breakdown of our activity such as the number of posts, likes, blocked accounts and muted accounts, among others. Likewise, we can enter each of these sections and we can verify our information with a graphical interface quite similar to the one that appears in the X timeline and that allows the user some comfort.

If we want to know our information in more detail, we can enter the **data** folder that was created after decompressing the .zip file or in the **Open this folder** option in the previously mentioned Your archive.html file.

In this folder we have a very wide and diverse amount of information. Most of these files are in a JavaScript format, therefore they have the `.js` extension.

Each of these files is named based on its content. In the `tweets.js` file all our posts are found in an array of objects. This format is found in each of the existing `.js` files.

In the `data` folder, we can also see that there are folders that include `_media` in the name. These show us the multimedia files that accompany our posts and also our profile and cover photo, among others.

# What this solution can do

This solution allows the user to directly download from X a history of the user's own information and corresponding activity.

# What this solution does not do

This solution does not allow the user to migrate the corresponding information to another social network service due to the various ways in which they operate. It also does not allow you to select the format in which the backup will be downloaded or export it to a cloud storage service. It will be stored directly to the device on which the `.zip file` is downloaded.