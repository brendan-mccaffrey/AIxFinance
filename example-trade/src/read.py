import time
from typing import Optional
from hyperliquid.info import Info
from hyperliquid.exchange import Exchange
from hyperliquid.utils.constants import TESTNET_API_URL
from src.util import save_json


def perp_overview(info: Info):
    network = "testnet" if info.base_url == TESTNET_API_URL else "mainnet"

    perp_dex_to_offset = {"": 0}
    perp_dexs = info.perp_dexs()

    for i, perp_dex in enumerate(perp_dexs[1:]):
        # builder-deployed perp dexs start at 110000
        perp_dex_to_offset[perp_dex["name"]] = 110000 + i * 10000

    save_json(perp_dexs, f"{network}/dexs/all.json")
    save_json(perp_dex_to_offset, f"{network}/dexs/offsets.json")


def dex_ctx(info: Info, dex: str):
    return info.post("/info", {"type": "metaAndAssetCtxs", "dex": dex})


def get_dex(info: Info, dex_name: str):
    network = "testnet" if info.base_url == TESTNET_API_URL else "mainnet"

    for i, perp_dex in enumerate(info.perp_dexs()[1:]):
        if perp_dex["name"] == dex_name:

            # save overview, meta, and ctx
            save_json(perp_dex, f"{network}/dexs/{dex_name}/overview.json")

            meta = info.meta(dex_name)
            save_json(meta, f"{network}/dexs/{dex_name}/meta.json")
            for i, asset in enumerate(meta["universe"]):
                print(i, asset["name"])

            ctx = dex_ctx(info, dex_name)
            save_json(ctx, f"{network}/dexs/{dex_name}/ctx.json")

            universe = ctx[0]["universe"]
            prices = ctx[1]

            new_state = {}
            for item, px_data in zip(universe, prices):
                ticker = item["name"].split(":")[1]
                new_state[ticker] = {
                    "external_fair_px": px_data["oraclePx"],
                    "reference_px": px_data["oraclePx"],
                }
            save_json(new_state, f"{network}/dexs/{dex_name}/state.json")

            return ctx

    return None
