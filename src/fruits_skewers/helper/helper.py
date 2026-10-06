def strtobool(s: str) -> bool:
    s = s.lower()
    if s in ("y", "yes", "t", "true", "on", "1"):
        return True
    elif s in ("n", "no", "f", "false", "off", "0"):
        return False
    else:
        return bool(s)
