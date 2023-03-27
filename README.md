# git: wut?

- I need to make changes to my code without fear of breaking it
- I need to collaborate with others on my code
- I need keep track of my code's history

## So what is Git?

Git means "global information tracker". It's a version control system that lets you manage and keep track of your source code history. Git is responsible for everything from small to very large projects with speed and efficiency.

## Version control systems

> A version control system is a tool that records changes to a file or set of files over time so that you can recall specific versions later. For the examples in this tutorial, you will use software source code as the files being version controlled, though in reality you can do this with nearly any type of file on a computer.

- Local
- Central
- Distributed

### Initializing a repository

This gets our repository set up to track changes. We can do this by running the following command:

    $ git init

### Adding files to the staging area

The staging area is where we can review changes before committing them to the repository. We can add files to the staging area by running the following commands:

```sh
    $ git add README.md
    $ git add calculator.py
    $ git add calculator_test.py
```
### Ignoring files

Sometimes we don't want to track certain files. For example, we might have a file that contains sensitive information, like a password or API key. We can tell Git to ignore these files by creating a file called `.gitignore` and adding the names of the files we want to ignore to it. For example, if we want to ignore all files with the `.pyc` extension, we can run the following commands:

    $ touch .gitignore
    $ echo "*.pyc" >> .gitignore

### Committing changes

To commit changes, we run the following command:

    $ git commit -m "Initial commit"

### Viewing the commit history

We can see the history by running the following command:

    $ git log

### Adding a remote

Typically you will want to add a remote repository so that you can push your changes to it and make it available to teammates. We can add a remote by running the following command:

    $ git remote add origin http://github.com/myktra/

### Pushing changes

Once a remote has been added, we can push our local branch to it by running the following command:

    $ git push -u origin main


## git in the real world

![image](assets/workflow.png)

### Branching

Branching is a way to work on different versions of a repository at one time. By default your repository has one branch named `main` which is considered to be the definitive branch. We use branches to experiment and make edits before committing them to `main`.

#### Creating a branch

To create a branch we use the `git branch` command. Let's create a new branch called `feature` by running the following command:

    $ git branch feature/subtract

#### Switching branches

To switch between branches, we use the `git checkout` command:

    $ git checkout feature/subtract

### Merging branches

Once we're done working on the feature, we can merge it back into `main` by running the following command:

    $ git merge feature/subtract
