import unittest

from warehouse.rates import shipping_quote


class RateTests(unittest.TestCase):
    # ------------------------------------------------------------------
    # Standard service (preserved behaviour)
    # ------------------------------------------------------------------
    def test_standard_rates(self):
        self.assertEqual(shipping_quote(2, "local"), 8.0)
        self.assertEqual(shipping_quote(2, "regional"), 11.0)

    def test_standard_explicit(self):
        """Explicit service="standard" matches the default."""
        self.assertEqual(
            shipping_quote(2, "local", service="standard"),
            shipping_quote(2, "local"),
        )

    # ------------------------------------------------------------------
    # Express service
    # ------------------------------------------------------------------
    def test_express_local(self):
        """Express local adds $7 to the standard local rate."""
        self.assertEqual(shipping_quote(2, "local", service="express"), 15.0)

    def test_express_regional(self):
        """Express regional adds $7 to the standard regional rate."""
        self.assertEqual(shipping_quote(2, "regional", service="express"), 18.0)

    def test_express_surcharge_is_seven(self):
        """The difference between express and standard is always $7."""
        for zone in ("local", "regional"):
            with self.subTest(zone=zone):
                diff = round(
                    shipping_quote(5, zone, service="express")
                    - shipping_quote(5, zone, service="standard"),
                    2,
                )
                self.assertEqual(diff, 7.0)

    # ------------------------------------------------------------------
    # Validation
    # ------------------------------------------------------------------
    def test_invalid_weight(self):
        with self.assertRaises(ValueError):
            shipping_quote(0, "local")

    def test_invalid_zone(self):
        with self.assertRaises(ValueError):
            shipping_quote(1, "intergalactic")

    def test_invalid_service(self):
        with self.assertRaises(ValueError):
            shipping_quote(1, "local", service="overnight")
