
buoyancy = 0
g = 9.8 #m/s^2
pressure =0
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



    

