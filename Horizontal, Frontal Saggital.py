#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# In[2]:


data=pd.read_excel('001_08.xlsx')
data.head()


# In[3]:


data.columns


# In[4]:


mag_x = data['Supine 8 min: Horizontal Magnitude']
mag_y = data['Supine 8 min: Frontal Magnitude']
mag_z = data['Supine 8 min: Saggital Magnitude']

ha_x = data['Supine 8 min: Horizontal Angle']
ha_y = data['Supine 8 min: Frontal Angle']
ha_z = data['Supine 8 min: Saggital Angle']

hap_x = data['Supine 8 min: Hor Planar Angle']
hap_y = data['Supine 8 min: Fro Planar Angle']
hap_z = data['Supine 8 min: Sag Planar Angle']

print(mag_x)


# In[5]:


exercise_duration = 8 * 60
num_samples = 134
time_values = np.linspace(0, exercise_duration, num_samples)


# In[6]:


fig, axs = plt.subplots(nrows=3, ncols=1, figsize=(10, 10))
axs[0].plot(time_values,mag_x)
axs[0].set_title('Horizontal Magnitude vs Time')

axs[1].plot(time_values,mag_y)
axs[1].set_title('Frontal Magnitude vs Time')

axs[2].plot(time_values,mag_z)
axs[2].set_title('Saggital Magnitude vs Time')

fig.suptitle('All 3 Magnitudes w.r.t Time')
plt.show()


# In[7]:


np_mag_x = np.array(mag_x)
np_ha_x = np.array(ha_x)
np_hap_x = np.array(hap_x)
np_mag_y = np.array(mag_y)
np_ha_y = np.array(ha_y)
np_hap_y = np.array(hap_y)
np_mag_z = np.array(mag_z)
np_ha_z = np.array(ha_z)
np_hap_z = np.array(hap_z)


# In[8]:


# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the vector
ax.quiver(0, 0, 0, np_mag_x[:], np_ha_x[:], np_hap_x[:], color='r')

# Set the axis limits and labels
ax.set_xlim([np_mag_x.min(), np_mag_x.max()])
ax.set_ylim([np_ha_x.min(), np_ha_x.max()])
ax.set_zlim([np_hap_x.min(), np_hap_x.max()])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Display the plot
plt.show()


# In[9]:


# Set up the plot
fig, ax = plt.subplots()

# Plot the vectors using the quiver function
for i in range(133):
    ax.quiver(0, 0, time_values[i], np_mag_x[i], angles='xy', scale_units='xy', scale=1, color='red')


# Set the x and y limits of the plot
ax.set_xlim([time_values.min(), time_values.max()])
ax.set_ylim([np_mag_x.min(), np_mag_x.max()])

# Label the x and y axes
ax.set_xlabel('Time')
ax.set_ylabel('Magnitude X')

# Display the plot
plt.show()


# In[10]:


# Set up the plot
fig, ax = plt.subplots()

# Plot the vectors using the quiver function
for i in range(133):
    ax.quiver(0, 0, time_values[i], np_mag_y[i], angles='xy', scale_units='xy', scale=1, color='red')


# Set the x and y limits of the plot
ax.set_xlim([time_values.min(), time_values.max()])
ax.set_ylim([np_mag_y.min(), np_mag_y.max()])

# Label the x and y axes
ax.set_xlabel('Time')
ax.set_ylabel('Magnitude Y')

# Display the plot
plt.show()


# In[11]:


# Set up the plot
fig, ax = plt.subplots()

# Plot the vectors using the quiver function
for i in range(133):
    ax.quiver(0, 0, time_values[i], np_mag_z[i], angles='xy', scale_units='xy', scale=1, color='red')


# Set the x and y limits of the plot
ax.set_xlim([time_values.min(), time_values.max()])
ax.set_ylim([np_mag_z.min(), np_mag_z.max()])

# Label the x and y axes
ax.set_xlabel('Time')
ax.set_ylabel('Magnitude Z')

# Display the plot
plt.show()


# In[13]:


magnitude = np_mag_x
angle_degrees = np_ha_x

# Convert angle to radians
angle_radians = np.radians(angle_degrees)

# Calculate components of vector
x = magnitude * np.cos(angle_radians)
y = magnitude * np.sin(angle_radians)

# Create plot with arrow representing vector
fig, ax = plt.subplots()
for i in range(133):
    ax.quiver(0, 0, x[i], y[i], angles='xy', scale_units='xy', scale=1, color='red')


ax.set_xlim([-2.5, 2.5])
ax.set_ylim([-2.5, 2.5])
plt.show()


# In[14]:


magnitude_y = np_mag_y
angle_degrees_y = np_ha_y

# Convert angle to radians
angle_radians_y = np.radians(angle_degrees_y)

# Calculate components of vector
x1 = magnitude * np.cos(angle_radians_y)
y1 = magnitude * np.sin(angle_radians_y)

# Create plot with arrow representing vector
fig, ax = plt.subplots()
for j in range(133):
    ax.quiver(0, 0, x1[j], y1[j], angles='xy', scale_units='xy', scale=1, color='blue')


ax.set_xlim([-2.5, 2.5])
ax.set_ylim([-2.5, 2.5])
plt.show()


# In[17]:


magnitude_z = np_mag_z
angle_degrees_z = np_ha_z

# Convert angle to radians
angle_radians_z = np.radians(angle_degrees_z)

# Calculate components of vector
x2 = magnitude * np.cos(angle_radians_z)
y2 = magnitude * np.sin(angle_radians_z)

# Create plot with arrow representing vector
fig, ax = plt.subplots()
for k in range(133):
    ax.quiver(0, 0, x2[k], y2[k], angles='xy', scale_units='xy', scale=1, color='black')


ax.set_xlim([-2.5, 2.5])
ax.set_ylim([-2.5, 2.5])
plt.show()


# In[ ]:




