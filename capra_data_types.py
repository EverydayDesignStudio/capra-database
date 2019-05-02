# Defines a picture object


class Picture:
    def __init__(self, picture_id, time, altitude, color, hike_id,
                 index_in_hike, camera1, camera2, camera3):
        self.picture_id = picture_id
        self.time = time
        self.altitude = altitude
        self.color = color
        self.hike_id = hike_id
        self.index_in_hike = index_in_hike
        self.camera1 = camera1
        self.camera2 = camera2
        self.camera3 = camera3


# Defines a hike object


class Hike:
    def __init__(self, hike_id, average_altitude, average_color, start_time,
                 end_time, pictures_num):
        self.hike_id = hike_id
        self.average_altitude = average_altitude
        self.average_color = average_color
        self.start_time = start_time
        self.end_time = end_time
        self.pictures_num = pictures_num