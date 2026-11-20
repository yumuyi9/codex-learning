import os
import sys

import requests


def main():
    if len(sys.argv) < 2:
        sys.exit("Missing command-line argument")
    if len(sys.argv) > 2:
        sys.exit("Expected one command-line argument")

    try:
        coins = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    # 在 VS Code 的 PowerShell 中设置 $env:COINCAP_API_KEY，密钥无需写进源码。
    api_key = os.environ.get("COINCAP_API_KEY", "")
    try:
        response = requests.get(
            "https://rest.coincap.io/v3/assets/bitcoin",
            params={"apiKey": api_key},
            timeout=10,
        )
        response.raise_for_status()
        # API 返回的 priceUsd 是字符串，计算前先转为浮点数。
        price = float(response.json()["data"]["priceUsd"])
    except requests.RequestException:
        if not api_key:
            sys.exit("Set the COINCAP_API_KEY environment variable")
        sys.exit("Could not get the Bitcoin price from CoinCap")
    except (KeyError, TypeError, ValueError):
        sys.exit("Unexpected price data from CoinCap")

    print(f"${coins * price:,.4f}")


if __name__ == "__main__":
    main()
