import unittest
import random
from solution import rewind_combo
from queue import SimpleQueue


class TestCodingChallenge7(unittest.TestCase):

    def test_basic(self):

        test1 = [4, 6, 3, 9, 7, 10]
        expected = [None, 4, None, 6, 6, 9]
        actual = rewind_combo(test1)
        self.assertEqual(actual, expected)

        test2 = [5, 2, 6, 0, 12, 3, 1]
        expected = [None, None, 5, None, 6, 2, 0]
        actual = rewind_combo(test2)
        self.assertEqual(actual, expected)

        test3 = [3, 4, 2, 0, 1, 5]
        expected = [None, 3, None, None, 0, 4]
        actual = rewind_combo(test3)
        self.assertEqual(actual, expected)

    def test_worst_case(self):

        test1 = [2, 4, 7, 8, 9, 11, 14]
        expected = [None, 2, 4, 7, 8, 9, 11]
        actual = rewind_combo(test1)
        self.assertEqual(actual, expected)

        test2 = [13, 10, 8, 7, 6, 3, 1]
        expected = [None, None, None, None, None, None, None]
        actual = rewind_combo(test2)
        self.assertEqual(actual, expected)

    def test_best_case(self):

        test1 = [8, 4, 10, 1, 5, 9, 15]
        expected = [None, None, 8, None, 4, 8, 10]
        actual = rewind_combo(test1)
        self.assertEqual(actual, expected)

        test2 = [12, 15, 5, 8, 17, 14, 0]
        expected = [None, 12, None, 5, 15, 12, None]
        actual = rewind_combo(test2)
        self.assertEqual(actual, expected)

    def test_small_comprehensive(self):

        random.seed(331)

        test1 = [18, 14, 15, 27, 26, 7, 13, 16, 28, 3, 12, 23, 21, 4, 24, 22, 29, 5, 9, 6, 19]
        expected = [None, None, 14, 18, 18, None, 7, 15, 27, None, 7, 18, 18, 3, 23, 21, 28, 4, 7, 5, 18]
        actual = rewind_combo(test1)
        self.assertEqual(actual, expected)

        test2 = random.sample(range(3, 31), 21)
        expected = [None, None, None, None, 8, 13, None, 23, 13, 13, 26, 13, 18, 13, 19, 13, 10, 8, None, 19, 6]
        actual = rewind_combo(test2)
        self.assertEqual(actual, expected)

        test3 = sorted(random.sample(range(3, 31), 21), reverse=True)
        expected = [None] * 21
        actual = rewind_combo(test3)
        self.assertEqual(actual, expected)

    def test_large_comprehensive(self):

        random.seed(331)

        test1 = random.sample(range(3, 3121), 1000)
        expected = [None, None, None, 704, 1318, None, 2591, 1318,
                    1318, 1951, 2658, 1318, 1951, 2719, 3000, 1379, 2719, 1708,
                    2728, 2391, 1708, None, 1772, 1951, 1018, 1951, 2974, 2391, 1318,
                    1379, 2157, 2719, 704, 3058, 426, 1160, 2505, 2391, 593, 168,
                    2728, 2229, 2552, 1379, 3000, 1018, 2157, 1951, 2825, 1951,
                    3061, None, 2591, 2865, 1777, 95, 2658, 426, 1918, 2069, 2220,
                    2157, 3010, 704, 336, 1160, 2728, 1951, 137, 3099, 137, 2229, 2728, 150, 781, 2452, 2803, 2895, 1285, 1379, 1018, 3109, 803, 704, 1977, 168, 593, 1465, 855, 426, 3115, 2825, 945, 151, 95, 1160, 1170, 602, 2091, 602, 2728, 3061, 803, 168, 137, 1825, 2505, 2670, 426, 2976, 2728, 2658, 96, 1018, 2229, 803, 1318, 152, 1977, 2666, 2069, 426, 2289, 593, 435, 3037, 2172, 1863, 1136, 2091, 2391, 2071, 168, 2091, 1188, 1031, 1825, 2505, 2404, 1415, 1072, 1519, 1772, 1318, 336, 1569, 2511, 2591, 1775, 1356, 2123, 1777, 2443, 3099, 1072, 532, 945, 2911, 657, 1918, 1211, 1417, 564, 1031, 3071, 1922, 144, 2291, 205, 1417, 1569, 657, 2291, 96, 2511, 1922, 995, 128, 860, 1798, 2172, 3010, 2865, 1576, 1798, 2404, 945, 1052, 1847, 2895, 2911, 469, 564, 1642, 2311, 2291, 2091, 1825, 1719, 267, 1576, 279, 626, 1285, 1293, None, 1417, 469, 1569, 2412, 285, 1777, 2976, 2731, 1519, 1143, 1798, 1465, 1519, 873, 1268, 2452, 1782, 860, 2413, 2229, 152, 205, 365, 2515, 2311, 2463, 1977, 569, 1170, 2423, 336, 187, 1674, 1753, 1261, 2313, 1188, 1825, 826, 2670, 1977, 2157, 1379, 2311, 285, 2515, 3100, 999, 1951, 215, 1992, 1485, 2205, 2911, 502, 649, 2452, 2249, 42, 1874, 2413, 2915, 232, 435, 1399, 626, 2333, 2658, 1538, 2744, 2092, 3092, 2511, 596, 1204, 96, 693, 2054, 1678, 1205, 1576, 1992, 1442, 2083, 1719, 3109, 1620, 2313, 2333, 2380, 152, 2949, 1446, 1327, 3101, 945, 96, 1918, 2445, 2092, 1890, 1072, 1211, 1072, 3109, 1188, 285, 267, 1874, 1005, 781, 279, 1545, 1465, 463, 690, 707, 2911, 1523, 1097, 215, 2054, 2552, 1847, 42, 3047, 2313, 2160, 236, 1739, 1941, 1379, 1005, 285, 1992, 1211, 426, 1890, 2895, 3019, 285, 2825, 2208, 2229, 524, 1427, 365, 1108, 300, 1922, 2391, 1399, 873, 3104, 1406, 2603, 803, 1576, 2463, 1446, 240, 826, 860, 1739, 2794, 469, 2465, 1285, 2564, 532, 2139, 502, 2861, 2667, 193, 1678, 1160, 719, 2229, 1977, 2004, 1401, 2744, 119, 380, 1951, 1669, 380, 1356, 707, 1946, 2552, 515, 2343, 2035, 1571, 573, 478, 2763, 83, 1467, 1955, 2603, 963, 2465, 337, 2391, None, 719, 834, 1261, 1739, 3071, 1834, 1992, 1195, 1965, 573, 337, 2803, None, 2552, 1525, 748, 42, 719, 435, 2249, 647, 707, 781, 2333, 2981, 759, 2343, 925, 124, 2026, 593, 2073, 690, 861, 2539, 2416, 3047, 170, 1854, 1918, 1097, 2731, 2471, 681, 1628, 3037, 2447, 2229, 1195, 1379, 1580, 1642, 2465, 102, 1418, 2483, 365, 1674, 1719, 1211, 2810, 989, 892, 45, 1919, 3073, None, 2622, 1994, 1760, 1955, 1125, 1761, 486, 532, 435, 1874, 1105, 748, 137, 657, 2515, 21, 1136, 1983, 2291, 1293, 781, 1215, 2230, 761, 267, 3000, 3019, 1242, 436, 2358, 1131, 1977, 480, 2862, 2719, 2670, 1545, 2075, 1996, 488, 390, 1072, 2094, 1170, 1195, 140, 845, 240, 1576, 2118, 2842, 602, 65, 1761, 1678, 2491, 2605, 1580, 21, 2825, 2636, 2917, 713, 285, 1110, 1951, 480, 2174, 326, 892, 949, 2773, 659, 1533, 2123, 1896, 1170, 1268, 1708, 1427, 1224, 1244, 1452, 956, 1072, 2670, 1018, 1097, 873, 1379, 1031, 2249, 240, 2987, 1533, 2813, 2182, 2932, 119, 1580, 2672, 2765, 2902, 45, 1890, 1290, 952, 1224, 2570, 2976, 792, 102, 906, 1467, 499, 2271, 2404, 1415, 1477, 579, 1371, 911, 365, 1118, 1590, 314, 440, 253, 532, 2340, 1863, 1969, 2816, 1708, 242, 57, 3010, 2607, 2102, 2539, 2867, 2257, 2622, 242, 1336, 1052, 1088, 1379, 2552, 31, 2843, 1653, 2427, 2767, 1344, 96, 1628, 1546, 1110, 365, 70, 1494, 2828, 2540, 2959, 917, 1406, 3111, 1406, 999, 2571, 2607, 337, 759, 873, 2571, 2094, 2358, 2768, 2591, 1245, 2278, 1653, 845, 1005, 2982, 1031, 1896, 1766, 1678, 1674, 174, 3061, 2278, 2485, None, 1494, 2843, 2591, 174, 70, 464, 719, 2736, 1494, None, 1248, 626, 2231, 2868, 517, 991, 1692, 2687, 502, 1886, 2075, 963, 2139, 215, 426, 927, 1810, 2959, 253, 2905, 2687, 2358, 203, 1178, 390, 1928, 140, 1467, 587, 1072, 1719, 2871, 1659, 395, 2077, 291, 662, 293, 1344, 35, 917, 305, 256, 215, 464, 714, 138, 1356, 1834, 1590, 2333, 504, 2638, 1928, 2515, 2026, 3073, 727, 2004, 1753, 1986, 834, 870, 2433, 2843, 165, 1305, 310, 440, 532, 1719, 602, 1313, 976, 3115, 1708, 285, 217, 1429, 1272, 180, 1485, 2723, 2452, 1552, 1630, 2281, 1525, 408, 2140, 1472, 1436, 602, 31, 254, 742, 410, 2295, 808, 358, 892, 272, 1620, 2035, 358, 1739, 1546, 2409, 205, 193, 2485, 1483, 931, 2073, 1863, 2343, 2496, 963, 2298, 1371, 2103, 1494, 410, 727, 3111, 1937, 2708, 963, 1724, 1293, 314, 2249, 2191, 686, 74, 2213, 2741, 3010, 1900, 1494, 1823, 465, 2803, 295, 1232, 3050, 1166, 2949, 602, 338, 2056, 544, 455, 3013, 626, 1630, 3028, 892, 2496, 2371, 2300, 1250, 107, 1682, 2291, 2291, 2731, 1125, 2818, 58, 45, 2295, 984, 184, 262, None, 564, 1762, 1147, 116, 649, 2932, 2736, 338, 882, 1155, 205, 681, 1261, 2238, 2744, 31, 2618, 3061, 2622, 1118, 1692, 2259, 2591, 2298, 970, 338, 410, 2282, 2429, 1206, 629, 1225, 2201, 2397, 2496, 826, 1467, 1623, 1108, 2123, 2871, 1018, 2182, 2577, 1727, 1825, 579, 2004, 2377, 2416, 942, 279, 1447, 943, 1336, 2881, 2843, 2085, 1344, 873, 1182, 1232, 1692, 812, 2344, 1874, 1787, 1662, 2609, 2150, 2825, 613, 488, 2990, 367, 455, 796, 768, 49, 2582, 1179, 2638, 1295, 785, 3019, 3003, 569, 3063, 280, 51, 2172, 3084, 3, 849, 1754, 2552, 719, 1768, 594, 1336, 3086, 2324, 999, 1947, 422, 579, 1599, 3025, 65, 3026, 1287, 1195, 1560, 1157, 1653, 2524, 70, 2471, 2423, 1007, 2917, 2593, 2976, 314, 1901, 2524, 2191, 693, 3050, 257, 369, 786, 2609, 1110, 1705, 931, 349]
        actual = rewind_combo(test1)
        self.assertEqual(actual, expected)

        test2 = sorted(random.sample(range(3, 3121), 900))
        expected = [None, 9, 16, 19, 20, 23, 24, 26, 31, 33, 34, 42, 45, 46,
                    52, 55, 58, 59, 61, 63, 65, 66, 69, 71, 75, 80, 81, 82, 84,
                    85, 86, 89, 90, 91, 93, 98, 99, 100, 101, 103, 107, 114, 115,
                    117, 118, 120, 124, 128, 130, 131, 136, 138, 140, 142, 144, 147,
                    149, 152, 154, 165, 166, 169, 171, 176, 178, 179, 184, 187, 188,
                    189, 191, 192, 193, 196, 198, 211, 215, 216, 218, 219, 224, 225,
                    227, 237, 238, 244, 254, 258, 269, 277, 278, 280, 286, 288, 293, 296, 299, 302, 306, 309, 314, 315, 323, 328, 329, 336, 344, 346, 351, 356, 357, 359, 360, 363, 365, 366, 367, 374, 380, 383, 384, 385, 398, 403, 404, 407, 419, 421, 424, 427, 436, 442, 443, 446, 447, 449, 452, 458, 463, 470, 481, 482, 491, 497, 501, 505, 506, 508, 512, 514, 515, 516, 523, 524, 525, 527, 530, 531, 532, 544, 550, 552, 557, 561, 562, 568, 578, 585, 587, 590, 591, 595, 599, 602, 604, 605, 610, 611, 613, 614, 618, 623, 624, 625, 626, 627, 630, 632, 633, 635, 637, 638, 641, 644, 647, 648, 649, 651, 654, 657, 662, 665, 667, 671, 672, 673, 676, 678, 681, 688, 690, 691, 698, 699, 710, 712, 714, 725, 726, 727, 728, 730, 732, 743, 746, 753, 755, 763, 772, 776, 779, 783, 791, 800, 801, 803, 814, 817, 818, 819, 821, 824, 825, 830, 833, 836, 837, 845, 846, 849, 851, 854, 863, 871, 873, 878, 883, 884, 885, 891, 892, 895, 899, 903, 904, 912, 915, 917, 920, 921, 923, 934, 938, 943, 944, 947, 948, 949, 950, 954, 955, 956, 959, 961, 963, 965, 967, 968, 971, 973, 974, 981, 984, 986, 987, 994, 1002, 1006, 1010, 1015, 1023, 1024, 1025, 1028, 1031, 1039, 1040, 1042, 1049, 1056, 1057, 1069, 1071, 1072, 1073, 1075, 1079, 1081, 1089, 1093, 1095, 1099, 1104, 1106, 1107, 1109, 1112, 1117, 1118, 1123, 1124, 1125, 1126, 1127, 1130, 1131, 1136, 1139, 1142, 1151, 1155, 1156, 1159, 1161, 1165, 1173, 1177, 1184, 1185, 1186, 1187, 1203, 1208, 1228, 1229, 1230, 1231, 1241, 1244, 1245, 1253, 1257, 1258, 1277, 1278, 1280, 1286, 1289, 1290, 1292, 1294, 1299, 1302, 1313, 1314, 1315, 1317, 1319, 1325, 1326, 1330, 1331, 1332, 1333, 1338, 1348, 1355, 1358, 1363, 1366, 1368, 1369, 1371, 1374, 1377, 1380, 1383, 1387, 1393, 1407, 1417, 1418, 1420, 1421, 1422, 1425, 1427, 1428, 1433, 1434, 1435, 1438, 1445, 1450, 1454, 1457, 1458, 1461, 1466, 1467, 1470, 1477, 1480, 1482, 1483, 1488, 1489, 1497, 1498, 1500, 1503, 1505, 1517, 1519, 1521, 1526, 1537, 1541, 1545, 1547, 1548, 1551, 1553, 1554, 1557, 1558, 1560, 1561, 1572, 1573, 1578, 1581, 1583, 1585, 1588, 1589, 1592, 1599, 1602, 1603, 1606, 1609, 1611, 1614, 1626, 1627, 1630, 1633, 1634, 1635, 1636, 1639, 1641, 1642, 1645, 1651, 1657, 1665, 1669, 1670, 1672, 1679, 1682, 1683, 1685, 1686, 1689, 1699, 1700, 1701, 1708, 1716, 1719, 1722, 1723, 1724, 1727, 1732, 1738, 1740, 1747, 1750, 1755, 1756, 1770, 1771, 1772, 1773, 1775, 1777, 1778, 1779, 1780, 1781, 1786, 1787, 1788, 1789, 1794, 1796, 1798, 1804, 1812, 1813, 1815, 1823, 1824, 1830, 1834, 1837, 1838, 1841, 1843, 1845, 1847, 1848, 1850, 1854, 1855, 1878, 1884, 1885, 1887, 1888, 1903, 1908, 1911, 1912, 1918, 1920, 1925, 1926, 1927, 1930, 1932, 1939, 1941, 1942, 1943, 1953, 1971, 1975, 1987, 1993, 1996, 2002, 2003, 2007, 2011, 2013, 2017, 2020, 2029, 2030, 2032, 2034, 2035, 2038, 2041, 2046, 2050, 2052, 2054, 2059, 2061, 2063, 2070, 2071, 2087, 2088, 2089, 2091, 2098, 2103, 2105, 2106, 2108, 2112, 2118, 2120, 2137, 2151, 2157, 2162, 2168, 2170, 2171, 2173, 2175, 2176, 2177, 2180, 2181, 2186, 2196, 2200, 2208, 2212, 2213, 2214, 2217, 2219, 2222, 2225, 2226, 2228, 2230, 2234, 2235, 2240, 2247, 2249, 2252, 2253, 2254, 2258, 2260, 2268, 2270, 2271, 2274, 2277, 2279, 2282, 2284, 2290, 2293, 2296, 2300, 2301, 2302, 2303, 2304, 2308, 2315, 2318, 2320, 2323, 2332, 2333, 2334, 2340, 2344, 2346, 2350, 2351, 2353, 2357, 2358, 2360, 2368, 2381, 2382, 2387, 2388, 2391, 2395, 2397, 2398, 2400, 2405, 2407, 2411, 2414, 2417, 2419, 2421, 2426, 2427, 2428, 2430, 2434, 2435, 2437, 2438, 2442, 2445, 2446, 2448, 2451, 2455, 2461, 2462, 2464, 2467, 2469, 2474, 2477, 2479, 2488, 2491, 2504, 2507, 2509, 2516, 2523, 2525, 2527, 2529, 2535, 2536, 2540, 2543, 2545, 2548, 2553, 2554, 2555, 2561, 2564, 2572, 2574, 2575, 2576, 2584, 2587, 2589, 2590, 2592, 2594, 2595, 2598, 2605, 2606, 2609, 2616, 2617, 2618, 2619, 2624, 2625, 2630, 2641, 2643, 2644, 2645, 2650, 2651, 2654, 2656, 2657, 2663, 2665, 2666, 2667, 2674, 2681, 2682, 2684, 2685, 2688, 2694, 2701, 2703, 2705, 2706, 2707, 2709, 2710, 2711, 2716, 2718, 2723, 2729, 2731, 2732, 2735, 2740, 2743, 2757, 2758, 2767, 2769, 2770, 2771, 2772, 2778, 2784, 2788, 2790, 2791, 2794, 2796, 2797, 2799, 2801, 2808, 2810, 2819, 2822, 2823, 2824, 2825, 2826, 2831, 2832, 2833, 2835, 2840, 2842, 2849, 2853, 2854, 2855, 2858, 2859, 2863, 2864, 2866, 2868, 2872, 2880, 2885, 2891, 2893, 2895, 2898, 2900, 2903, 2907, 2910, 2915, 2920, 2921, 2925, 2937, 2942, 2943, 2946, 2949, 2950, 2952, 2954, 2955, 2958, 2963, 2964, 2966, 2969, 2974, 2977, 2983, 2986, 2988, 2994, 2998, 2999, 3002, 3007, 3015, 3016, 3024, 3025, 3027, 3030, 3031, 3032, 3033, 3034, 3039, 3042, 3049, 3050, 3052, 3053, 3054, 3061, 3065, 3068, 3071, 3072, 3084, 3090, 3092, 3094, 3107, 3108, 3109, 3113, 3117]
        actual = rewind_combo(test2)
        self.assertEqual(actual, expected)

    def test_run_time_no_points(self):
        """ if you pass this, you still need to check with Mimir running time """
        def generateBestCaseArray(array):
            """ Generates best case scenario input for algorithm! """
            bestCase = list()
            if array:
                queue = SimpleQueue()
                queue.put((0, len(array) - 1))
                while not queue.empty():
                    start, end = queue.get()
                    mid = (start + end) // 2
                    bestCase.append(array[mid])
                    if start <= mid - 1:
                        queue.put((start, mid - 1))
                    if mid + 1 <= end:
                        queue.put((mid + 1, end))

            return bestCase

        # These should run in O(nlogn) time!
        test = [i for i in range(1000)]
        best = generateBestCaseArray(test)
        rewind_combo(best)

        test = [i for i in range(100000)]
        best = generateBestCaseArray(test)
        rewind_combo(best)


if __name__ == '__main__':
    unittest.main()
