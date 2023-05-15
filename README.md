# bash.py

Self-contained Python file providing syntax sugar for invoking bash. 

There's a PIP module that serves the same purpose https://pypi.org/project/bash/ but this project is for case when you can't install custom PIP libraries.

## Setup

1-) Download this project or manually copy the files' content:


2-) Create a directory in your user directory:

```
cd ~/
mkdir -p lib/python/bash
```

3-) Add the `lib/python` directory to `PYTHONPATH` by adding this to your `.bashrc`:

```
export PYTHONPATH="~/lib/python/:$PATH"
```

4-) Run

```
source ~/.bashrc
```

5-) In any Python script

Import via

```python
from bash import bash
```
