# Change Log - Pglet client for Python

## [0.5.9](https://pypi.org/project/pglet/0.5.9)

* Default Pglet Server port is now `8550` (changed from `5000` because of AirDrop service on macOS).
* [PDM](https://pdm.fming.dev/) is used for development and packaging.
* Created a minimal contribution guide: [CONTRIBUTING.md](CONTRIBUTING.md).
* In development mode Pglet Server is automatically downloaded on the first run from GitHub to `$HOME/.pglet/bin`.
* Grid control fixes:
  * Persist selection.
  * Settable `selected_items` property - you can pre-select items in a grid now.
* New `Page` properties: `gap`, `bgcolor`.