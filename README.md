# CS 1110 projects

This repository contains two Python course assignments: a currency exchange program and a color-model application. The files are organized by assignment and are intended to be run from their own directories.

## Currency project

`currencyproject/` parses responses from an online currency service and provides a small command-line interface. It depends on the course's `introcs` package and network access to the service.

From the assignment directory, run the provided tests or start the interactive app:

```sh
cd currencyproject
python3 a1test.py
python3 a1app.py
```

The app prompts for source currency, destination currency, and amount. Exchange rates come from the remote service and can change; the program is a course exercise, not financial advice or a guaranteed transaction quote. Follow the course environment instructions for installing `introcs`.

## Color module

`colormodule/` implements color conversion and formatting functions, with a Kivy interface defined by `a3app.py` and `a3view.kv`. Run the assignment tests with `python3 a3test.py` from that directory. To open the interface, use `python3 a3app.py`; it requires Kivy and the course's `introcs` package. Keep the `.kv` layout file beside the application code.

## Repository notes

The `a1test.py` and `a3test.py` files are assignment tests. Feedback text files record course feedback and are retained with the submitted work. The original assignment handouts and all environment setup instructions are not included here, so use the course materials for exact specifications and dependency setup.
