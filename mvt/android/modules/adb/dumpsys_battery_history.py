# Mobile Verification Toolkit (MVT)
# Copyright (c) 2021-2023 Claudio Guarnieri.
# Use of this software is governed by the MVT License 1.1 that can be found at
#   https://license.mvt.re/1.1/

import logging
from typing import Optional

from mvt.android.artifacts.dumpsys_battery_history import DumpsysBatteryHistoryArtifact

from .base import AndroidExtraction


class DumpsysBatteryHistory(DumpsysBatteryHistoryArtifact, AndroidExtraction):
    """This module extracts records from battery history events."""

    def __init__(
        self,
        file_path: Optional[str] = None,
        target_path: Optional[str] = None,
        results_path: Optional[str] = None,
        module_options: Optional[dict] = None,
        log: logging.Logger = logging.getLogger(__name__),
        results: Optional[list] = None,
    ) -> None:
        super().__init__(
            file_path=file_path,
            target_path=target_path,
            results_path=results_path,
            module_options=module_options,
            log=log,
            results=results,
        )

    def run(self) -> None:
        self._adb_connect()
        output = self._adb_command("dumpsys batterystats --history")
        self._adb_disconnect()

        self.parse(output)

        self.log.info("Extracted %d records from battery history", len(self.results))
