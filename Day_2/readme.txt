Day 2: Git Commands
- git pull origin main
- git checkout my-test-branch
- git add .
- git commit -m "making a test branch for a demo" # Like taking a snapshot of your code at a given moment
- git push --set-upstream origin my-branch-name # Pushing this all upstream within a branch
- git merge my-test-branch # Main branch into the main project
- git checkout main # Go back to main before creating a new branch

Day 2: Common Git Error
- git pull origin main (the branch does not exist) -> Pull the sources from main 
- To initialise a main branch we need a README.md (we have to have this)
- git remote add origin (SSH Git URL)
- git add . (Shorthand for adding all files)
- git push origin
- git --help
- git branch --help (add the action for help on what it does)

- git stash stashes the changes
- git branch (new branch)
- git stash pop (pops all changes into new branch)

Day 2: Git Clone and Walkthrough
- Use the SSH tab
- git remote add origin SSH
- git clone (SSH) # Made a clone of the repository github but it is on your local machine
- git pull origin main #Always run to see if there are any new changes within the code
- words are connected with dashes -> branches enable you to work within your own bubble
- write the code and make some changes
- mv /d/dev/my_first_script.py /d/script.py -> can more to a new path
- git status -> make sure we are on the right branch
- -m "message signal"
- fixed, update -> try to avoid these
- git push origin branch-name