# Interlock Rochester Website Source

## Overview
This is the source branch of the content hosted on https://www.interlockroc.org. If you're interest in contributing to the
site's content as a blog post or making a fix instructions are below. This site is hosted on Github Pages with the help of
CloudFlare for HTTPS. You can contribute to the site by sending us a pull request. 

## Reporting problems

Please consider [opening an issue](https://github.com/Interlock-Rochester/interlock-rochester.github.io/issues)
for any question you have or bug you might notice in the web page before
attempting anything below.

Interlock members might also wish to raise concerns on the
interlock-rochester Google Group or drop in on the [#Interlock](https://webchat.freenode.net/#interlock) channel 
on Freenode. 

# Contributing

The following is just a rough guide.  It will help a great deal if you have
some experience editing text configuration files as well as using git,
GitHub, and python virtual environments.

The [Pelican static website generator](https://blog.getpelican.com/) is what
we use. It is [extensively documented](http://docs.getpelican.com/en/stable/).

## Quick Setup
* Clone the repo locally
* Install pelican and requirements
* Switch to the `src` branch
* Make additions as you want
* Preview your changes using `./develop_server.sh start` and review http://localhost:8000
* Submit a pull request of your changes when you're ready
* Nag one someone with access to accept your pull request either in person or electronically

## Setup

### Fork the git repo

If you don't have a github account, create one.

Navigate to

    https://github.com/Interlock-Rochester/interlock-rochester.github.io

click the **fork** button.  


### Computer Setup:

Setup a [virtual Python environment](http://docs.python-guide.org/en/latest/dev/virtualenvs/) created with the following command:
```bash
virtualenv
pip install pelican
```
*NOTE: Being a virtual environment, be sure it is active before installing or
trying to use pelican.* 

### Clone the repo
Clone your fork of your repo: 

```
git clone git@github.com:your-github-username/interlock-rochester.github.io.src.git
```

*NOTE: Be sure to substitute your own github account name in place of
**your-github-username***

### Edit the site

Edit the site as you want. The following instructions will give you an example of making a new blog post

Create a new file in the /content directory in format of `YYYY-MM-DD-TITLE.md` changing the name as necessary. Use the template below as a starting point: 

```markdown
Title: Project update
Date: 1982-12-01 10:20
Modified: 1984-12-05 19:30
Category: Projects
Tags: hacking, electronics
Slug: descriptive-title-for-inside-the-url
Authors: Joanna Rutkowska
Summary: Short description of what this blog post is about that shows up in search indexes. Be two sentences at the most. 

Today, someone new learned how to contribute to the Interlock website and it is me!
```

*NOTE: FOr more information on how to add images and other types of content [see the Pelican Content page](http://docs.getpelican.com/en/3.6.3/content.html) for more information.*

### Test your changes by running Pelican

Start Development version of site on your machine:

```
./develop_server.sh start
```

View your development version in your web browser at:

    http://localhost:8000


Repeat the edit-test process as often as necessary to get the result you
seek.

The development server will continue to run in the background, incorporating
changes, until you stop it:

```
./develop_server.sh stop
```

### Push your changes to your fork at github

Once you're satisfied with your changes and the test out OK:

```
git add [list of changed files]

git commit -am ["a description of your commit"]

git push
```

*NOTE: For those with permision to push to the main repo, you should be using the `make publish github` which will 
build the HTML and automatically push it to the `master` branch which is where the HTML is served.*

### Make a pull request to submit your changes to the public site

* vigate to your fork of the src repository, eg

    https://github.com/your-github-username/interlock-rochester.github.io

* Click the **New pull request** button near the upper-left above the file
listing.
* Click the green **Create pull request** button to submit it.

After changes have been submitted, they will be reviewed and, if
appropriate, merged and a new copy of the site built and uploaded.

