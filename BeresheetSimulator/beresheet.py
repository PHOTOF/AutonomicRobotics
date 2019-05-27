import math
import matplotlib.pyplot as plt

# Moon variables
MOON_RADIUS = 3475 * 1000  # meters
MOON_ACC = 1.622  # m / s ^ 2
EQ_SPEED = 1700  # m / s
WEIGHT_EMP = 165  # kg
WEIGHT_FULE = 420  # kg
WEIGHT_FULL = WEIGHT_EMP + WEIGHT_FULE  # kg
MAIN_ENG_F = 430  # N
SECOND_ENG_F = 25  # N
MAIN_BURN = 0.15  # liter per sec, 12 liter per m'
SECOND_BURN = 0.009  # liter per sec 0.6 liter per m'
ALL_BURN = MAIN_BURN + 8 * SECOND_BURN

def get_acc(speed):
    n = abs(speed) / EQ_SPEED
    ans = (1 - n) * MOON_ACC
    return ans

def acc_max(weight):
    return acc(weight, True, 8)


def acc(weight, main, seconds):
    t = 0
    if main:
        t += MAIN_ENG_F
    t += seconds * SECOND_ENG_F
    ans = t / weight
    return ans


x = []
y = []
z = []

# starting point:
verticalSpeed = 24.8
horizontalSpeed = 932
ang = 58.3  # zero is vertical (as in landing)
alt = 13748  # 2:25:40 (as in the simulation) # https:#www.youtube.com/watch?v=JJ0VfRL9AMs
time = 0
dt = 1  # sec
acceleration = 0  # Acceleration rate (m/s^2)
fuel = 121  #
weight = WEIGHT_EMP + fuel
print("time, vertical speed, horizontal speed, altitude, angle, weight, acc")
NN = 0.7  # rate[0,1]
dist = 1
# ***** main simulation loop ******
while alt > 0:
    # make up some data
    x.append(0 - dist)
    y.append(alt)
    z.append(verticalSpeed)

    if time % 10 == 0 or alt < 100:
        print("%s, %s, %s, %s, %s, %s, %s" % (time, verticalSpeed, horizontalSpeed, alt, ang, weight, acceleration))

    # over 2 km above the ground
    if alt > 2000:  # maintain a vertical speed of [20-25] m/s
        if verticalSpeed > 25:
            NN += 0.003 * dt  # more power for braking
            # NN = 1  # maximum braking!
        if verticalSpeed < 20:
            NN -= 0.003 * dt  # less power for braking
    # lower than 2 km - horizontal speed should be close to zero
    else:
        if ang > 3:
            ang -= 3  # rotate to vertical position.
        else:
            ang = 0
        NN = 0.5  # brake slowly, a proper PID controller here is needed!
        if horizontalSpeed < 2:
            horizontalSpeed = 0
        if alt < 125:  # very close to the ground!
            NN = 1  # maximum braking!
            # NN += 0.003 * dt  # more power for braking
            if verticalSpeed < 5:
                NN = 0.7  # if it is slow enough - go easy on the brakes

    if alt < 5:   # no need to stop
        NN = 0.4

    # main computations
    ang_rad = math.radians(ang)
    h_acc = math.sin(ang_rad) * acceleration
    v_acc = math.cos(ang_rad) * acceleration
    vacc = get_acc(horizontalSpeed)
    time += dt
    dw = dt * ALL_BURN * NN
    if fuel > 0:
        fuel -= dw
        weight = WEIGHT_EMP + fuel
        acceleration = NN * acc_max(weight)

    else:  # ran out of fuel
        acceleration = 0

    v_acc -= vacc
    if horizontalSpeed > 0:
        horizontalSpeed -= h_acc * dt
    verticalSpeed -= v_acc * dt
    alt -= dt * verticalSpeed
    dist -= horizontalSpeed*dt


# plot
plt.plot(x, y, label = "Altitude")
plt.plot(x, z, label = "Vertical Speed")



# naming the garph
plt.title(' Beresheet Landing: (time - sec) ' + str((time/60)))
# naming the x axis
plt.xlabel('Dist')
# naming the y axis
plt.ylabel('Altitude')

# beautify the x-labels
# plt.gcf().autofmt_xdate()

plt.show()
