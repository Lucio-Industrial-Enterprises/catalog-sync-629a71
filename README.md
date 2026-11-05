# Warehouse tools

Small Python utilities for warehouse order and shipping workflows.

Run the tests with `python3 -m unittest discover -s tests -v`.

## Shipping

`shipping_quote(weight_kg, zone, service="standard")` returns a delivery quote
in USD.

| Parameter   | Values                      | Notes                              |
|-------------|-----------------------------|------------------------------------|
| `weight_kg` | any positive float          | Parcel weight in kilograms         |
| `zone`      | `"local"`, `"regional"`    | Delivery zone                      |
| `service`   | `"standard"`, `"express"`  | Default `"standard"`; express adds a flat **$7** surcharge |

Rates (before the express surcharge):

| Zone       | Formula                      |
|------------|------------------------------|
| local      | $5.00 + $1.50 × weight\_kg  |
| regional   | $8.00 + $1.50 × weight\_kg  |

### CLI usage

```
python -m warehouse.cli <weight_kg> <zone> [--service {standard,express}]
```

Examples:

```
# Standard quote — 3 kg, local zone
python -m warehouse.cli 3 local
# $9.50

# Express quote — 3 kg, local zone
python -m warehouse.cli 3 local --service express
# $16.50
```
