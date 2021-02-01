class GPSObject:
    def __init__(self, ssid, suid, ts, lat, lon, alt=0, conf=1, cov_xx=0.0, cov_yy=0.0, cov_xy=0.0):
        self.ssid = ssid
        self.suid = suid
        self.ts = ts
        self.lat = lat
        self.lon = lon
        self.alt = alt
        self.conf = conf
        self.cov_xx = cov_xx
        self.cov_yy = cov_yy
        self.cov_xy = cov_xy

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f"GPSObject @{self.ts} [{self.ssid}/{self.suid}] {self.conf:.2f}: {self.lat}, {self.lon}, {self.alt}"
