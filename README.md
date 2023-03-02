# Codes Only


### How to create new branch without using any other branch?

```bash
cd repository
git checkout --orphan orphan_name
git rm -rf .
rm '.gitignore'
echo "#Title of Readme" > README.md
git add README.md
git commit -a -m "Initial Commit"
git push origin orphan_name
```
