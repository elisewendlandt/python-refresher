
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
     if F_magnitude < 0:
          raise ValueError("Magnitude cannote be negative")
     else:
          Torque = F_magnitude * F_direction * abs(r)

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
# def calculate_auv_acceleration(F_magnitude, F_angle,volume = 0.1,mass = 100, thruster_distance = 0.5):
     
     
