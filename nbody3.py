"""
    N-body simulation.
    time=31.61249005121186s
"""

#PI = 3.14159265358979323
#SOLAR_MASS = 4 * 3.14159265358979323 * 3.14159265358979323
#DAYS_PER_YEAR = 365.24
'''
BODIES = {
    'sun': [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], 4 * 3.14159265358979323 * 3.14159265358979323],

    'jupiter': [[4.84143144246472090e+00,
                 -1.16032004402742839e+00,
                 -1.03622044471123109e-01],
                [1.66007664274403694e-03 * 365.24,
                 7.69901118419740425e-03 * 365.24,
                 -6.90460016972063023e-05 * 365.24],
                9.54791938424326609e-04 * 4 * 3.14159265358979323 * 3.14159265358979323],

    'saturn': [[8.34336671824457987e+00,
                4.12479856412430479e+00,
                -4.03523417114321381e-01],
               [-2.76742510726862411e-03 * 365.24,
                4.99852801234917238e-03 * 365.24,
                2.30417297573763929e-05 * 365.24],
               2.85885980666130812e-04 * 4 * 3.14159265358979323 * 3.14159265358979323],

    'uranus': [[1.28943695621391310e+01,
                -1.51111514016986312e+01,
                -2.23307578892655734e-01],
               [2.96460137564761618e-03 * 365.24,
                2.37847173959480950e-03 * 365.24,
                -2.96589568540237556e-05 * 365.24],
               4.36624404335156298e-05 * 4 * 3.14159265358979323 * 3.14159265358979323],

    'neptune': [[1.53796971148509165e+01,
                 -2.59193146099879641e+01,
                 1.79258772950371181e-01],
                [2.68067772490389322e-03 * 365.24,
                 1.62824170038242295e-03 * 365.24,
                 -9.51592254519715870e-05 * 365.24],
                5.15138902046611451e-05 * 4 * 3.14159265358979323 * 3.14159265358979323]}

'''
'''def compute_deltas(x1, x2, y1, y2, z1, z2):
    return (x1-x2, y1-y2, z1-z2)
    
def compute_b(m, dt, dx, dy, dz):
    mag = compute_mag(dt, dx, dy, dz)
    return m * mag

def compute_mag(dt, dx, dy, dz):
    return dt * ((dx * dx + dy * dy + dz * dz) ** (-1.5))'''

'''def update_vs(v1, v2, dt, dx, dy, dz, m1, m2):
    #v1[0] -= dx * compute_b(m2, dt, dx, dy, dz)
    #v1[0]-=dx*m2*compute_mag(dt,dx,dy,dz)
    v1[0]-=dx*m2*dt * ((dx * dx + dy * dy + dz * dz) ** (-1.5))
    v1[1]-=dy*m2*dt * ((dx * dx + dy * dy + dz * dz) ** (-1.5))
    #v1[1] -= dy * compute_b(m2, dt, dx, dy, dz)
    #v1[2] -= dz * compute_b(m2, dt, dx, dy, dz)
    v1[2]-=dz*m2*dt * ((dx * dx + dy * dy + dz * dz) ** (-1.5))
    #v2[0] += dx * compute_b(m1, dt, dx, dy, dz)
    v2[0]+=dx*m1*dt * ((dx * dx + dy * dy + dz * dz) ** (-1.5))
    #v2[1] += dy * compute_b(m1, dt, dx, dy, dz)
    v2[1]+=dy*m1*dt * ((dx * dx + dy * dy + dz * dz) ** (-1.5))
    #v2[2] += dz * compute_b(m1, dt, dx, dy, dz)
    v2[2]+=dz*m1*dt * ((dx * dx + dy * dy + dz * dz) ** (-1.5))'''
'''def update_rs(r, dt, vx, vy, vz):
    r[0] += dt * vx
    r[1] += dt * vy
    r[2] += dt * vz'''
'''
def advance(dt):
    '''
        #advance the system one timestep
'''
    for i in range(5):
        for j in range(i+1,5):
                ([x1, y1, z1], v1, m1) = BODIES[index[i]]
                ([x2, y2, z2], v2, m2) = BODIES[index[j]]
                (dx, dy, dz) = (x1-x2, y1-y2, z1-z2)
                #update_vs(v1, v2, dt, dx, dy, dz, m1, m2)
                v1[0]-=dx*m2*dt * pow((dx * dx + dy * dy + dz * dz),(-1.5))
                v1[1]-=dy*m2*dt * pow((dx * dx + dy * dy + dz * dz), (-1.5))
                v1[2]-=dz*m2*dt * pow((dx * dx + dy * dy + dz * dz), (-1.5))
                v2[0]+=dx*m1*dt * pow((dx * dx + dy * dy + dz * dz),(-1.5))
                v2[1]+=dy*m1*dt * pow((dx * dx + dy * dy + dz * dz),(-1.5))
                v2[2]+=dz*m1*dt * pow((dx * dx + dy * dy + dz * dz),(-1.5))
        
        
    for body in BODIES.keys():
        [r,[vx, vy, vz],m]= BODIES[body]
        #update_rs(r, dt, vx, vy, vz)
        r[0] += dt * vx
        r[1] += dt * vy
        r[2] += dt * vz'''

'''def compute_energy(m1, m2, dx, dy, dz):
    return (m1 * m2) / ((dx * dx + dy * dy + dz * dz) ** 0.5)'''
    
'''def report_energy(e=0.0):
    '''
        #compute the energy and return it so that it can be printed
        
'''
    index=[string for string in BODIES.keys()]
    for i in range(5):
        for j in range(i+1,5):
                ([x1, y1, z1], v1, m1) = BODIES[index[i]]
                ([x2, y2, z2], v2, m2) = BODIES[index[j]]
                e -= (m1 * m2) / pow(((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2), 0.5)
                
        
    for body in BODIES.keys():
        (r, [vx, vy, vz], m) = BODIES[body]
        e += m * (vx * vx + vy * vy + vz * vz) / 2.
     
    return e'''

'''def offset_momentum(ref, px=0.0, py=0.0, pz=0.0):
    '''
       # ref is the body in the center of the system
        #offset values from this reference
'''
    for body in BODIES.keys():
        (r, [vx, vy, vz], m) = BODIES[body]
        px -= vx * m
        py -= vy * m
        pz -= vz * m
        
    (r, v, m) = ref
    v[0] = px / m
    v[1] = py / m
    v[2] = pz / m'''


def nbody(loops, reference, iterations):
    '''
        nbody simulation
        loops - number of loops to run
        reference - body at center of system
        iterations - number of timesteps to advance
    '''
    BODIES = {
    'sun': [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], 4 * 3.14159265358979323 * 3.14159265358979323],

    'jupiter': [[4.84143144246472090e+00,
                 -1.16032004402742839e+00,
                 -1.03622044471123109e-01],
                [1.66007664274403694e-03 * 365.24,
                 7.69901118419740425e-03 * 365.24,
                 -6.90460016972063023e-05 * 365.24],
                9.54791938424326609e-04 * 4 * 3.14159265358979323 * 3.14159265358979323],

    'saturn': [[8.34336671824457987e+00,
                4.12479856412430479e+00,
                -4.03523417114321381e-01],
               [-2.76742510726862411e-03 * 365.24,
                4.99852801234917238e-03 * 365.24,
                2.30417297573763929e-05 * 365.24],
               2.85885980666130812e-04 * 4 * 3.14159265358979323 * 3.14159265358979323],

    'uranus': [[1.28943695621391310e+01,
                -1.51111514016986312e+01,
                -2.23307578892655734e-01],
               [2.96460137564761618e-03 * 365.24,
                2.37847173959480950e-03 * 365.24,
                -2.96589568540237556e-05 * 365.24],
               4.36624404335156298e-05 * 4 * 3.14159265358979323 * 3.14159265358979323],

    'neptune': [[1.53796971148509165e+01,
                 -2.59193146099879641e+01,
                 1.79258772950371181e-01],
                [2.68067772490389322e-03 * 365.24,
                 1.62824170038242295e-03 * 365.24,
                 -9.51592254519715870e-05 * 365.24],
                5.15138902046611451e-05 * 4 * 3.14159265358979323 * 3.14159265358979323]}


    # Set up global state
    #offset_momentum(BODIES[reference])
    [px,py,pz]=[0.0,0.0,0.0]
    for body,item in BODIES.items():
        (r, [vx, vy, vz], m_) = item
        [px,py,pz]=list(map(lambda x,y:y-x*m_,[vx,vy,vz],[px,py,pz]))
        

    (r, v, m) = BODIES[reference]
    v[0] = px / m
    v[1] = py / m
    v[2] = pz / m

    pairs = []
    seenit = set()

    for body1 in BODIES.keys():
        for body2 in BODIES.keys():
            if not (body2 in seenit) and (body1 != body2):
                pairs.append((body1, body2))
                seenit.add(body1)
    
    for _ in range(loops*iterations):
        #report_energy
        for (body1, body2) in pairs:
                ([x1, y1, z1], v1, m1) = BODIES[body1]
                ([x2, y2, z2], v2, m2) = BODIES[body2]
                (dx, dy, dz) = (x1-x2, y1-y2, z1-z2)
                temp=0.01 * pow((dx * dx + dy * dy + dz * dz),(-1.5))
                v1[0]-=dx*m2*temp
                v1[1]-=dy*m2*temp
                v1[2]-=dz*m2*temp
                v2[0]+=dx*m1*temp
                v2[1]+=dy*m1*temp
                v2[2]+=dz*m1*temp
        for body,item in BODIES.items():
                [r,[vx, vy, vz],m]= item
                #update_rs(r, dt, vx, vy, vz)
                r[0] += 0.01 * vx
                r[1] += 0.01 * vy
                r[2] += 0.01 * vz
        if (_ % iterations==0 and _ >0):
            e=0.0
            for (body1, body2) in pairs:
                ((x1, y1, z1), v1, m1) = BODIES[body1]
                ((x2, y2, z2), v2, m2) = BODIES[body2]
                (dx, dy, dz) = (x1-x2, y1-y2, z1-z2)
                e -= (m1 * m2) / pow((dx * dx + dy * dy + dz * dz), 0.5)
            for body in BODIES.keys():
                (r, [vx, vy, vz], m) = BODIES[body]
                e += m * (vx **2 + vy**2 + vz**2) / 2
            print(e)

if __name__ == '__main__':
    import timeit
    print(timeit.timeit(lambda:nbody(100, 'sun', 20000), number=1))
