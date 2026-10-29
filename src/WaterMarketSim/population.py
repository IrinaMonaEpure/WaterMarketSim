import numpy as np
import pandas as pd


def generate_population(config: dict) -> pd.DataFrame:
    """Generate a synthetic population informed by census and access data."""

    n = config["simulation"]["n_farmers"]
    rng = np.random.default_rng(config["simulation"]["seed"])
    params = config["population"]

    census = pd.read_csv(params["census_path"])
    access = pd.read_csv(params["groundwater_indices_path"])

    # Sample caste/ethnicity using census population shares.
    probabilities = census["population"] / census["population"].sum()

    sampled = rng.choice(
        len(census),
        size=n,
        p=probabilities,
    )

    farmers = census.iloc[sampled][
        ["caste_ethnicity", "kc_category"]
    ].reset_index(drop=True)

    farmers.insert(0, "farmer_id", np.arange(n))

    # Attach relative groundwater ownership indices.
    farmers = farmers.merge(
        access,
        on="kc_category",
        how="left",
        validate="many_to_one",
    )

    # Unclassified groups use neutral indices as an explicit assumption.
    farmers["borehole_index"] = farmers["borehole_index"].fillna(1.0)
    farmers["pump_index"] = farmers["pump_index"].fillna(1.0)

    # Convert relative indices into illustrative ownership probabilities.
    borehole_prob = np.clip(
        params["borehole_ownership_probability"]
        * farmers["borehole_index"].to_numpy(),
        0,
        1,
    )

    pump_prob = np.clip(
        params["pump_ownership_probability"]
        * farmers["pump_index"].to_numpy(),
        0,
        1,
    )

    farmers["owns_borehole"] = rng.random(n) < borehole_prob
    farmers["owns_pump"] = rng.random(n) < pump_prob

    land_min, land_max = params["land_area_ha"]
    assets_min, assets_max = params["initial_assets_npr"]

    farmers["land_area_ha"] = rng.uniform(
        land_min, land_max, n
    )

    farmers["initial_assets_npr"] = rng.uniform(
        assets_min, assets_max, n
    )

    farmers["canal_access"] = (
        rng.random(n) < params["canal_access_probability"]
    )

    return farmers