import json
from pathlib import Path
from typing import List, Optional
from eth_account.signers.local import LocalAccount
from hyperliquid.info import Info
from hyperliquid.exchange import Exchange
from hyperliquid.utils.constants import MAINNET_API_URL, TESTNET_API_URL


def new_info(mainnet: bool = False, skip_ws: bool = True, perp_dexs: Optional[List[str]] = None) -> Info:
    return Info(MAINNET_API_URL if mainnet else TESTNET_API_URL, skip_ws, perp_dexs=perp_dexs)


def new_exchange(account: LocalAccount, mainnet: bool = False, perp_dexs: Optional[List[str]] = None) -> Exchange:
    return Exchange(account, MAINNET_API_URL if mainnet else TESTNET_API_URL, perp_dexs=perp_dexs)


def save_json(data: dict, file: Path, absolute_path: bool = False):
    if not absolute_path:
        file = Path("data") / file

    file.parent.mkdir(parents=True, exist_ok=True)
    with file.open("w") as f:
        json.dump(data, f, indent=2)
    print(f"saved {file}")


def load_json(file: Path) -> dict:
    file = file.with_suffix(".json")
    with file.open("r") as f:
        return json.load(f)
