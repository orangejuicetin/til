# Git

America runs on Dunkin, the tech runs on git

- If you want to revert to the commit before c5f567, append ~1 (where 1 is the
  number of commits you want to go back, it can be anything):

  `git checkout c5f567~1 -- file1/to/restore`

  This is super helpful for when you have a file from a prior commit where you
  want to revert the work that you did on it, but don't want to revert that
  _entire_ commit.
