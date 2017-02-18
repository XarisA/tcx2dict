# tcx2dict

tcx2dict stores tcx data in a dictionary having a (#Lap,#measurement) tuple as a key.

Example:


MyDictionary= ttd().dict_data

print MyDictionary


Running: /home/xaris/bin/git/tcx2dict/tcx2dict/ttd.py (Sat Feb 18 17:40:10 2017)

`{(0, 1): ['2017-02-11T06:48:34.000Z', 3.760009765625, 87], (3, 35): ['2017-02-11T07:03:19.000Z', 3395.360107421875, 160], (4, 36): ['2017-02-11T07:07:46.000Z', 4291.8798828125, 167], (0, 76): ['2017-02-11T06:48:16.000Z', 382.6600036621094, 149], (4, 66): ['2017-02-11T07:08:54.000Z', 4519.06005859375, 168], (1, 64): ['2017-02-11T06:55:04.000Z', 1740.800048828125, 168], (2, 78): ['2017-02-11T07:00:54.000Z', 2913.080078125, 170], (0, 98): ['2017-02-11T06:49:02.000Z', 532.0800170898438, 147], (3, 86): ['2017-02-11T07:06:20.000Z', 4001.5400390625, 171]
...
}`


## Data Explanation:

`MyDictionary[0,1]` _returns data from 1st Lap , 2nd Measurement._

_['2017-02-11T06:48:34.000Z', 3.760009765625, 87]_

### _Get Datetime in isoformat_
`MyDictionary[0,1][0]`

_'2017-02-11T06:48:34.000Z'_

### _Get Distance_
`MyDictionary[0,1][1]`

_3.760009765625_

### _Get Heart Rate _
`MyDictionary[0,1][2]`

_87_
