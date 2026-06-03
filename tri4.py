import fastf1
import matplotlib.pyplot as plt
import os


# Make sure the cache folder exists
os.makedirs("cache", exist_ok=True)

fastf1.Cache.enable_cache("cache")

fastf1.Cache.enable_cache("cache")
session = fastf1.get_session(
    2024,
    "monaco",

    "Q"
)
session.load()
lap = session.laps.pick_fastest()
pos = lap.get_pos_data()
plt.plot(
    pos["X"],
    pos["Y"],
    lw = 4
)
plt.axis("equal"),plt.title("Monaco GP Track")
plt.show()