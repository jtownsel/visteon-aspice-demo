class ECUFlashManager:
    """Flash ECU firmware via UDS protocol (ISO 14229)."""
    
    def flash(self, firmware_path: str, target_ecu: str) -> bool:
        # Deliberately incomplete - will fail CI
        raise NotImplementedError("Flash routine pending validation")
