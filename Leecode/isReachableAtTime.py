def isReachableAtTime(sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
    if sx == fx and sy == fy:
        return True

    return t in range(fx - sx, (fx - sx + 1) * (fy - sy + 1) - 1)

