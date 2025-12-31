import inspect
from typing import Any, Protocol

from textual.widget import Widget

type JSXComponent = type[Widget]
type JSX = list[Widget]
type _Child = JSX | str


class JSXFragment(Protocol):
    def __call__(self, *args: Any, **kwds: Any) -> JSX: ...


def _flatten_children(children: list[_Child]) -> list[Widget | str]:
    result: list[Widget | str] = []
    for child in children:
        if isinstance(child, list):
            result.extend(child)
        else:
            result.append(child)
    return result


class _JSX:
    def __call__(
        self,
        tag: JSXComponent | JSXFragment,
        props: dict[str, Any],
        children: list[JSX],
    ) -> JSX:
        if inspect.isclass(tag) and issubclass(tag, Widget):
            return [tag(*_flatten_children(children), **props)]  # type: ignore
        else:
            return tag(children=children)

    def Fragment(
        self,
        *,
        children: list[JSX],
        **_: Any,
    ) -> JSX:
        return _flatten_children(children)  # type: ignore


jsx = _JSX()
