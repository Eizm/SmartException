# SmartException
An easy-to-use context manager for Python developers that catches errors and re-raises them after providing extra information

Examples are given directly inside the script. Executing it as-is prints

```console
[1, 2, 3]

Error trying to index the following variable
{'t': [1, 2, 3], 'r': [5, 7, 9]}
Which has the following keys
dict_keys(['t', 'r'])
Traceback (most recent call last):
  File "/data/user/0/ru.iiec.pydroid3/files/accomp_files/iiec_run/iiec_run.py", line 31, in <module>
    start(fakepyfile,mainpyfile)
  File "/data/user/0/ru.iiec.pydroid3/files/accomp_files/iiec_run/iiec_run.py", line 30, in start
    exec(open(mainpyfile).read(),  __main__.__dict__)
  File "<string>", line 67, in <module>
KeyError: 'k'

[Program finished]
```