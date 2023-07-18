import numpy as np
import matplotlib.pyplot as plt
buoyancy = 0
g = 9.8 #m/s^2
pressure =0
Force = 0
tau = 0
inertia = 0
def __init__(self, V, density_fluid, mass, depth):
        #defines each variable and can be changed later
        self.V = V
        self.density_fluid = density_fluid
        self.mass = mass
        self.depth = abs(depth)
    
def calculate_buoyancy(V, density_fluid):
        #checks if density of the fluid is negative if not it calculates buoyancy
        V = V
        density_fluid = density_fluid
        if(density_fluid <0):
            raise ValueError("density cannot be negative")
        else:
            buoyancy = V* density_fluid * g
            print(buoyancy)
        return buoyancy

def will_it_float(V, density_fluid, mass):
        #
        V = V
        density_fluid = density_fluid
        mass = mass
        if (V < 0):
            raise ValueError("Volume cannot be negative")
        elif (mass < 0): 
            raise ValueError("Mass cannot be negative")
        else:
            if buoyancy < (g*mass):
                return False
            elif buoyancy > (g*mass):
                return True
            else:
                return None
        
def calculate_pressure(depth):
        depth = abs(depth)
        pressure = 1000 * g * depth
         
        return pressure #in pascals 
'''
Calculates acceleration 
'''
def calculate_acceleration(Force, mass):
     if mass < 0:
          raise ValueError("mass cannot be negative")
     acceleration = Force/mass
     return acceleration
'''
calculates angular acceleration with the equation and throws an error if inertia is negative 
'''
def calculate_angular_acceleration(tau, inertia):
     if inertia <= 0:
          raise ValueError("Inertia cannot be negative")
     else:
        angular_acceleration = tau/inertia
     
     return angular_acceleration
'''
Calculates torque of an object but throws an error if magnitude is less than zero 
'''

def calculate_torque(F_magnitude, F_direction_degrees, r):
     if F_magnitude <= 0:
          raise ValueError("Magnitude cannote be negative")
     if r<= 0:
          raise ValueError("radius is not negative")
     else:

          F_direction_radians = (F_direction_degrees*np.pi)/180
          torque= F_magnitude * np.sin(F_direction_radians)*r

          return torque
     
     '''
     Calculates the Inertia of an object using its mass and absolute value of radius 
     
     '''
def calculate_moment_of_inertia(mass,r):
     if mass <= 0 or r<=0: 
            raise ValueError("Mass cannot be negative")
     else:
        moment_of_inertia = mass*np.power(r,2)
        return moment_of_inertia
     
     '''
     used trig to solve for components of F
     used that to calculate acceleration with the previous function 
     put each x and y acceleratoin values into an array
     '''
def calculate_auv_acceleration(F_magnitude, F_angle_radians,volume = 0.1,mass = 100, thruster_distance = 0.5):
     if F_magnitude<=0 or mass<=0 or volume<=0 or thruster_distance <=0:
          raise ValueError("Invalid cannot be negative")
     F_y = F_magnitude * np.sin(F_angle_radians)
     F_x = F_magnitude * np.cos(F_angle_radians)
     acceleration_y = calculate_acceleration(F_y, mass)
     acceleration_x = calculate_acceleration(F_x, mass)
     net_acceleration = np.array([acceleration_x, acceleration_y])
     return net_acceleration

'''
changed degrees to radians 
calculated torque and assigned it to T 
used the T to calculate angular acceleration with the function 
'''
def calculate_auv_angular_acceleration(F_magnitude, F_angle_radians, inertia = 1, thruster_distance =0.5):
     if F_magnitude <=0 or inertia <=0 or thruster_distance<=0:
          raise ValueError("invalid values")
     perpendicular_force = F_magnitude*np.sin(F_angle_radians)
     angular_acceleration = calculate_angular_acceleration(perpendicular_force*thruster_distance, inertia)
     return angular_acceleration

def calculate_auv2_acceleration(T, alpha, theta, mass = 100):
     if type(T) != np.ndarray:
          raise ValueError("T has to be an ndarray")
     if mass <= 0:
          raise ValueError("mass cannot be negative")

     components = np.array([[np.cos(alpha), np.cos(alpha), -np.cos(alpha), -np.cos(alpha)],
          [np.sin(alpha), -np.sin(alpha), -np.sin(alpha), np.sin(alpha)] ])
     net_force_prime = np.matmul(components,T)
     rotation_matrix = np.array([[np.cos(theta), -np.sin(theta)],[np.sin(theta),np.cos(theta)]])
     net_force = np.matmul(rotation_matrix, net_force_prime)
     acceleration_x = net_force[0]/mass
     acceleration_y = net_force[1]/mass
     net_acceleration = np.array([acceleration_x,acceleration_y])
     return net_acceleration

def calculate_auv2__angular_acceleration(T, alpha, L, l, inertia = 100):
     if type(T) != np.ndarray:
          raise ValueError("T has to be an ndarray")
     if L <= 0 :
          raise ValueError("Latitude cannot be negative")
     if l <= 0 :
          raise ValueError("Longitude cannot be negative")
     if inertia <= 0:
          raise ValueError("inertia cannot be negative")
     
     components = np.array([L*np.sin(alpha) + l*np.cos(alpha), -L*np.sin(alpha)-l*np.cos(alpha),L*np.sin(alpha) + l*np.cos(alpha), -L*np.sin(alpha)-l*np.cos(alpha)])
     net_torque = np.matmul(components,T)
     angular_acceleration = calculate_angular_acceleration(net_torque,inertia)
     return angular_acceleration

def simulate_auv2_motion(T,alpha, L, l, inertia =100, dt =0.1,t_final =10, x0 =0, y0 =10, theta0 = 0, mass =100):
     time = np.arange(0, t_final, dt)
     x = np.zeros_like(time)
     x[0] = x0
     y = np.zeros_like(time)
     y[0] = y0
     theta = np.zeros_like(time)
     theta[0] = theta0
     v = np.zeros(shape =(len(time),2))
     omega = np.zeros_like(time)
     linear_acceleration = np.zeros(shape =(len(time),2))
     angular_acceleration = np.zeros_like(time)
     for i in range(1, len(time)):
          linear_acceleration[i][0] = calculate_auv2_acceleration(T,alpha, theta[i], mass)[0]
          linear_acceleration[i][1] = calculate_auv2_acceleration(T,alpha, theta[i], mass)[1]
          v[i][0] = v[i-1][0] + linear_acceleration[i][0]*dt
          v[i][1] = v[i-1][1] + linear_acceleration[i][1]*dt
          x[i] = x[i-1] + v[i][0] * dt
          y[i] = y[i-1] + v[i][1] * dt

          angular_acceleration[i] = calculate_auv2__angular_acceleration(T, alpha, L, l, inertia) 
          omega[i] = omega[i-1] + angular_acceleration[i]*dt
          theta[i] = np.mod(theta[i-1] + omega[i-1]*dt, 2*np.pi)
          ret = (time,x, y, theta,v, omega, linear_acceleration)
          return ret

def plot_auv2_motion(time,x,y,theta,v, omega, a):
     plt.plot(time, x, label="X:Position")
     plt.plot(time, y, label="Y:Position")
     plt.plot(time, theta, label="Angle Displacement")
     vx = np.zeros_like(time)
     vy = np.zeros_like(time)
     ax = np.zeros_like(time)
     ay = np.zeros_like(time)
     for i in range (0,len(v)):
         vx[i] = v[i][0]
         vy[i] = v[i][1]
         ax[i] = a[i][0]
         ay[i] = a[i][1]
     plt.plot(time, omega, label="Angular Velocity")
     plt.plot(time, vx, label="X:Velocity")
     plt.plot(time, vy, label="Y:Velocity")
     plt.plot(time, ax, label="X:Acceleration")
     plt.plot(time, ay, label="Y:Acceleration")
     plt.xlabel("Time (s)")
     plt.ylabel("Position (m), Velocity (m/s), Acceleration (m/s^2)")
     plt.legend()
     plt.show()

     
