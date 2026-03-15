from __future__ import annotations

from .pipeline import run_trading_system


def main() -> None:
    result = run_trading_system()
    print(result["report"])


if __name__ == "__main__":
    main()
