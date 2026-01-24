class ConfigError(Exception):
    def __init__(self, message="Error applying configuration"):
        super().__init__(message)
