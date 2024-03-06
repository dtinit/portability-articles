---
title: Transfering and exporting Todoist tasks
datatype: Tasks
sources: Todoist
destinations: ["Google Sheet", "Things", "Download myself"]
---

# Todoist and Interoperability

Todoist is lacking in the options available for exporting user data. The service does not allow exports in formats usable for other services and officially simply gives the only option of exporting data to Google Sheets.

There are some third-party open source solutions that allow user information to be exported in JSON and CVS formats, but eventually, the information in these formats does not allow import compatibility in other similar services.

## Todoist to Things

Some services, such as Things, allow the user to migrate their information from Todoist using the [Todoist public API](https://developer.todoist.com/sync/v9/#get-all-projects), but it can result in a complicated and tedious process for the user because queries must be performed to obtain the information requested.

## Download data for myself
This [third-party open source](https://darekkay.com/todoist-export/) tool allows the user to backup Todoist data as CSV or JSON. Both formats are available but it is recommended to download the information in CSV (Comma Separated Values) due to its ease of reading both for the user downloading and for carrying out the import process in other services.

**In order to export your data you need to sign in to your Todoist account via the service itself.**

* Once you select the format in which you want your data to be exported, you need to authorize and sign in with your Todoist account in order for the tool to begin the backup process.

Having your data in these formats might be useful when trying to import to other tasks services.

## Todoist to Google Sheet

This [official extension](https://todoist.com/help/articles/use-the-export-to-google-sheets-extension-with-todoist-A0r79pnM5) allow the user to export the data they want but also collaborate and document work in progress. We'll be able to export and share active and completed tasks and its information (date, description, priority).

* To activate it, first we need to log in in our Todoist account using the desktop version of it.
* In settings, we click the Integrations menu and we'll see the Integrations settings and select Export to Google Sheets.
* If this is the first time running this extension, you'll be asked to sign in to your Google account.


## What this solution can do

These solutions allow the user to find the appropriate ways to export their data given the complexity that Todoist provides in this section.

## What this solution does not do

These solutions do not describe ways to migrate to other task services with equal or greater popularity (TickTick, for example) due to the obstacles placed by Todoist when exporting the information. This process must be done manually.
