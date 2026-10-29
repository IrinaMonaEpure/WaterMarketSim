from pathlib import Path

from WaterMarketSim.main import load_config


def test_load_config():
    config = load_config(Path("configs/baseline.yaml"))

    assert config["simulation"]["n_farmers"] > 0
    assert config["simulation"]["n_days"] > 0
    assert config["location"]["name"] == "Barahathawa"