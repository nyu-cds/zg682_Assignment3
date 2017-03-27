%%cython
'''The running time has been reduced to 8.16362965642395s
The time has been greatly decreased compared with the original optimized version which is 29.5s 
'''

cdef float PI= 3.14159265358979323 
cdef float SOLAR_MASS = 4 * PI * PI 
cdef float DAYS_PER_YEAR = 365.24

cdef dict BODIES = {
    'sun': ([0.0, 0.0, 0.0], [0.0, 0.0, 0.0], SOLAR_MASS),

    'jupiter': ([4.84143144246472090e+00,
                 -1.16032004402742839e+00,
                 -1.03622044471123109e-01],
                [1.66007664274403694e-03 * DAYS_PER_YEAR,
                 7.69901118419740425e-03 * DAYS_PER_YEAR,
                 -6.90460016972063023e-05 * DAYS_PER_YEAR],
                9.54791938424326609e-04 * SOLAR_MASS),

    'saturn': ([8.34336671824457987e+00,
                4.12479856412430479e+00,
                -4.03523417114321381e-01],
               [-2.76742510726862411e-03 * DAYS_PER_YEAR,
                4.99852801234917238e-03 * DAYS_PER_YEAR,
                2.30417297573763929e-05 * DAYS_PER_YEAR],
               2.85885980666130812e-04 * SOLAR_MASS),

    'uranus': ([1.28943695621391310e+01,
                -1.51111514016986312e+01,
                -2.23307578892655734e-01],
               [2.96460137564761618e-03 * DAYS_PER_YEAR,
                2.37847173959480950e-03 * DAYS_PER_YEAR,
                -2.96589568540237556e-05 * DAYS_PER_YEAR],
               4.36624404335156298e-05 * SOLAR_MASS),

    'neptune': ([1.53796971148509165e+01,
                 -2.59193146099879641e+01,
                 1.79258772950371181e-01],
                [2.68067772490389322e-03 * DAYS_PER_YEAR,
                 1.62824170038242295e-03 * DAYS_PER_YEAR,
                 -9.51592254519715870e-05 * DAYS_PER_YEAR],
                5.15138902046611451e-05 * SOLAR_MASS)}

from itertools import combinations
cdef list body_pairs=list(combinations(BODIES.keys(),2))

cdef void advance(float dt, int iterations, dict bodies=BODIES):
    cdef float mag
    cdef float m2r,m1r,x1,y1,z1,x2,y2,z2,vx,vy,vz
    cdef float dx,dy,dz
    cdef list v1,m1,v2,m2
    for i in range(iterations):
        for (body1, body2) in body_pairs:
            ([x1, y1, z1], v1, m1) = bodies[body1]
            ([x2, y2, z2], v2, m2) = bodies[body2]
            # unpack compute_deltas function
            (dx, dy, dz) = (x1-x2, y1-y2, z1-z2)
            # unpack update_vs/compute_b(m2, dt, dx, dy, dz) function
            mag=dt * ((dx * dx + dy * dy + dz * dz) ** (-1.5))
            m2r = m2 * mag
            m1r= m1 * mag
            v1[0] -= dx * m2r
            v1[1] -= dy * m2r
            v1[2] -= dz * m2r
            v2[0] += dx * m1r
            v2[1] += dy * m1r
            v2[2] += dz * m1r

        for content in bodies.values():
            (r, [vx, vy, vz], m) = content
            # unpack update_rs(r, dt, vx, vy, vz) function
            r[0] += dt * vx
            r[1] += dt * vy
            r[2] += dt * vz

cdef float report_energy(float e=0.0, dict bodies=BODIES, list pairs=body_pairs):
    cdef float x1, y1, z1,x2, y2, z2,m1,m2,vx, vy, vz,m
    cdef float dx,dy,dz
    cdef list v1,v2,r
    for (body1, body2) in pairs:
        ([x1, y1, z1], v1, m1) = bodies[body1]
        ([x2, y2, z2], v2, m2) = bodies[body2]
        # unpack compute_deltas function
        (dx, dy, dz) = (x1-x2, y1-y2, z1-z2)
        # unpack report_energy function
        e -= (m1 * m2) / ((dx ** 2 + dy ** 2 + dz ** 2) ** 0.5)

    for content in bodies.values():
        (r, [vx, vy, vz], m) = content
        e += m * (vx * vx + vy * vy + vz * vz) / 2.
        
    return e

cdef void nbody(int loops, str reference, int iterations, dict bodies=BODIES):
    # unpack offset_momentum function
    cdef float px=0.0,py=0.0,pz=0.0
    cdef float vx,vy,vz,m
    cdef list v,r,m_
    for content in bodies.values():
        (r, [vx, vy, vz], m_) = content
        [px, py, pz] = list(map(lambda x,y: y-x*m_, [vx,vy,vz],[px,py,pz]))#vectorV-m*vector
        
    (r, v, m) = bodies[reference]
    v[0] = px / m
    v[1] = py / m
    v[2] = pz / m
    

    for _ in range(loops):
        advance(0.01,iterations)
        print(report_energy())

if __name__ == '__main__':
    import timeit
    print(timeit.timeit(lambda:nbody(100, 'sun', 20000), number=1))

