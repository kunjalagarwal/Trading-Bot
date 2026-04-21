import argparse
from bot.orders import place_order
from bot.validators import validate_order
from bot.logging_config import setup_logger

logger = setup_logger()

def main():
    parser = argparse.ArgumentParser(description="Trading Bot CLI")

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", required=True)
    parser.add_argument("--price", required=False)

    args = parser.parse_args()

    try:
        validate_order(args.symbol, args.side, args.type, args.quantity, args.price)

        logger.info(f"Placing order: {args}")

        response = place_order(
            symbol=args.symbol,
            side=args.side,
            order_type=args.type,
            quantity=args.quantity,
            price=args.price
        )

        print("\n=== ORDER SUCCESS ===")
        print(f"Order ID: {response.get('orderId')}")
        print(f"Status: {response.get('status')}")
        print(f"Executed Qty: {response.get('executedQty')}")
        print(f"Avg Price: {response.get('avgPrice', 'N/A')}")

        logger.info(f"Response: {response}")

    except Exception as e:
        logger.error(f"Error: {str(e)}")
        print("\n❌ Order Failed:", str(e))

if __name__ == "__main__":
    main()