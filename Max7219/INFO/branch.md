To start a new branch in GitHub, switch to it, and push your changes, follow these steps:

### 1\. **Create a New Branch Locally**

First, make sure you're on the correct repository and have the latest changes:

```bash
git pull
```
Now, create a new branch and switch to it:

```bash
git checkout -b <new-branch-name>
```
### 2\. **Make Changes**

Now that you're on the new branch, make any necessary changes to your files.

### 3\. **Stage and Commit Your Changes**

Once you've made the changes, stage and commit them:

```bash
git add .
git commit -m "Description of your changes"
```
### 4\. **Push the New Branch to GitHub**

Push your new branch to the remote repository on GitHub:

```bash
git push -u origin <new-branch-name>
```

The `-u` flag sets the upstream branch, which makes future `git push` commands simpler, as Git will remember which remote branch you're pushing to.

### 5\. **Switching Between Branches**

If you want to switch back to another branch (e.g., `main` or `master`), you can use:

```bash
git checkout <branch-name>
```
That's it! You have created a new branch, committed changes, and pushed it to GitHub.