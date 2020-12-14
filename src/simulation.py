from times import arrival_time, departure_time
from random import shuffle

MAX_TIME = 99999999999
DURATION = 10080


def shuffle_tracks():
    tracks = list(range(5))
    shuffle(tracks)
    return tracks

def simulate(arriv_param, shuffle=True):
    # ss = [0]*6          # [customers in the system, wich are in any of the landing tracks]
    n = 0
    occupied = [False]*5
    
    arrival_times = []
    departure_times = []

    unoccupied_time = [0]*5
    last_occupied_time = [0]*5

    times = [MAX_TIME]*5
    next_arrival = arrival_time(arriv_param) 
    t = 0

    while t < DURATION:
        if next_arrival <= min(times):
            t = next_arrival
            next_arrival = t + arrival_time(arriv_param)
            arrival_times.append(t)

            if shuffle:
                tracks = shuffle_tracks()
            else:
                tracks = range(5)
            for i in tracks:
                if not occupied[i]:
                    occupied[i] = True
                    times[i] = t + departure_time()
                    unoccupied_time[i] += t - last_occupied_time[i]
                    break
            else:
                n += 1
        else:
            if shuffle:
                tracks = shuffle_tracks()
            else:
                tracks = range(5)
            for i in tracks:
                if next_arrival > times[i] and occupied[i]:
                    occupied[i] = False
                    ti = times[i]
                    times[i] = MAX_TIME
                    t = max(t, ti) 
                    last_occupied_time[i] = t

                    if n > 0:
                        visited = True
                        n -= 1
                        occupied[i] = True
                        unoccupied_time[i] += t - last_occupied_time[i]
                        times[i] = t + departure_time()
    return unoccupied_time
                    
def get_results(arriv_param, shuffle):
    lines = []
    accum = {}
    for i in range(30):
        lines.append('-----------------------------\n')
        lines.append(f'Simulation {i}\n')
        unoccupied_time = simulate(arriv_param, shuffle)
        for track, time in enumerate(unoccupied_time):
            time = round(time, 4)
            lines.append(f'Avarage time for track {track}: {time}\n')
            try:
                accum[track] += time
            except:
                accum[track] = time
    lines.append('==============================\n')
    for track, avarege_time in accum.items():
        avarege_time = avarege_time / 30
        avarege_time = round(avarege_time, 4)
        lines.append(f'Total avarage time for track {track}: {avarege_time}\n')
    with open(f'simulation({arriv_param})({shuffle}).txt', 'w+') as fp:
        fp.writelines(lines)

if __name__ == "__main__":
    get_results(20, False)
    get_results(1/20, False)
    get_results(1/20, True)
    # unoccupied_time = simulate()
    # print('Tiempo total de desocupación de cada una de las pistas')
    # for i, time in enumerate(unoccupied_time):
    #     print(f'Pista {i}: {time}')