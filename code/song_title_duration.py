song_times_1 = [
    ("Stairway to Heaven", "8:05"), ("Immigrant Song", "2:27"),
    ("Rock and Roll", "3:41"), ("Communication Breakdown", "2:29"),
    ("Good Times Bad Times", "2:48"), ("Hot Dog", "3:19"),
    ("The Crunge", "3:18"), ("Achilles Last Stand", "10:26"),
    ("Black Dog", "4:55")
]
song_times_2 = [
    ("Stairway to Heaven", "8:05"), ("Immigrant Song", "2:27"),
    ("Rock and Roll", "3:41"), ("Communication Breakdown", "2:29"),
    ("Good Times Bad Times", "2:48"), ("Black Dog", "4:55"),
    ("The Crunge", "3:18"), ("Achilles Last Stand", "10:26"),
    ("The Ocean", "4:31"), ("Hot Dog", "3:19"),
]
song_times_3 = [
    ("Stairway to Heaven", "8:05"), ("Immigrant Song", "2:27"),
    ("Rock and Roll", "3:41"), ("Communication Breakdown", "2:29"),
    ("Hey Hey What Can I Do", "4:00"), ("Poor Tom", "3:00"),
    ("Black Dog", "4:55")
]
song_times_4 = [
    ("Hey Hey What Can I Do", "4:00"), ("Rock and Roll", "3:41"),
    ("Communication Breakdown", "2:29"), ("Going to California", "3:30"),
    ("On The Run", "3:50"), ("The Wrestler", "3:50"), 
    ("Black Mountain Side", "2:00"), ("Black Dog", "4:55")
]
song_times_5 = [("Celebration Day", "3:30"), ("Going to California", "3:30")]
song_times_6 = [
  ("Rock and Roll", "3:41"), ("If I lived here", "3:59"),
  ("Day and night", "5:03"), ("Tempo song", "1:57")
]

from random import randint 
def min_to_sec(g :list):
    l=[]
    for i in g:
        l.append(list(i))
    for i in l:
        ms = i[1]
        msl = ms.split(':')
        s = (int(msl[0])*60)+int(msl[1])
        i[1] = s

    return l


def pairup(g :list):
    l = min_to_sec(g)
    rtrlst = []
    rtr = []
    for i in l:
        temp_lst = l
        temp_lst.remove(i)
        for g in temp_lst:
            if i[1]+g[1]==420:
                rtrlst.append([i[0],g[0]])

    try:
        rtr=rtrlst.pop(randint(0,len(rtrlst)-1)) 
    except:
        pass 
    return rtr          




print(pairup(song_times_2))