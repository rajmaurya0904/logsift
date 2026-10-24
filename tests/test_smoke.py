"""Smoke test: package imports cleanly. Replace/extend as modules land."""

import logsift


def test_version_is_set() -> None:
    assert logsift.__version__
