"""Anticloud egress guard (behaviour-changing patch).

Added by Anticloud. Refuses hosted frontier API calls so this repository
honours its declared offline posture instead of merely asserting it.

Licence interaction: this file is licensed Apache-2.0 OR
LicenseRef-Anticommons-Enterprise-1.0 and is kept in a separate module so the
upstream tree's own licence is not extended over it.
"""

from __future__ import annotations

import os
import socket

__all__ = ["EgressDenied", "guarded_connect", "is_offline"]

_OFFLINE = "ANTICLOUD_OFFLINE"

#: Hosts that mean "someone else's paid, hosted model".
_FRONTIER_MARKERS = (
    "api.openai.com", "api.anthropic.com", "api.cohere.ai",
    "api.mistral.ai", "api.groq.com", "api.together.xyz",
    "api.deepseek.com", "generativelanguage.googleapis.com",
    "api.perplexity.ai", "openrouter.ai", "api.fireworks.ai",
)


class EgressDenied(PermissionError):
    """Raised when a blocked host is contacted while offline mode is on."""


def is_offline() -> bool:
    value = os.environ.get(_OFFLINE, "").strip().lower()
    return value not in ("", "0", "false", "no")


def _is_frontier(host: str) -> bool:
    h = (host or "").lower().split(":")[0]
    return any(h == m or h.endswith("." + m) for m in _FRONTIER_MARKERS)


def guarded_connect(address, *args, **kwargs):
    """Drop-in `socket.create_connection` replacement.

    Local addresses are always permitted: an offline guarantee is about
    hosted frontier spend, not about a model running on this machine.
    """
    host = address[0] if isinstance(address, tuple) else address
    if is_offline() and _is_frontier(str(host)):
        raise EgressDenied(
            f"offline mode: refusing connection to frontier host {host!r}. "
            f"Set {_OFFLINE}=0 to allow, or run the model locally.")
    return _ORIGINAL(address, *args, **kwargs)


_ORIGINAL = socket.create_connection
_PATCHED = False


def install() -> bool:
    """Idempotently install the guard. Returns True if it is now active."""
    global _PATCHED
    if not is_offline():
        return False
    if not _PATCHED:
        socket.create_connection = guarded_connect
        _PATCHED = True
    return True
