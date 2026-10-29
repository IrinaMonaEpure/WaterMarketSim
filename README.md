# Barahathawa Drought-to-Flood Model

A Python research prototype investigating how farmers' irrigation decisions during drought can influence their financial vulnerability to subsequent flooding.

## Research question

Does the financial burden of drought adaptation increase vulnerability to a subsequent flood, and how might this vary between socioeconomic groups?

## Planned components

1. A simplified agent-based model of farmer irrigation decisions, groundwater access, and household finances.
2. Satellite-derived flood exposure analysis using Sentinel-1 imagery and agricultural land-cover data for Barahathawa Municipality, Nepal.

## Installation

```bash
python -m pip install -e ".[dev]"
```

## Run

From the repository root:

```bash
WaterMarketSim
```

## Tests

```bash
pytest -q
```

## Status

Early-stage research prototype. All initial simulation parameters are illustrative. The model has not been calibrated or validated against observations from the 2025 Nepal drought and flood events.

## Scientific background

The project is motivated by research on socio-hydrological modelling, groundwater access inequalities, and compound drought–flood risk, including:
> De Bruijn, J. A., Smilovic, M., Burek, P., Guillaumot, L., Wada, Y., & Aerts, J. C. (2023). GEB v0. 1: a large-scale agent-based socio-hydrological model–simulating 10 million individual farming households in a fully distributed hydrological model. Geoscientific Model Development, 16(9), 2437-2454.

> Kalthof, M. W., De Bruijn, J., De Moel, H., Kreibich, H., & Aerts, J. C. (2025). Adaptive behavior of farmers under consecutive droughts results in more vulnerable farmers: a large-scale agent-based modeling analysis in the Bhima basin, India. Natural Hazards and Earth System Sciences, 25(3), 1013-1035.

> KC, Sumitra, Manohara Khadka, Anuj Mishra, and Anil Aryal. 2026. Mapping the Invisible: Groundwater Use, Access, Equity, and Governance in Nepal’s Southern Plains; Policy Pathways for Equitable and Sustainable Groundwater Use. International Water Management Institute (IWMI).

> Ward, P. J., de Ruiter, M. C., Mård, J., Schröter, K., Van Loon, A., Veldkamp, T., ... & Wens, M. (2020). The need to integrate flood and drought disaster risk reduction strategies. Water security, 11, 100070.