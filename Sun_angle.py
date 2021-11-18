def sun_angle(time):
    h,m = time.split(":")
    time_dec = float(h) + float(m) / 60
    sun_angle = (time_dec - 6) * 15

    if (sun_angle >= 0 and sun_angle <= 180):
        return round(sun_angle, 2)
    else:
        return "I don't see the sun!"

# assert sun_angle("18:00") == 0
# print(sun_angle("12:15"))
# assert sun_angle("12:15") == 93.75
#
# assert sun_angle("01:23") == "I don't see the sun!"

sun_angle("6:00")
sun_angle("7:00")
sun_angle("10:00")
sun_angle("12:00")