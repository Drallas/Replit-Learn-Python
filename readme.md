This is a collection of usefull Python Scripts, collected while learn how to code with Python..


To run function from programming_languages, it needs to be imported.

```python
import programming_languages
```

But it's also possible to edit the (hidden) .replit file and change the ```entrypoint = "main.py"``` value to something else!

To make shure it runs after an import from Github add this to the .replit file.
```bash
entrypoint = "main.py"
modules = ["python-3.11"]

[nix]
channel = "stable-24_05"

[unitTest]
language = "python3"

[gitHubImport]
requiredFiles = [".replit", "replit.nix"]

[deployment]
run = ["python3", "main.py"]
deploymentTarget = "cloudrun"
```