import time

class Space():
    """each object of this class stores information about
    the each individual space agency launches"""
    def __init__(self, num, agency, site, location, day, mm, dd, yyyy,
                 time, time_Zone, rocketName, active, cost, suc_or_fail):
        self.num = 0
        self.agency = agency
        self.site = site
        self.location = location
        self.day = day
        self.mm = mm
        self.dd = dd
        self.yyyy = yyyy
        self.time = time
        self.time_Zone = time_Zone
        self.rocketName = rocketName
        self.active = active
        self.cost = cost
        self.suc_or_fail = suc_or_fail

    def pacific_time_convertor(self):
         """converts time from UCT to PST"""
         time_pieces = self.time.split(":")
         hours = int(time_pieces[0])
         min = int(time_pieces[1])
         print(str(hours) + ":" + str(min) +
               " Coordinated Universal Time")
         hours += 7
         if hours > 12:
            hours -= 12
         print(str(hours) + ":" + str(min) + " Pacific Standard Time")

    def spending(self):
        print(self.agency + " spent " + str(self.cost) +
              " million dollars to launch the " + self.rocketName)

    def launch_facility(self):
        print("the " + self.rocketName + " was launched at " + self.site)

    # tells user exactly how long ago this rocket launched
    def time_since_launch(self):
        pass


setString = "0, SpaceX, LC-39A Kennedy Space Center, Florida USA, " \
            "Fri, 8, 07, 2020, 05:12, UTC, Falcon 9 Block 5 | Starlink V1 " \
            "L9 & BlackSky, 1, 50.0, 1" \
            "1, CASC, Site 9401 (SLS-2) Jiuquan Satellite Launch Center, " \
            "China, Thu, 8, 06, 2020, 04:01, UTC, Long March 2D | Gaofen-9 04 " \
            "& Q-SAT, 1, 29.75, 1" \
            "2, SpaceX, Pad A Boca Chica, Texas USA, Tue, 8, 04, 2020, " \
            "23:57, UTC, Starship Prototype | 150 Meter Hop, 1, N/A, 1" \
            "3, Roscosmos, Site 200/39 Baikonur Cosmodrome, Kazakhstan, " \
            "Thu, 7, 3, 2020, 21:25, UTC, Proton-M/Briz-M | Ekspress-80 & " \
            "Ekspress-103, 1, 165.0, 1" \
            "4, ULA, SLC-41, Cape Canaveral AFS, Florida USA, Thu, 7, 30, 2020, " \
            "11:50, UTC, Atlas V 541 | Perseverance, 1, 145.0, 1"

                                                                          #
setTuple = [(0, "SpaceX", "LC-39A Kennedy Space Center", "Florida USA",
             "Fri", 8,7, 2020, "5:12", "UTC",
             "Falcon 9 Block 5 Starlink V1 L9 & BlackSky", 1, 50.0, 1),
            (1,"CASC", "Site 9401 (SLS-2) Jiuquan Satellite Launch Center",
             "China", "Thu", 8, 6, 2020, "4:01", "UTC",
             "Long March 2D | Gaofen-9 04 & Q-SAT", 1, 29.75, 1),
            (2, "SpaceX", "Pad A Boca Chica", "Texas USA", "Tue", 8, 4,
             2020, "23:57", "UTC", "Starship Prototype | 150 Meter Hop",
             1, 0, 1),
            (3, "Roscosmos", "Site 200/39 Baikonur Cosmodrome",
             "Kazakhstan", "Thu", 7, 3, 2020, "21:25", "UTC",
             "Proton-M/Briz-M | Ekspress-80 & Ekspress-103", 1, 165.0, 1),
            (4, "ULA", "SLC-41, Cape Canaveral AFS", "Florida USA", "Thu",
             7, 30, 2020, "11:50", "UTC", "Atlas V 541 | Perseverance",
             1, 145.0, 1)]

another_tuple = (1,2,3),(4,5,6),(7,8,9)

agency1 = Space(0, "SpaceX", "LC-39A Kennedy Space Center", "Florida USA",
                "Fri", 8, 7, 2020, "5:12", "UTC",
                "Falcon 9 Block 5 | Starlink V1 L9 & BlackSky", 1,50.0,1)

agency1.spending()
agency1.pacific_time_convertor()
agency1.launch_facility()