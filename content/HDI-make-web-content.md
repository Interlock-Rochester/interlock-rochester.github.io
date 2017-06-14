Create Web Content
=============

date
:   2017-06-13 20:15

author
:   Carl

category
:   Uncategorized

slug
:   web-content

status
:   un-published

This is the HDI class for June. We will figure out how to make 
a posting to the Interlock Website. So following Joe's instructions
posted to IRC today we are going to this.

First I cloned the website git repository.

git clone https://github.com/Interlock-Rochester/interlock-rochester.github.io.src

Then I started editing this file in the markdown directory. The file
is called HDI-make-web-content.md

I followed the format of an existing file to get all the content
headers correct. Now I am filling in the rest of the page.


[![blank
canvas](http://www.interlockroc.org/wp-content/uploads/2013/12/100_2677-300x225.jpg)](http://www.interlockroc.org/wp-content/uploads/2013/12/100_2677.jpg)

Here are some of Joe's instructions:

12:35 <+dzho> lemme see if I can run through a short version here just to 
              limber up:
12:36 <+dzho> git clone 
https://github.com/Interlock-Rochester/interlock-rochester.github.io.src
12:36 <+dzho> cd interlock-rochester.github.io.src
12:36 <+dzho> vi content/my-new-post.md
12:36 <+dzho> (write your post in markdown, make sure to have a Title: and a 
              Date: line at the top)
12:37 <+dzho> git add content/my-new-post.md
12:37 <+dzho> git commit -m "my new post, y'all"
12:37 <+dzho> hmm, I skipped a step there if we want to use the github pull 
              request model.
12:37 <+dzho> fork 
https://github.com/Interlock-Rochester/interlock-rochester.github.io.src
12:38 <+dzho> git clone 
              https://github.com/$YOURGITHUBID/interlock-rochester.github.io.src
12:38 <+dzho> proceed as above
12:38 <+dzho> git push
12:38 <+dzho> then generate a pull request against the repo
12:38 <+dzho> then magic happens
12:39 <+dzho> (eg, manual intervention on my part to build the thing with 
              pelican and copy it to the linode)
12:40 <+dzho> (to set up that part, virtualenv ~/pelican-venv; . 
              ~/pelican-venv/bin/activate ; pip install pelican ; )
12:42 <+dzho> then, within interlock-rochester.github.io.src: pelican content
12:43 <+dzho> that will build the site and put the results in the output dir, 
              which is parallel to the content dir, underneath the 
              interlock-rochester.github.io.src dir
12:43 <+dzho> I've been rsync'ing output up to ~djoe on the vm, and then from 
              there into the web server directory.
12:44 <+dzho> (the first step, from the outside, requires only sending files 
              into the VM from an unprivileged account, the second requires 
              privileges sufficient to write to the web directory. I keep them 
              separate as a precaution.)
12:44 <+dzho> I think that captures the general flow of things, off the top of 
              my head with only a little reference to various of the stuff 
              involved.)
 
Now I am going to try putting this into the git repo. Then if successfull
I will then attempt to make updates to the frontpage so you can find this.


