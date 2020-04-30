#!/bin/bash
# Look for folders under ~/ that have a .git folder in them. Show them as options.
leaf_dir=$(find ~/ -maxdepth 4 -type d -name .git | xargs dirname | xargs basename -a | dmenu)

# If the variable is empty b/c I hit escape, do nothing
[ -z "$leaf_dir" ] && exit

# Find the absolute path to that directory. At this point I am assuming there isn't
# some naming degeneracy in my folder structure. That can be dealth with later as a
# corner case
abs_dir=$(find ~/ -maxdepth 3 -type d -name $leaf_dir)

# Launch vscode and open that folder
code -n $abs_dir

