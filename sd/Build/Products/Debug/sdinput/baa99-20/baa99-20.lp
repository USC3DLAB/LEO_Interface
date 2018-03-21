\ENCODING=ISO-8859-1
\Problem name: baa99-20.mps

Minimize
 obj: 400 x1 + 380 x2 + 360 x3 + 340 x4 + 320 x5 + 300 x6 + 280 x7 + 260 x8
      + 240 x9 + 220 x10 + 200 x11 + 180 x12 + 160 x13 + 140 x14 + 120 x15
      + 100 x16 + 80 x17 + 60 x18 + 40 x19 + 20 x20 - 800 W1A - 760 W1B
      - 720 W1C - 680 W1D - 640 W1E - 600 W1F - 560 W1G - 520 W1H - 480 W1I
      - 440 W1J - 400 W1K - 360 W1L - 320 W1M - 280 W1N - 240 W1O - 200 W1P
      - 160 W1Q - 120 W1R - 80 W1S - 40 W1T - 760 W2B - 720 W2C - 680 W2D
      - 640 W2E - 600 W2F - 560 W2G - 520 W2H - 480 W2I - 440 W2J - 400 W2K
      - 360 W2L - 320 W2M - 280 W2N - 240 W2O - 200 W2P - 160 W2Q - 120 W2R
      - 80 W2S - 40 W2T - 720 W3C - 680 W3D - 640 W3E - 600 W3F - 560 W3G
      - 520 W3H - 480 W3I - 440 W3J - 400 W3K - 360 W3L - 320 W3M - 280 W3N
      - 240 W3O - 200 W3P - 160 W3Q - 120 W3R - 80 W3S - 40 W3T - 680 W4D
      - 640 W4E - 600 W4F - 560 W4G - 520 W4H - 480 W4I - 440 W4J - 400 W4K
      - 360 W4L - 320 W4M - 280 W4N - 240 W4O - 200 W4P - 160 W4Q - 120 W4R
      - 80 W4S - 40 W4T - 640 W5E - 600 W5F - 560 W5G - 520 W5H - 480 W5I
      - 440 W5J - 400 W5K - 360 W5L - 320 W5M - 280 W5N - 240 W5O - 200 W5P
      - 160 W5Q - 120 W5R - 80 W5S - 40 W5T - 600 W6F - 560 W6G - 520 W6H
      - 480 W6I - 440 W6J - 400 W6K - 360 W6L - 320 W6M - 280 W6N - 240 W6O
      - 200 W6P - 160 W6Q - 120 W6R - 80 W6S - 40 W6T - 560 W7G - 520 W7H
      - 480 W7I - 440 W7J - 400 W7K - 360 W7L - 320 W7M - 280 W7N - 240 W7O
      - 200 W7P - 160 W7Q - 120 W7R - 80 W7S - 40 W7T - 520 W8H - 480 W8I
      - 440 W8J - 400 W8K - 360 W8L - 320 W8M - 280 W8N - 240 W8O - 200 W8P
      - 160 W8Q - 120 W8R - 80 W8S - 40 W8T - 480 W9I - 440 W9J - 400 W9K
      - 360 W9L - 320 W9M - 280 W9N - 240 W9O - 200 W9P - 160 W9Q - 120 W9R
      - 80 W9S - 40 W9T - 440 W10J - 400 W10K - 360 W10L - 320 W10M - 280 W10N
      - 240 W10O - 200 W10P - 160 W10Q - 120 W10R - 80 W10S - 40 W10T
      - 400 W11K - 360 W11L - 320 W11M - 280 W11N - 240 W11O - 200 W11P
      - 160 W11Q - 120 W11R - 80 W11S - 40 W11T - 360 W12L - 320 W12M
      - 280 W12N - 240 W12O - 200 W12P - 160 W12Q - 120 W12R - 80 W12S
      - 40 W12T - 320 W13M - 280 W13N - 240 W13O - 200 W13P - 160 W13Q
      - 120 W13R - 80 W13S - 40 W13T - 280 W14N - 240 W14O - 200 W14P
      - 160 W14Q - 120 W14R - 80 W14S - 40 W14T - 240 W15O - 200 W15P
      - 160 W15Q - 120 W15R - 80 W15S - 40 W15T - 200 W16P - 160 W16Q
      - 120 W16R - 80 W16S - 40 W16T - 160 W17Q - 120 W17R - 80 W17S - 40 W17T
      - 120 W18R - 80 W18S - 40 W18T - 80 W19S - 40 W19T - 40 W20T + 20 v1
      + 20 v2 + 20 v3 + 20 v4 + 20 v5 + 20 v6 + 20 v7 + 20 v8 + 20 v9 + 20 v10
      + 20 v11 + 20 v12 + 20 v13 + 20 v14 + 20 v15 + 20 v16 + 20 v17 + 20 v18
      + 20 v19 + 20 v20 + 1000 uA + 950 uB + 900 uC + 850 uD + 800 uE + 750 uF
      + 700 uG + 650 uH + 600 uI + 550 uJ + 500 uK + 450 uL + 400 uM + 350 uN
      + 300 uO + 250 uP + 200 uQ + 150 uR + 100 uS + 50 uT
Subject To
 s1:  - x1 + W1A + W1B + W1C + W1D + W1E + W1F + W1G + W1H + W1I + W1J + W1K
      + W1L + W1M + W1N + W1O + W1P + W1Q + W1R + W1S + W1T + v1  = 0
 s2:  - x2 + W2B + W2C + W2D + W2E + W2F + W2G + W2H + W2I + W2J + W2K + W2L
      + W2M + W2N + W2O + W2P + W2Q + W2R + W2S + W2T + v2  = 0
 s3:  - x3 + W3C + W3D + W3E + W3F + W3G + W3H + W3I + W3J + W3K + W3L + W3M
      + W3N + W3O + W3P + W3Q + W3R + W3S + W3T + v3  = 0
 s4:  - x4 + W4D + W4E + W4F + W4G + W4H + W4I + W4J + W4K + W4L + W4M + W4N
      + W4O + W4P + W4Q + W4R + W4S + W4T + v4  = 0
 s5:  - x5 + W5E + W5F + W5G + W5H + W5I + W5J + W5K + W5L + W5M + W5N + W5O
      + W5P + W5Q + W5R + W5S + W5T + v5  = 0
 s6:  - x6 + W6F + W6G + W6H + W6I + W6J + W6K + W6L + W6M + W6N + W6O + W6P
      + W6Q + W6R + W6S + W6T + v6  = 0
 s7:  - x7 + W7G + W7H + W7I + W7J + W7K + W7L + W7M + W7N + W7O + W7P + W7Q
      + W7R + W7S + W7T + v7  = 0
 s8:  - x8 + W8H + W8I + W8J + W8K + W8L + W8M + W8N + W8O + W8P + W8Q + W8R
      + W8S + W8T + v8  = 0
 s9:  - x9 + W9I + W9J + W9K + W9L + W9M + W9N + W9O + W9P + W9Q + W9R + W9S
      + W9T + v9  = 0
 s10: - x10 + W10J + W10K + W10L + W10M + W10N + W10O + W10P + W10Q + W10R
      + W10S + W10T + v10  = 0
 s11: - x11 + W11K + W11L + W11M + W11N + W11O + W11P + W11Q + W11R + W11S
      + W11T + v11  = 0
 s12: - x12 + W12L + W12M + W12N + W12O + W12P + W12Q + W12R + W12S + W12T
      + v12  = 0
 s13: - x13 + W13M + W13N + W13O + W13P + W13Q + W13R + W13S + W13T + v13  = 0
 s14: - x14 + W14N + W14O + W14P + W14Q + W14R + W14S + W14T + v14  = 0
 s15: - x15 + W15O + W15P + W15Q + W15R + W15S + W15T + v15  = 0
 s16: - x16 + W16P + W16Q + W16R + W16S + W16T + v16  = 0
 s17: - x17 + W17Q + W17R + W17S + W17T + v17  = 0
 s18: - x18 + W18R + W18S + W18T + v18  = 0
 s19: - x19 + W19S + W19T + v19  = 0
 s20: - x20 + W20T + v20  = 0
 d1:  W1A + uA  = 100
 d2:  W1B + W2B + uB  = 100
 d3:  W1C + W2C + W3C + uC  = 100
 d4:  W1D + W2D + W3D + W4D + uD  = 100
 d5:  W1E + W2E + W3E + W4E + W5E + uE  = 100
 d6:  W1F + W2F + W3F + W4F + W5F + W6F + uF  = 100
 d7:  W1G + W2G + W3G + W4G + W5G + W6G + W7G + uG  = 100
 d8:  W1H + W2H + W3H + W4H + W5H + W6H + W7H + W8H + uH  = 100
 d9:  W1I + W2I + W3I + W4I + W5I + W6I + W7I + W8I + W9I + uI  = 100
 d10: W1J + W2J + W3J + W4J + W5J + W6J + W7J + W8J + W9J + W10J + uJ  = 100
 d11: W1K + W2K + W3K + W4K + W5K + W6K + W7K + W8K + W9K + W10K + W11K + uK
       = 100
 d12: W1L + W2L + W3L + W4L + W5L + W6L + W7L + W8L + W9L + W10L + W11L + W12L
      + uL  = 100
 d13: W1M + W2M + W3M + W4M + W5M + W6M + W7M + W8M + W9M + W10M + W11M + W12M
      + W13M + uM  = 100
 d14: W1N + W2N + W3N + W4N + W5N + W6N + W7N + W8N + W9N + W10N + W11N + W12N
      + W13N + W14N + uN  = 100
 d15: W1O + W2O + W3O + W4O + W5O + W6O + W7O + W8O + W9O + W10O + W11O + W12O
      + W13O + W14O + W15O + uO  = 100
 d16: W1P + W2P + W3P + W4P + W5P + W6P + W7P + W8P + W9P + W10P + W11P + W12P
      + W13P + W14P + W15P + W16P + uP  = 100
 d17: W1Q + W2Q + W3Q + W4Q + W5Q + W6Q + W7Q + W8Q + W9Q + W10Q + W11Q + W12Q
      + W13Q + W14Q + W15Q + W16Q + W17Q + uQ  = 100
 d18: W1R + W2R + W3R + W4R + W5R + W6R + W7R + W8R + W9R + W10R + W11R + W12R
      + W13R + W14R + W15R + W16R + W17R + W18R + uR  = 100
 d19: W1S + W2S + W3S + W4S + W5S + W6S + W7S + W8S + W9S + W10S + W11S + W12S
      + W13S + W14S + W15S + W16S + W17S + W18S + W19S + uS  = 100
 d20: W1T + W2T + W3T + W4T + W5T + W6T + W7T + W8T + W9T + W10T + W11T + W12T
      + W13T + W14T + W15T + W16T + W17T + W18T + W19T + W20T + uT  = 100
Bounds
 0 <= x1 <= 217
 0 <= x2 <= 217
 0 <= x3 <= 217
 0 <= x4 <= 217
 0 <= x5 <= 217
 0 <= x6 <= 217
 0 <= x7 <= 217
 0 <= x8 <= 217
 0 <= x9 <= 217
 0 <= x10 <= 217
 0 <= x11 <= 217
 0 <= x12 <= 217
 0 <= x13 <= 217
 0 <= x14 <= 217
 0 <= x15 <= 217
 0 <= x16 <= 217
 0 <= x17 <= 217
 0 <= x18 <= 217
 0 <= x19 <= 217
 0 <= x20 <= 217
End
