import json
import secrets
from pathlib import Path
from eth_account import Account
from eth_account.signers.local import LocalAccount


def generate_secure_private_key():
    """Generate a cryptographically secure 256-bit private key"""
    random_bytes = secrets.token_bytes(32)
    return random_bytes.hex()


def create_wallet() -> LocalAccount:
    """Generate a wallet file with a given number of iterations."""

    account: LocalAccount = Account.create()
    print("Generated wallet")
    print(f"Ethereum Address    : {account.address}")
    print(f"Private Key         : 0x{account.key.hex()}")

    return account


def wallet_json(account: LocalAccount):
    return {
        "address": account.address,
        "private_key": account.key.hex(),
    }
