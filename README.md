# Assessment

# Steps

## Step 1

 Understanding what the problem is asking for. 
 Input: An STL file of a 3D Object
 Output: Represent the 3D Object in such a way that it can be viewed as if it were physically present from different angles or perspectives in real space.

 This can be done using Blender, which would visualize the object in the real world. Blender has virtual cameras that can be used to simulate the movement of drones or as is to capture the objects appereance from differnet cameras.


 Since I have never used Blender before. I used the following guides to understand how Blender works. 

 https://www.youtube.com/watch?v=EMMOZ3OhASw&ab_channel=BlenderForbeg -> tried to understand how drones can be used in 3D object and at first, I didnt know that drones arent readily created tools in blender. 

 However, I understood afterwards that cameras in blender can be used instead of creating a drone in blender to achieve the goal of the problem. 

 https://www.premiumbeat.com/blog/blender-software-guide/ -> Gave me pointers on how Blender works and what it is used for and the tools available such as cameras and 3D objects.


 Now that I got a much clearer picture of the problem, I can divide this problem into smaller pieces.

 1. Create a STL file for a simple 3D Object (Cube)
 2. Install Blender 
 3. Import the STL file in blender
 4. Setup the virtual cameras
 5. Animate the cameras 
 6. Render the perspective for object

  https://www.youtube.com/watch?v=nVIMVBmAi_8&ab_channel=AndrewSink -> Used Chatgpt to create an STL file for a cube object and fixed it since it had errors

  I followed the above tutorial and created an STL file for the sube which rendered perfectly after fixing a few errors.  

  https://www.youtube.com/watch?v=O67P0uzbQBk&ab_channel=NikKottmann -> This video was useful as it gave me insight on montion tracking and i used it as a guide 

  **PSA: I realized up until this point I had completely misunderstood the entire assignment as the aim of the company is to have drone shows as advertisements for other companies. I realized my mistake when I searched what Blender Skybrush was used for.**


# REDO

## Step 1

https://www.youtube.com/watch?v=n9Pd8fXS2j4&list=PLugH8MPHvzvQtgdtnnsQn28eWh54bYBGs&ab_channel=COLLMOT --> Used this playlist as a guide

 Input: An STL file of a 3D Object
 Output: Represent the 3D Object using drones in blender skybrush in real space.

1. Import STL file
2. Create drones 
3. Animate the drones for external meshes
4. Define flight paths for drones
5. View it using Skybrush viewer
6. Put this all in a python script

I installed the Skybrush add-on plugin tool.

## Step 2: Importing STL File and creation of drones

I imported the STL file I had previously created.

Skybrush tool in Blender has drones as objects available. Another way would to to use spheres and insert a virtual camera in them thus it would act as a drone.

## Step 3 and 4: Animate the drone for the STL file and defining flight paths

I added 9 drones with 3 x 3 to represent the cube in real space. It had 8 vertices hence i used 8 drones. It worked well.

To test with a much higher number of drones, I used a crown.stl file from the internet. The crown object had around 5,049 vertices however I used a maximum of around 690 drones which was still enough to visualise the 3D object.

**Challenge**

At first , I was not able to make the drones mimic the 3D Object. 
https://www.youtube.com/watch?v=AstdDVdHGSo&list=PLugH8MPHvzvQtgdtnnsQn28eWh54bYBGs&index=4&ab_channel=COLLMOT -> I followed the following tutorial which then solved my problem. Using this tutorial, I also added a lights effect

## Step 5: Viewing using Skybrush Viewer

After exporting the animation as a .skyc file, and adjusting the scene by zooming out. The animation works well

## Step 6: Creating a python script

This was a bit challenging so I tried to use chatgpt-3.5 for a bit of help. However, it did not include any information regarding Skybrush Studio.

Chat-gpt did not give the full code but gave steps for the script


    # import bpy
    # Initialize Blender environment
    # Load STL file, create drone models, set up lighting, etc.
    # Define flight paths for drones
    # Use keyframes to specify drone positions and orientations over time
    # Choreograph the show
    # Define formations, transitions, and effects
    # Create a timeline for the show
    # Add lighting effects
    # Use keyframes to control lights on the drones
    # Visualize and verify the show
    # Render a preview of the simulation
    # Export or simulate the show
    # Test and refine as needed
    # Export or save the final result
    
      
   Using the above comments, a bit of help from chatgpt  (most commands were incorrect) , and the use of console log in blender to see the commands logged when clicked, I created the following python script *"run.py"*(though not fully functional).

This script can be run in the scripting tab in blender by creating a new text file. However, it is not fully functional as there were some unresolved errors as commented in the code. I believe this is due to the learning curve in understanding Blender.

   Therefore, the rest of the steps were done on blender manually and exported as a .skyc file. I tested the render named *" CrownRender.skyc"* using Skybrush Viewer.

   The result is the following GIF:
   
![](https://github.com/Your_Repository_Name/Your_GIF_Name.gif)
    
**I began working on this assignment properly on Wednesday (13/09/2023) as I had misunderstood the assignment when I first recieved it but I got on the right track after asking the Devops Lead a few questions to clarify my understanding.** 
