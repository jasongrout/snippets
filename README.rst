Snippets
========

This website aims to provide a version controlled snippet database.

See the TODO.txt file for a list of things to do.

To Run
======

This project requires Mercurial to be installed (that is what the repositories use).  It also requires Flask to be installed.  To run, simply do::

    python webserver.py

Then open your browser to the indicated URL.  There, you can create a new snippet (repository), list the currently created repositories, and create new versions of snippets in the repositories.  If you edit a version of a snippet that is not the tip (HEAD) version, it forks the snippet and branches at that commit.  The UI doesn't show this very well at this point, though.

Design Goals
============
Goal: Design an online library of interacts and other snippets of Sage code.  This library should allow:
  * syntax-highlighting of snippets of code
  * multiple files in a snippet
  * logged-in users to upload or "fork" other people's snippets
  * anyone to run a single-cell in the same directory as the files in the snippet (you can import things from the snippets)
  * if the snippet is just a single file, anyone to run a single-cell after the contents of the file have been executed (this means that if no command is specified, it's as if I've typed the snippet into the command line)
  * live interacts (available after the person has pressed "Run")
  * tags on snippets, along with autocomplete on tags, etc.
  * Comments on snippets or line-level comments (ala google code reviews or github commit comments)
  * searching full-text or tags
  * hierarchical browsing of tags/filtering system
  * thumbnail screenshots maybe?
  * some sort of rating system
  * place for short blurb and title of the snippet
  * links to relevant other snippets and tags
  * Credit lines for primary author, contributors, and committers
  * permalink to snippet
  * link to view snippet as raw text, download snippet (zip if multiple files)
  * community rating system
  * "like this/email" links to various online sites (facebook, twitter, etc.)
  * ability to view the entire commit tree of the snippet and related forks.  Ability to see from any snippet the recent activity on another branch.  Hmmm...but we don't want to just reimplement gitorious/bitbucket/github here; that's too big of a project
