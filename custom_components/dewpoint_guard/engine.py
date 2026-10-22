"""Pure dew point and condensation-risk calculations."""
from __future__ import annotations
from math import log
from homeassistant.const import UnitOfTemperature

def to_celsius(value: float, unit: str | None) -> float:
    if unit == UnitOfTemperature.FAHRENHEIT:
        return (value - 32.0) * 5.0 / 9.0
    return value

def calculate(config, values, units):
    try:
        air = to_celsius(float(values["air_temperature_entity"]), units["air_temperature_entity"])
        humidity = float(values["humidity_entity"])
        surface = to_celsius(float(values["surface_temperature_entity"]), units["surface_temperature_entity"])
        if not 0 < humidity <= 100:
            raise ValueError("relative humidity must be greater than 0 and at most 100")
        gamma = log(humidity / 100.0) + 17.62 * air / (243.12 + air)
        dewpoint = 243.12 * gamma / (17.62 - gamma)
        margin = surface - dewpoint
        return {"dew_point": round(dewpoint, 2), "margin": round(margin, 2), "risk": margin <= float(config["risk_margin"])}
    except (TypeError, ValueError, ZeroDivisionError, OverflowError):
        return {"dew_point": None, "margin": None, "risk": None}
