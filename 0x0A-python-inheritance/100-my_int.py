#!/usr/bin/python3
"""Integer representation class"""


class MyInt(int):
    """A class that overrides integer operations to invert them."""

    def __eq__(self, other):
        """Override the == operator."""
        return super().__ne__(other)

    def __ne__(self, other):
        """Override the != operator."""
        return super().__eq__(other)
