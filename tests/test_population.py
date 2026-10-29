from pathlib import Path

import pandas as pd

from WaterMarketSim.main import load_config
from WaterMarketSim.population import generate_population


def test_population_size():
    config = load_config(Path("configs/baseline.yaml"))
    farmers = generate_population(config)

    assert len(farmers) == config["simulation"]["n_farmers"]


def test_reproducibility():
    config = load_config(Path("configs/baseline.yaml"))

    first = generate_population(config)
    second = generate_population(config)

    pd.testing.assert_frame_equal(first, second)


def test_population_attributes():
    config = load_config(Path("configs/baseline.yaml"))
    farmers = generate_population(config)

    assert farmers["farmer_id"].is_unique
    assert (farmers["land_area_ha"] > 0).all()
    assert (farmers["initial_assets_npr"] >= 0).all()

    assert farmers["owns_borehole"].dtype == bool
    assert farmers["owns_pump"].dtype == bool
    assert farmers["canal_access"].dtype == bool


def test_all_categories_are_known():
    config = load_config(Path("configs/baseline.yaml"))
    farmers = generate_population(config)

    assert farmers["kc_category"].notna().all()