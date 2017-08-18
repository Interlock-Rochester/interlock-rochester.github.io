
# Reporting problems

Please consider [opening an issue](https://github.com/Interlock-Rochester/interlock-rochester.github.io.src/issues)
for any question you have or bug you might notice in the web page before
attempting anything below.

Interlock members might also wish to raise concerns on the
interlock-rochester Google Group.

# Background

The following is just a rough guide.  It will help a great deal if you have
some experience editing text configuration files as well as using git,
GitHub, and python virtual environments.

The [Pelican static website generator](https://blog.getpelican.com/) is what
we use. It is [extensively documented](http://docs.getpelican.com/en/stable/).

A great deal of our content was converted automatically from WordPress into
Pelican-flavored [reStructuredText](http://docutils.sourceforge.net/rst.html) format files, and then hand-corrected.

Most content created or modified after that has been in [Markdown](https://en.wikipedia.org/wiki/Markdown).



# Clone the repository in github

If you don't have a github account, create one.

Navigate to

    https://github.com/Interlock-Rochester/interlock-rochester.github.io.src

click the **fork** button.  


# Computer Setup:

```
sudo apt install pelican
```

__Note: This may give you and old, incompatible version of Pelican__

Alternately, issue

```
pip install pelican
```
possibly in a [virtual Python environment](http://docs.python-guide.org/en/latest/dev/virtualenvs/) created with the 

```
virtualenv
``` 

command.  

If using a virtual environment, be sure it is active before installing or
trying to use pelican.



# get the repos

```
mkdir interlock_website

cd interlock_website

git clone git@github.com:your-github-username/interlock-rochester.github.io.src.git

cd interlock-rochester.github.io.src

```

Be sure to substitute your own github account name in place of
**your-github-username**

# Edit the site

You can change or create files as either reStructuredText (.rst) or Markdown
(.md) but these files need to be somewhere within the ```content```
directory. 

# Test your changes by running Pelican

Start Development version of site

```
./develop_server.sh start
```

Repeat the edit-test process as often as necessary to get the result you
seek.

# Push your changes to your fork at github

git add [list of changed files]

git commit

git push

(You may wish to develop on a separate branch from **master** but how to do
that is beyond the scope of this README.)


# Make a pull request to submit your changes to the public site

Navigate to your fork of the src repository, eg

    https://github.com/your-github-username/interlock-rochester.github.io.src

Click the **New pull request** button near the upper-left above the file
listing.

Click the green **Create pull request** button to submit it.

After changes have been submitted, they will be reviewed and, if
appropriate, merged and a new copy of the site built and uploaded.

