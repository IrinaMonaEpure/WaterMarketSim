from pathlib import Path

import yaml

from WaterMarketSim.population import generate_population


def load_config(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as file:
        return yaml.safe_load(file)


def main() -> None:
    config_path = Path("configs/baseline.yaml")
    config = load_config(config_path)

    print("Barahathawa drought-to-flood model")
    print(f"Location: {config['location']['name']}")
    print(f"Farmers: {config['simulation']['n_farmers']}")
    print(f"Days: {config['simulation']['n_days']}")
    print(f"Seed: {config['simulation']['seed']}")

    farmers = generate_population(config)

    print("\nSynthetic farmer population:")
    print(farmers.head())

    print("\nPopulation by KC category:")
    print(farmers["kc_category"].value_counts())

    print("\nGroundwater infrastructure ownership by category:")
    print(
        farmers.groupby("kc_category")[
            ["owns_borehole", "owns_pump"]
        ].mean().round(3)
    )


if __name__ == "__main__":
    main()