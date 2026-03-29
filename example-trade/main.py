import typer
from src.wallet import create_wallet, wallet_json
from src.util import save_json, load_json, new_info
from src.read import get_dex


app = typer.Typer()

XYZ_DEX_NAME = "XYZ"


@app.command()
def hello():
    print("hello world")


@app.command()
def new_wallet():
    account = create_wallet()
    save_json(wallet_json(account), "wallet.json")


@app.command()
def markets_overview(mainnet: bool = False):
    info = new_info(mainnet, perp_dexs=[XYZ_DEX_NAME])

    mids = info.all_mids(XYZ_DEX_NAME)

    candles = info.candles_snapshot("xyz:SILVER", "1m", 1743225600, 1743225600)

    print(get_dex(info, XYZ_DEX_NAME))


if __name__ == "__main__":
    app()
