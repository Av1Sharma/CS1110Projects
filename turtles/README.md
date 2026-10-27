# A4: Turtles

`a4.py` implements every drawing task, including all three radial shapes and
both recursive filled fractals. `a4test.py` is the unchanged official test script.
`a4verify.py` adds checks for invalid inputs, geometry, dash patterns, recursive
shape counts, and turtle state restoration.

Run from this folder with the project environment:

```sh
.venv/bin/python a4test.py
.venv/bin/python a4verify.py
```

For the official interactive tests, enter speed `0` for instant drawing, then
press Return between pictures. The tests open an IntroCS graphics window.

The local environment uses the existing system IntroCS and NumPy packages with
a compatible ARM Pillow installed locally. It avoids the architecture mismatch
in the system Pillow installation. To recreate it on this machine:

```sh
python3 -m venv --system-site-packages .venv
.venv/bin/python -m pip install --ignore-installed Pillow
```

On another machine, follow the course's IntroCS installation instructions.

The assignment requests only `a4.py` for the CMS upload, due October 29, 2026.
The personal CMS survey must also be completed. No upload or survey response
has been made by this project setup.
