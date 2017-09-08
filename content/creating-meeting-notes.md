Title: Creating Meeting Notes
Author: jnwatts
Category: Tasks
Date: 2017-09-07
Status: published

To create meeting notes, create a new file in the content folder with the filename "YYYY-MM-DD.md" and use the following template:

```
Title: YYYY-MM-DD
Date: YYYY-MM-DD
Author: YOURUSERNAME
Category: meeting_notes

During this meeting...
```

When you're done, commit the new file and push to the repository:

```
git commit content/YYYY-MM-DD.md -m "Meeting notes from YYYY-MM-DD"
git push origin
```