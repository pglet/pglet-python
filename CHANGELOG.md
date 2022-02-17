# Change Log - Pglet client for Python

## [0.7.0](https://pypi.org/project/pglet/0.7.0) - Feb 17, 2022

Works with [Pglet Server 0.7.0](https://github.com/pglet/pglet/releases/tag/v0.7.0).

New `SplitStack` control (based on [split.js](https://split.js.org/)) which could be used as a drop-in replacement for `Stack`, but with resize gutters instead of gaps. Check out [SplitStack control example](https://github.com/pglet/examples/blob/main/python/controls/split.py).

New `TextBox` control properties:
* `shiftEnter` (bool) - blocks ENTER button in `multiline` TextBox, but pops up the event, so `Stack.submit` could be triggered. New line could still be entered with SHIFT+ENTER. This is to build Discord-like message box.
* `rows` (int) - sets initial size in rows of `multiline` TextBox.
* `resizable` (bool) - controls whether `multiline` TextBox is resizable by the user. Default is `true`. `autoAdjustHeight` is still respected even if `resizable` is `false`.

`Panel` control changes:
* `blocking` (bool) is now `true` by default.

`border_style` property in `Image`, `IFrame`, `Stack` and `Text` allows lists, for example:

```python
stack.border_style = ["solid", "double"]  # top and bottom borders are solid, left and right are double
```


## [0.6.0](https://pypi.org/project/pglet/0.6.0) - Feb 13, 2022

* Works with [Pglet Server 0.6.0](https://github.com/pglet/pglet/releases/tag/v0.6.0).
* Added `focused` property, `focus` and `blur` events to all input controls - paving the way to a proper validation support.
* New [`Persona`](https://developer.microsoft.com/en-us/fluentui#/controls/web/persona) control.
* New [`ComboBox`](https://developer.microsoft.com/en-us/fluentui#/controls/web/combobox) control.
* New page events: `connect` and `disconnect` for real-time chat-like experiences.
* Harmonization of border styling propeties across `Stack`, `Image`, `IFrame` and `Text` controls: HTML-ish `border` property with mixed and confusing to non-web devs semantics (`1px solid black` or `solid 1px black`?) replaced with clean and simple `border_style`, `border_width` and `border_color` properties.
* All boolean and enum-like properties are protected with [`beartype`](https://github.com/beartype/beartype).
* Fixed all control tests to ensure [Pglet works nice with Python 3.7 and above](https://ci.appveyor.com/project/pglet/pglet-python). Big shout-out to [@mikaelho](https://github.com/mikaelho) for helping with that!
* [Black](https://github.com/psf/black) and [isort](https://pycqa.github.io/isort/) was adopted as official formatting tools.
* Generating platform-specific wheels (`.whl`) with one `pglet` executable inside only: smaller wheels - faster installation!


## [0.5.9](https://pypi.org/project/pglet/0.5.9) - Jan 27, 2022

* Default Pglet Server port is now `8550` (changed from `5000` because of AirDrop service on macOS).
* [PDM](https://pdm.fming.dev/) is used for development and packaging.
* Created a minimal contribution guide: [CONTRIBUTING.md](CONTRIBUTING.md).
* In development mode Pglet Server is automatically downloaded on the first run from GitHub to `$HOME/.pglet/bin`.
* Grid control fixes:
  * Persist selection.
  * Settable `selected_items` property - you can pre-select items in a grid now.
* New `Page` properties: `gap`, `bgcolor`.