# Dewpoint Guard

**Monitor cold surfaces for condensation risk using local temperature and humidity sensors.**

A room can look dry while a cold wall or window is already close to condensation. This integration compares the calculated dew point with a measured surface temperature.

## Features

- Dew point in °C, calculated with the Magnus approximation.
- Surface margin in °C (surface temperature minus dew point).
- Condensation risk binary sensor when the margin is at or below your chosen threshold.

## Install with HACS

1. In Home Assistant, open **HACS → Integrations**.
2. Add `https://github.com/CodeArcade-ctrl/dewpoint-guard` as a custom repository of type **Integration**.
3. Install **Dewpoint Guard** and restart Home Assistant.
4. Open **Settings → Devices & services → Add integration** and select **Dewpoint Guard**.

The catalog request is pending review. Until it is accepted, users must add this repository as a custom repository.

## Privacy and limitations

All calculations run locally in Home Assistant. The integration reads only the selected entities and makes no external network requests. Inputs must have valid numeric states; derived values are unavailable while source values are unknown or invalid.

## License

MIT. See [LICENSE](LICENSE).
