# Change Log - Pglet client for Python

## [0.6.0](https://pypi.org/project/pglet/0.6.0)

* Works with [Pglet Server 0.6.0](https://github.com/pglet/pglet/releases/tag/v0.6.0).
* Added `focused` property, `focus` and `blur` events to all input controls - paving the way to a proper validation support.
* New [`Persona`](https://developer.microsoft.com/en-us/fluentui#/controls/web/persona) control.
* New [`ComboBox`](https://developer.microsoft.com/en-us/fluentui#/controls/web/combobox) control.
* New page events: `connect` and `disconnect` for real-time chat-like experiences.
* Harmonization of border styling propeties across `Stack`, `Image`, `IFrame` and `Text` controls: HTML-ish `border` property with mixed and confusing to non-web devs semantics (`1px solid black` or `solid 1px black`?) replaced with clean and simple `border_style`, `border_width` and `border_color` properties.
* All boolean and enum-like properties are protected with [`beartype`](https://github.com/beartype/beartype).
* Fixed all control tests to ensure [Pglet works nice with Python 3.7 and above](https://ci.appveyor.com/project/pglet/pglet-python). Big shout-out to @mikaelho for helping with that!
* Generating platform-specific wheels (`.whl`) with one `pglet` executable inside only: smaller wheels - faster installation!


## [0.5.9](https://pypi.org/project/pglet/0.5.9)

* Default Pglet Server port is now `8550` (changed from `5000` because of AirDrop service on macOS).
* [PDM](https://pdm.fming.dev/) is used for development and packaging.
* Created a minimal contribution guide: [CONTRIBUTING.md](CONTRIBUTING.md).
* In development mode Pglet Server is automatically downloaded on the first run from GitHub to `$HOME/.pglet/bin`.
* Grid control fixes:
  * Persist selection.
  * Settable `selected_items` property - you can pre-select items in a grid now.
* New `Page` properties: `gap`, `bgcolor`.