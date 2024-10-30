### Requirements

```shell
# this command install all requirement in the file 'requirements.txt'
pip install -r requirements.txt

```

### Black

```shell
# this command list and format all files
black .

# OR

# this command list and format all files and shows what he changed in each file
black . --diff

# OR

# this command only check and list files that need to reformat
black . --check
```

### Flake8

After running the above commands, run following command, it will check all files on your project 
and shows errors based on [PEP8](https://peps.python.org/pep-0008/).
```shell
flake8 .
```