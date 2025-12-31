# textual-jsx: Textual 💚 JSX

Enable JSX syntax support for [Textual](https://textual.textualize.io/) applications.

Write your Textual UI with familiar JSX-like syntax instead of nested Python calls.

## Installation

```bash
uv pip install git+https://github.com/frostming/textual-jsx.git
# Or
pip install git+https://github.com/frostming/textual-jsx.git
```

**Requirements:** Python 3.12+

## Usage Guide

- Name the python file with JSX syntax with `.px` extension or add `# coding: jsx` at the top of the file.
- Add `from textual_jsx import jsx` in every `.px` file that uses JSX syntax.
- Add `import pyjsx.auto_setup` at the entry point of your application to enable automatic transpilation of `.px` files.

See the [example counter app](./counter.px) and [main.py](./main.py).

Run the example app:

```bash
cd examples && uv run main.py
```

Refer to the [pyjsx](https://github.com/tomasr8/pyjsx) project for more details about the JSX syntax and how to add support for VSCode and

## Credits

- [Textual](https://textual.textualize.io/) - TUI framework for Python
- [PyJSX](https://github.com/tomasr8/pyjsx) - JSX transpiler for Python

## License

MIT
