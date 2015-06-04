## M3/mu (gluino/neutralino) grid for Run2 photon + jet analysis

import susyhitutils

at = 0
tanb = 1.5
msq = 5.0E+03

mum1_dict = {
    100: 816,
    110: 480,
    120: 363,
    130: 308,
    140: 282,
    150: 267,
    160: 259,
    170: 255,
    180: 254,
    190: 257,
    200: 259,
    210: 264,
    220: 269,
    230: 275,
    240: 282,
    250: 288,
    260: 296,
    270: 303,
    280: 311,
    290: 321,
    300: 328,
    310: 337,
    320: 346,
    330: 354,
    340: 363,
    350: 373,
    360: 381,
    370: 390,
    380: 400,
    390: 409,
    400: 419,
    410: 427,
    420: 437,
    430: 446,
    440: 456,
    450: 466,
    460: 476,
    470: 485,
    480: 495,
    490: 505,
    500: 515,
    510: 524,
    520: 534,
    530: 544,
    540: 554,
    550: 563,
    560: 573,
    570: 583,
    580: 593,
    590: 602,
    600: 612,
    610: 622,
    620: 632,
    630: 641,
    640: 651,
    650: 660,
    660: 670,
    670: 681,
    680: 691,
    690: 701,
    700: 711,
    710: 720,
    720: 730,
    730: 740,
    740: 750,
    750: 759,
    760: 769,
    770: 779,
    780: 789,
    790: 799,
    800: 809,
    810: 819,
    820: 830,
    830: 840,
    840: 850,
    850: 860,
    860: 869,
    870: 879,
    880: 889,
    890: 899,
    900: 908,
    910: 918,
    920: 928,
    930: 938,
    940: 949,
    950: 957,
    960: 968,
    970: 978,
    980: 987,
    990: 997,
    1000: 1007,
    1010: 1017,
    1020: 1027,
    1030: 1037,
    1040: 1047,
    1050: 1057,
    1060: 1068,
    1070: 1078,
    1080: 1088,
    1090: 1098,
    1100: 1107,
    1110: 1117,
    1120: 1127,
    1130: 1137,
    1140: 1146,
    1150: 1156,
    1160: 1166,
    1170: 1176,
    1180: 1185,
    1190: 1195,
    1200: 1205,
    1210: 1215,
    1220: 1226,
    1230: 1236,
    1240: 1246,
    1250: 1256,
    1260: 1265,
    1270: 1275,
    1280: 1285,
    1290: 1296,
    1300: 1306,
    1310: 1316,
    1320: 1326,
    1330: 1335,
    1340: 1345,
    1350: 1355,
    1360: 1365,
    1370: 1374,
    1380: 1384,
    1390: 1394,
    1400: 1404,
    1410: 1413,
    1420: 1423,
    1430: 1433,
    1440: 1443,
    1450: 1454,
    1460: 1464,
    1470: 1474,
    1480: 1482,
    1490: 1493,
    1500: 1503,
    1510: 1513,
    1520: 1523,
    1530: 1532,
    1540: 1542,
    1550: 1552,
    1560: 1562,
    1570: 1571,
    1580: 1581,
    1590: 1593,
    1600: 1603,
    1610: 1612,
    1620: 1622,
    1630: 1632,
    1640: 1642,
    1650: 1651,
    1660: 1661,
    1670: 1671,
    1680: 1681,
    1690: 1690,
    1700: 1700,
    1710: 1710,
    1720: 1720,
    1730: 1731,
    1740: 1739,
    1750: 1749,
    1760: 1759,
    1770: 1770,
    1780: 1780,
    1790: 1790,
    1800: 1800,
    1810: 1809,
    1820: 1819,
    1830: 1829,
    1840: 1839,
    1850: 1848,
    1860: 1858,
    1870: 1868,
    1880: 1878,
    1890: 1887,
    1900: 1899,
    1910: 1909,
    1920: 1918,
    1930: 1928,
    1940: 1938,
    1950: 1948,
    1960: 1957,
    1970: 1967,
    1980: 1977,
    1990: 1987,
    1036: 1044,
    1123: 1129,
    1209: 1215,
    1292: 1296,
    1375: 1379,
    1459: 1462,

    # diagonal
    1036: 1044,
    1123: 1129,
    1209: 1215,
    1292: 1296,
    1375: 1379,
    1459: 1462,
    1540: 1542,
    1623: 1624,
    1788: 1788,

}

# Nominal
# m3mu_dict = {
#     1000: [150, 200, 250, 350, 450, 550, 650, 750, 850, 950, 1036],
#     1100: [150, 200, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1123],
#     1200: [150, 200, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1209],
#     1300: [150, 200, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1292],
#     1400: [150, 200, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1375],
#     1500: [150, 200, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1459],
#     1600: [150, 200, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1540],
#     1700: [150, 200, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1623],
#     1800: [150, 200, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, ],
#     1900: [150, 200, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1788],
#     2000: [150, 200, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800],
# }

m3mu_dict = {
    1000: [150, 200, 250, 350, 450, 550, 650, 750, 850, 950, 1036],
    1100: [150, 200, 250, 350, 450, 550, 650, 750, 850, 950, 1050, 1123],
    1200: [150, 200, 250, 350, 450, 550, 650, 750, 850, 950, 1050, 1150, 1209],
    1300: [150, 200, 250, 350, 450, 550, 650, 750, 850, 950, 1050, 1150, 1250, 1292],
    1400: [150, 200, 250, 350, 450, 550, 650, 750, 850, 950, 1050, 1150, 1250, 1350, 1375],
    1500: [150, 200, 250, 350, 450, 550, 650, 750, 850, 950, 1050, 1150, 1250, 1350, 1459],
    1600: [150, 200, 250, 350, 450, 550, 650, 750, 850, 950, 1050, 1150, 1250, 1350, 1450, 1540],
    1700: [150, 200, 250, 350, 450, 550, 650, 750, 850, 950, 1050, 1150, 1250, 1350, 1450, 1550, 1623],
    1800: [150, 200, 250, 350, 450, 550, 650, 750, 850, 950, 1050, 1150, 1250, 1350, 1450, 1550, 1650, 1700, ],
    1900: [150, 200, 250, 350, 450, 550, 650, 750, 850, 950, 1050, 1150, 1250, 1350, 1450, 1550, 1650, 1750, 1788],
    2000: [150, 200, 250, 350, 450, 550, 650, 750, 850, 950, 1050, 1150, 1250, 1350, 1450, 1550, 1650, 1750, 1800],
}

#
# m3mu_dict = {
#     1000: [150, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1036],
#     1100: [150, 250, 350, 450, 550, 650, 750, 850, 950, 1050, 1123],
#     1200: [150, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1209],
#     1300: [150, 250, 350, 450, 550, 650, 750, 850, 950, 1050, 1150, 1250, 1292],
#     1400: [150, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1375],
#     1500: [150, 250, 350, 450, 550, 650, 750, 850, 950, 1050, 1150, 1250, 1350, 1450, 1459],
#     1600: [150, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1540],
#     1700: [150, 250, 350, 450, 550, 650, 750, 850, 950, 1050, 1150, 1250, 1350, 1450, 1550, 1600, 1623],
#     1800: [150, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, ],
#     1900: [150, 250, 350, 450, 550, 650, 750, 850, 950, 1050, 1150, 1250, 1350, 1450, 1550, 1650, 1750, 1788],
#     2000: [150, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800],
# }

# m3mu_dict = {
#     1000: [150, 200, 300, 500, 700,  900, 1036],
#     1050: [150, 200, 400, 600, 800, 1000, 1036],
#     1100: [150, 200, 300, 500, 700,  900, 1100, 1123],
#     1150: [150, 200, 400, 600, 800, 1000, 1123],
#     1200: [150, 200, 300, 500, 700,  900, 1100, 1200, 1209],
#     1250: [150, 200, 400, 600, 800, 1000, 1200, 1209],
#     1300: [150, 200, 300, 500, 700,  900, 1100, 1200, 1292],
#     1350: [150, 200, 400, 600, 800, 1000, 1200, 1292],
#     1400: [150, 200, 300, 500, 700,  900, 1100, 1300, 1375],
#     1450: [150, 200, 400, 600, 800, 1000, 1200, 1375],
#     1500: [150, 200, 300, 500, 700,  900, 1100, 1300, 1459],
#     1550: [150, 200, 400, 600, 800, 1000, 1200, 1400, 1459],
#     1600: [150, 200, 300, 500, 700,  900, 1100, 1300, 1500, 1540],
#     1650: [150, 200, 400, 600, 800, 1000, 1200, 1400, 1540],
#     1700: [150, 200, 300, 500, 700,  900, 1100, 1300, 1500, 1623],
#     1750: [150, 200, 400, 600, 800, 1000, 1200, 1400, 1600, 1623],
#     1800: [150, 200, 300, 500, 700,  900, 1100, 1300, 1500, 1700, ],
#     1850: [150, 200, 400, 600, 800, 1000, 1200, 1400, 1600, 1700, ],
#     1900: [150, 200, 300, 500, 700,  900, 1100, 1300, 1500, 1700, 1788],
#     1950: [150, 200, 400, 600, 800, 1000, 1200, 1400, 1600, 1788],
#     2000: [150, 200, 300, 500, 700,  900, 1100, 1300, 1500, 1700, 1800],
#     2050: [150, 200, 400, 600, 800, 1000, 1200, 1400, 1600, 1800],
# }


run_dir = 'run2grid_slha_strong'

susyhitutils.create_run_directory(run_dir)

for m3, mulist in m3mu_dict.iteritems():

    for mu in mulist:

        # Gravitino mass
        Gmass = 1E-09 + ((1E-07 - 1E-09)/(float(m3)-150))*(float(mu)-150)

        m1 = mum1_dict.get(mu)

        outfile = 'susy_GGM_M3_mu_%s_%s.slha' % (m3, mu)

        susyhitutils.generate_slha(at, tanb, msq, m3, m1, mu, Gmass, outfile=outfile)

        print outfile

susyhitutils.clean_run_directory()



## EWK grid

m3 = 5E+03
mu_list = [150, 200, 250, 350, 450, 550, 650, 750, 850, 950, 1050, 1150, 1250, 1350, 1450, 1550, 1650, 1750, 1800]

run_dir = 'run2grid_slha_ewk'

susyhitutils.create_run_directory(run_dir)

for mu in mu_list:

    # Gravitino mass
    Gmass = 1E-09 + ((1E-07 - 1E-09)/(float(m3)-150))*(float(mu)-150)

    m1 = mum1_dict.get(mu)

    outfile = 'susy_GGM_mu_%s.slha' % mu

    susyhitutils.generate_slha(at, tanb, msq, m3, m1, mu, Gmass, outfile=outfile)

    print outfile

susyhitutils.clean_run_directory()