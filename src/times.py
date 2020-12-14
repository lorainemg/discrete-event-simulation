from distributions import exponential, normal, bernoulli

def arrival_time(lambd):
    return exponential(lambd)

def landing_time():
    return normal(10, 5)

def takeoff_time():
    return normal(10, 5)

def load():
    return bernoulli(0.5)

def unload():
    return bernoulli(0.5)

def loading_time():
    return exponential(30)

def unloading_time():
    return exponential(30)

def broke():
    return bernoulli(0.1)

def fix_time():
    return exponential(15)

def recharge_time():
    return exponential(30)

def departure_time():
    time = landing_time()
    
    rechargetime = recharge_time()
    unloadingtime = unloading_time() if unload() else 0
    loadingtime = loading_time() if load() else 0
    fixtime = fix_time() if broke() else 0
    
    time += max(rechargetime, loadingtime)
    time += max(unloadingtime, fixtime)
    time += takeoff_time()
    return time
    