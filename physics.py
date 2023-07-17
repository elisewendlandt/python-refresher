
import numpy as np
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
     acceleration = Force/mass
     return acceleration
'''
calculates angular acceleration with the equation and throws an error if inertia is negative 
'''
def calculate_angular_acceleration(tau, inertia):
     if inertia < 0:
          raise ValueError("Inertia cannot be negative")
     else:
        angular_acceleration = tau/inertia
     
     return angular_acceleration
'''
Calculates torque of an object but throws an error if magnitude is less than zero 
'''

def calculate_torque(F_magnitude, F_direction, r):
     if F_magnitude <= 0:
          raise ValueError("Magnitude cannote be negative")
     elif r<= 0:
          raise ValueError("radius is not negative")
     else:
          x = F_magnitude * np.sin(F_direction)
          Torque = x * r

          return Torque
     
     '''
     Calculates the Inertia of an object using its mass and absolute value of radius 
     
     '''
def calculate_moment_of_inertia(mass,r):
     if (mass < 0): 
            raise ValueError("Mass cannot be negative")
     else:
        I = mass * abs(r*r)
        return I
     
     '''
     used trig to solve for components of F
     used that to calculate acceleration with the previous function 
     put each x and y acceleratoin values into an array
     '''
def calculate_auv_acceleration(F_magnitude, F_angle,volume = 0.1,mass = 100, thruster_distance = 0.5):
     Fy = F_magnitude * np.sin(F_angle)
     Fx = F_magnitude * np.cos(F_angle)
     Ay = calculate_acceleration(Fy, mass)
     Ax = calculate_acceleration(Fx, mass)
     auv_acceleration = [Ax,Ay]
     return auv_acceleration

'''
changed degrees to radians 
calculated torque and assigned it to T 
used the T to calculate angular acceleration with the function 
'''
def calculate_auv_angular_acceleration(F_magnitude, F_angle, inertia = 1, thruster_distance =0.5):
     F_angle = (F_angle *180)/ np.pi
     T = calculate_torque(F_magnitude, F_angle, thruster_distance)
     auv_angular_acceleration = calculate_angular_acceleration(T, inertia)
     return auv_angular_acceleration

def calculate_auv2_acceleration(T, alpha, mass = 100):
     x = [[np.cos(alpha), np.cos(alpha), -np.cos(alpha), -np.cos(alpha)],
          [np.sin(alpha), -np.sin(alpha), -np.sin(alpha), np.sin(alpha)]]
     F = np.matmul(x, T)
     Ax = F[0,0]/mass
     Ay = F[1,0]/mass
     auv2_acceleration = [Ax, Ay]
     return auv2_acceleration

def calculate_auv2__angular_acceleration(T, alpha, Latitude, Longitude, inertia = 100):

     if Latitude <= 0 :
          raise ValueError("Latitude cannot be negative")
     elif Longitude <= 0 :
          raise ValueError("Longitude cannot be negative")
     x = [[np.cos(alpha), np.cos(alpha), -np.cos(alpha), -np.cos(alpha)],
          [np.sin(alpha), -np.sin(alpha), -np.sin(alpha), np.sin(alpha)]]
     F = np.matmul(x, T)
     Fnet = F[0] + F[1]
     rx = np.sqrt((Latitude*Latitude) + (Longitude*Longitude))
     tau = Fnet * rx
     auv2_angular_acceleration = calculate_angular_acceleration(tau,rx)
     return auv2_angular_acceleration



