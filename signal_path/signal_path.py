#Simulate singal paths by solving an initial value problem for a system of ODEs (ordinary differential equations) using Michaelisa-Menten enzyme kinetics
#Tomasz Kolbus, 2026-03-27

from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Right-hand side of the system: the time derivative of the state y at time t
# dy / dt = f(t, y)
# y(t0) = y0
def f(t,y,Xt,V1,V2,K1,K2):
    Xa=y[0]
    return V1*(Xt-Xa)/(K1+(Xt-Xa)) - (V2*Xa)/(K2+Xa)


# for p1 in range(1):
    # for p2 in range(5):
        # for p3 in range(1):
            # for p4 in range(1):
                # for p5 in range(1):               
                    
                    # Xt=1.0 # total amout of protein, default 1.0
                    # V1=round(0.5+p2*0.1,2) # maximum kinase activation rate, default 1.0 
                    # V2=round(1.0+p3*0.1,2) # maximum phosphatase deactivation rete, default 1.0 
                    # K1=round(0.1+p4*0.1,2) # Michaelis constant for activation, default 0.1 
                    # K2=round(0.1+p5*0.1,2) # Michaelis constant for deactivation, default 0.1 
                    
                    # params = (Xt,V1,V2,K1,K2)                    
                    # sol = solve_ivp(f, [0, 20], [0],args=params) 
                    # results[params]=sol



#prepare plot to show results
fig, ax = plt.subplots(2, 2, figsize=(16, 10), num="X*(t) - active protein over time")

#populate params and execute solver for different parameters

#######################
###### [ V1 ] #########
#######################

results = {}

#default
Xt,V1,V2,K1,K2 = 1.0,1.0,1.0,0.1,0.1
for p in range(5): 
    V1=round(1.0+p*0.1,2) # maximum kinase activation rate, default 1.0
    params = (Xt,V1,V2,K1,K2)                    
    sol = solve_ivp(f, [0, 20], [0],args=params) 
    results[params]=sol    

# show results 
for x in results:
    ax[0,0].plot(results[x].t, results[x].y[0], label = str(x))
                 
ax[0,0].set_title("#1 different V1 values")
ax[0,0].legend(title="Parameters Xt,V1,V2,K1,K2:", title_fontsize='small', loc='lower right')
ax[0,0].set_xlabel("t", loc='right')
ax[0,0].set_ylabel("X*(t)", loc='top')


#######################
###### [ V2 ] #########
#######################

results = {}

#default
Xt,V1,V2,K1,K2 = 1.0,1.0,1.0,0.1,0.1
for p in range(5): 
    V2=round(1.0+p*0.1,2) # maximum phosphatase deactivation rete, default 1.0 
    params = (Xt,V1,V2,K1,K2)                    
    sol = solve_ivp(f, [0, 20], [0],args=params) 
    results[params]=sol    

# show results 
for x in results:
    ax[0,1].plot(results[x].t, results[x].y[0], label = str(x))
                 
ax[0,1].set_title("#2 different V2 values")
ax[0,1].legend(title="Parameters Xt,V1,V2,K1,K2:", title_fontsize='small', loc='lower right')   
ax[0,1].set_xlabel("t", loc='right')
ax[0,1].set_ylabel("X*(t)", loc='top')

#######################
###### [ K1 ] #########
#######################

results = {}

#default
Xt,V1,V2,K1,K2 = 1.0,1.0,1.0,0.1,0.1
for p in range(5): 
    K1=round(0.1+p*0.1,2) # Michaelis constant for activation
    params = (Xt,V1,V2,K1,K2)                    
    sol = solve_ivp(f, [0, 20], [0],args=params) 
    results[params]=sol    

# show results 
for x in results:
    ax[1,0].plot(results[x].t, results[x].y[0], label = str(x))
                 
ax[1,0].set_title("#3 different K1 values")
ax[1,0].legend(title="Parameters Xt,V1,V2,K1,K2:", title_fontsize='small', loc='lower right')   
ax[1,0].set_xlabel("t", loc='right')
ax[1,0].set_ylabel("X*(t)", loc='top')


#######################
###### [ K2 ] #########
#######################

results = {}

#default
Xt,V1,V2,K1,K2 = 1.0,1.0,1.0,0.1,0.1
for p in range(5): 
    K2=round(0.1+p*0.1,2) # Michaelis constant for deactivation
    params = (Xt,V1,V2,K1,K2)                    
    sol = solve_ivp(f, [0, 20], [0],args=params) 
    results[params]=sol    

# show results 
for x in results:
    ax[1,1].plot(results[x].t, results[x].y[0], label = str(x))
                 
ax[1,1].set_title("#4 different K2 values")
ax[1,1].legend(title="Parameters Xt,V1,V2,K1,K2:", title_fontsize='small', loc='lower right')   
ax[1,1].set_xlabel("t", loc='right')
ax[1,1].set_ylabel("X*(t)", loc='top')

plt.show()


# additional scenarios

"""
# V1 vs V2
plt.clf()
results = {}
params = (1.0,1.0,1.0,0.1,0.1)                    
results[params]=solve_ivp(f, [0, 20], [0],args=params)
plt.plot(results[params].t, results[params].y[0], label = str(params))                 


params = (1.0,1.1,1.0,0.1,0.1)                    
results[params]=solve_ivp(f, [0, 20], [0],args=params)     
plt.plot(results[params].t, results[params].y[0], label = str(params))                 


params = (1.0,1.0,1.1,0.1,0.1)                    
results[params]=solve_ivp(f, [0, 20], [0],args=params)     
plt.plot(results[params].t, results[params].y[0], label = str(params))                 


params = (1.0,1.1,1.1,0.1,0.1)                    
results[params]=solve_ivp(f, [0, 20], [0],args=params)    
plt.plot(results[params].t, results[params].y[0], label = str(params))                 

plt.suptitle("#5 V1 vs V2")
plt.legend(title="Parameters Xt,V1,V2,K1,K2:", title_fontsize='small', loc='lower right')   
plt.show()
"""

"""
# K1 vs K2
plt.clf()
results = {}
params = (1.0,1.0,1.0,0.1,0.1)                    
results[params]=solve_ivp(f, [0, 20], [0],args=params)
plt.plot(results[params].t, results[params].y[0], label = str(params))                 


params = (1.0,1.0,1.0,0.2,0.1)                    
results[params]=solve_ivp(f, [0, 20], [0],args=params)     
plt.plot(results[params].t, results[params].y[0], label = str(params))                 


params = (1.0,1.0,1.0,0.1,0.2)                    
results[params]=solve_ivp(f, [0, 20], [0],args=params)     
plt.plot(results[params].t, results[params].y[0], label = str(params))                 


params = (1.0,1.0,1.0,0.2,0.2)                    
results[params]=solve_ivp(f, [0, 20], [0],args=params)    
plt.plot(results[params].t, results[params].y[0], label = str(params))                 

plt.suptitle("#5 K1 vs K2")
plt.legend(title="Parameters Xt,V1,V2,K1,K2:", title_fontsize='small', loc='lower right')   
plt.show()
"""