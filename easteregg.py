import json

#  _    _                           ______          _             
# | |  | |                         |  ____|        | |            
# | |__| | __ _ _ __  _ __  _   _  | |__   __ _ ___| |_ ___ _ __  
# |  __  |/ _` | '_ \| '_ \| | | | |  __| / _` / __| __/ _ \ '__| 
# | |  | | (_| | |_) | |_) | |_| | | |___| (_| \__ \ ||  __/ |    
# |_|  |_|\__,_| .__/| .__/ \__, | |______\__,_|___/\__\___|_|    
#              | |   | |     __/ |                                
#   __         |_|   |_|    |___/   _    _ _____ _   _ _____      
#  / _|                     | |    | |  | |_   _| \ | |  __ \     
# | |_ _ __ ___  _ __ ___   | |    | |__| | | | |  \| | |  | |    
# |  _| '__/ _ \| '_ ` _ \  | |    |  __  | | | | . ` | |  | |    
# | | | | | (_) | | | | | | | |____| |  | |_| |_| |\  | |__| |    
# |_| |_|  \___/|_| |_| |_| |______|_|  |_|_____|_| \_|_____/     


flights_json = """[{"flight_no": "LH61", "departure_datetime": "2021-04-14T01:06:44.619712"}, {"flight_no": "LH54", "departure_datetime": "2021-04-14T14:33:44.619712"}, {"flight_no": "LH97", "departure_datetime": "2021-04-11T18:08:44.619712"}, {"flight_no": "LH47", "departure_datetime": "2021-03-27T10:26:44.619712"}, {"flight_no": "LH108", "departure_datetime": "2021-03-28T07:48:44.619712"}, {"flight_no": "LH61", "departure_datetime": "2021-04-10T18:06:44.619712"}, {"flight_no": "LH116", "departure_datetime": "2021-03-25T20:52:44.619712"}, {"flight_no": "LH121", "departure_datetime": "2021-03-28T18:47:44.619712"}, {"flight_no": "LH115", "departure_datetime": "2021-04-05T05:47:44.619712"}, {"flight_no": "LH97", "departure_datetime": "2021-04-16T18:50:44.619712"}, {"flight_no": "LH115", "departure_datetime": "2021-03-31T21:47:44.619712"}, {"flight_no": "LH112", "departure_datetime": "2021-04-09T03:03:44.619712"}, {"flight_no": "LH97", "departure_datetime": "2021-04-01T13:16:44.619712"}, {"flight_no": "LH112", "departure_datetime": "2021-03-27T21:58:44.619712"}, {"flight_no": "LH110", "departure_datetime": "2021-04-06T01:47:44.619712"}, {"flight_no": "LH112", "departure_datetime": "2021-04-03T07:51:44.619712"}, {"flight_no": "LH47", "departure_datetime": "2021-04-05T16:50:44.619712"}, {"flight_no": "LH38", "departure_datetime": "2021-04-12T17:38:44.619712"}, {"flight_no": "LH102", "departure_datetime": "2021-03-30T00:36:44.619712"}, {"flight_no": "LH108", "departure_datetime": "2021-04-16T04:59:44.619712"}, {"flight_no": "LH111", "departure_datetime": "2021-04-02T17:38:44.619712"}, {"flight_no": "LH61", "departure_datetime": "2021-04-18T13:59:44.619712"}, {"flight_no": "LH46", "departure_datetime": "2021-03-29T07:48:44.619712"}, {"flight_no": "LH98", "departure_datetime": "2021-04-11T03:53:44.619712"}, {"flight_no": "LH97", "departure_datetime": "2021-04-17T23:35:44.619712"}, {"flight_no": "LH46", "departure_datetime": "2021-04-07T15:14:44.619712"}, {"flight_no": "LH105", "departure_datetime": "2021-04-13T05:23:44.619712"}, {"flight_no": "LH108", "departure_datetime": "2021-03-29T15:22:44.619712"}, {"flight_no": "LH112", "departure_datetime": "2021-03-26T16:14:44.619712"}, {"flight_no": "LH114", "departure_datetime": "2021-04-04T18:48:44.619712"}, {"flight_no": "LH115", "departure_datetime": "2021-03-26T22:06:44.619712"}, {"flight_no": "LH103", "departure_datetime": "2021-04-18T00:23:44.619712"}, {"flight_no": "LH116", "departure_datetime": "2021-03-30T13:29:44.619712"}, {"flight_no": "LH112", "departure_datetime": "2021-04-08T06:56:44.619712"}, {"flight_no": "LH100", "departure_datetime": "2021-04-13T21:31:44.619712"}, {"flight_no": "LH38", "departure_datetime": "2021-04-15T12:22:44.619712"}, {"flight_no": "LH101", "departure_datetime": "2021-04-06T17:30:44.619712"}, {"flight_no": "LH112", "departure_datetime": "2021-03-28T02:11:44.619712"}, {"flight_no": "LH47", "departure_datetime": "2021-03-27T19:32:44.619712"}, {"flight_no": "LH103", "departure_datetime": "2021-04-01T18:10:44.619712"}, {"flight_no": "LH111", "departure_datetime": "2021-04-11T00:18:44.619712"}, {"flight_no": "LH100", "departure_datetime": "2021-04-06T09:22:44.619712"}, {"flight_no": "LH63", "departure_datetime": "2021-04-09T06:42:44.619712"}, {"flight_no": "LH101", "departure_datetime": "2021-04-04T09:40:44.619712"}, {"flight_no": "LH101", "departure_datetime": "2021-04-04T12:31:44.619712"}, {"flight_no": "LH110", "departure_datetime": "2021-03-31T17:55:44.619712"}, {"flight_no": "LH97", "departure_datetime": "2021-03-27T20:16:44.619712"}, {"flight_no": "LH99", "departure_datetime": "2021-04-03T15:06:44.619712"}, {"flight_no": "LH114", "departure_datetime": "2021-04-02T09:55:44.619712"}, {"flight_no": "LH116", "departure_datetime": "2021-03-26T09:40:44.619712"}, {"flight_no": "LH101", "departure_datetime": "2021-04-18T11:26:44.619712"}, {"flight_no": "LH104", "departure_datetime": "2021-04-08T16:05:44.619712"}, {"flight_no": "LH49", "departure_datetime": "2021-04-14T14:45:44.619712"}, {"flight_no": "LH117", "departure_datetime": "2021-04-17T16:38:44.619712"}, {"flight_no": "LH97", "departure_datetime": "2021-04-03T15:08:44.619712"}, {"flight_no": "LH58", "departure_datetime": "2021-03-27T01:47:44.619712"}, {"flight_no": "LH46", "departure_datetime": "2021-04-03T12:13:44.619712"}, {"flight_no": "LH97", "departure_datetime": "2021-03-31T16:39:44.619712"}, {"flight_no": "LH106", "departure_datetime": "2021-04-10T18:37:44.619712"}, {"flight_no": "LH55", "departure_datetime": "2021-04-14T11:58:44.619712"}, {"flight_no": "LH48", "departure_datetime": "2021-04-14T22:05:44.619712"}, {"flight_no": "LH117", "departure_datetime": "2021-04-02T22:43:44.619712"}, {"flight_no": "LH99", "departure_datetime": "2021-04-10T01:56:44.619712"}, {"flight_no": "LH104", "departure_datetime": "2021-03-25T06:47:44.619712"}, {"flight_no": "LH49", "departure_datetime": "2021-04-18T20:52:44.619712"}, {"flight_no": "LH97", "departure_datetime": "2021-04-09T16:16:44.619712"}, {"flight_no": "LH57", "departure_datetime": "2021-04-14T19:29:44.619712"}, {"flight_no": "LH104", "departure_datetime": "2021-03-31T01:06:44.619712"}, {"flight_no": "LH120", "departure_datetime": "2021-04-07T02:37:44.619712"}, {"flight_no": "LH110", "departure_datetime": "2021-04-17T01:18:44.619712"}, {"flight_no": "LH100", "departure_datetime": "2021-04-12T09:49:44.619712"}, {"flight_no": "LH117", "departure_datetime": "2021-03-29T17:21:44.619712"}, {"flight_no": "LH114", "departure_datetime": "2021-04-03T18:40:44.619712"}, {"flight_no": "LH105", "departure_datetime": "2021-04-05T22:31:44.619712"}, {"flight_no": "LH103", "departure_datetime": "2021-04-17T15:24:44.619712"}]"""

# Welcome to LHIND's digital Easter egg hunt. 
# We are glad that you are curious and want to solve our Python puzzle. 
# Depending on your skills, the riddle will take about 30 to 60 minutes.
# Are you ready? We wish you good luck and Happy Easter.

# The riddle goes as follows:
# The airline code is not part of the easteregg.
# The remaining flight numbers sorted by departure date contain our easteregg encoded in unicode.
