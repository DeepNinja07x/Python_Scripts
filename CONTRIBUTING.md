# Contribution
 If this is your first time to open source contribution and you know only python, then you have arrived at the right repository. 

 # How to contribute!

## Steps:
-  I would suggest you to create an issue for the development you want to make in the project. Though it isn't mandatory.
  
-  Fork this [repository](https://github.com/DeepNinja07x/Python_Scripts)
  
-  Clone the forked https://github.com/<Your_Username>/PyScripts
    > git clone https://github.com/<Your_Username>/Python_Scripts.git

-  Create new branch 
    > git checkout -b <Your_Branch_Name>

-  Add Scripts related to your respective issues.
    > git add <Your_Contribution>
 
-  Add a commit message !
    > git commit -a -m "<Your_Message>
    
-  Push changes
    > git push -u origin <Name_Of_Your_Branch>
 
-  Create pull requests
[Try to Mention the related issue for your PR] 
<br/>
// After Contributing add your name and GitHub handle at Contributors.md

# How to Sync the Repo!

## Steps: 
- When you see your repo is behind from the main project's repo in terms of commits. Just sync your repo with the main project's repo.

    > git remote -v

- Add the upstream (main project's) repo's URL

    > git remote add upstream https://github.com/DeepNinja07x/Python_Scripts.git

- Now fetch all the new commits from upstream to your local repo.

    > git fetch upstream

- Just check if you are in master branch before merging. If not just change your branch to master branch

    > git checkout master

- Merge the upstream branch with your master branch

    > git merge upstream/master

- push those changes to your GitHub repository

    > git push origin master
