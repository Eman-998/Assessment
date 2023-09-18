import bpy
import math

# Clear existing objects, lights, and cameras

bpy.ops.object.select_all(action='DESELECT')
bpy.ops.object.select_by_type(type='MESH')
bpy.ops.object.delete()
bpy.ops.object.select_by_type(type='LIGHT')
bpy.ops.object.delete()
bpy.ops.object.select_by_type(type='CAMERA')
bpy.ops.object.delete()

# Create Takeoff grid
bpy.ops.skybrush.create_takeoff_grid(rows=30, columns=23, drones=690, empty_slots=0)

# Create a camera
bpy.ops.object.camera_add(location=(0, -6, 3)) 
camera = bpy.context.object
camera.data.lens = 35  
camera.data.sensor_width = 32  

# Import the STL file (Add ones own path)
stl_path = "C:\\Users\\Eman's PC\\Assessment\\crownn.stl"
bpy.ops.import_mesh.stl(filepath=stl_path)

# Resize 3D shape
bpy.context.view_layer.objects.active = bpy.context.selected_objects[0]
bpy.ops.transform.resize(value=(0.051368, 0.051368, 0.051368))

# Move the object
bpy.ops.transform.translate(value=(-20.1518, 8.55366, 43.9047))
bpy.ops.transform.translate(value=(-16.0752, -7.71511, 23.2353))
bpy.ops.transform.translate(value=(-3.16919, 8.4823, 12.6904))


# Warning: The next section of code gives errors which i wasn't able to figure due to lack of familiarity with blender functions 


# Coloring all drones with a lighting effect
bpy.context.scene.skybrush.light_effects.active_entry_index = 0

bpy.context.scene.skybrush.led_control.primary_color = (0.867718, 1, 0.252409)
bpy.context.scene.skybrush.led_control.secondary_color = (0.0494089, 0.131038, 0.393114)

bpy.ops.skybrush.apply_colors_to_selection(primary_color=(0.867718, 1, 0.252409), secondary_color=(0.0494089, 0.131038, 0.393114), color='SECONDARY', fade=False)


bpy.data.textures["Texture for light effect"].color_ramp.elements[0].color = (0.997922, 1, 0.578725, 1)
bpy.data.textures["Texture for light effect"].color_ramp.elements[1].color = (0.413729, 0.75, 0.418229, 1)
bpy.data.textures["Texture for light effect"].color_ramp.elements[2].color = (0.272344, 0.362329, 0.5, 1)
bpy.data.textures["Texture for light effect"].color_ramp.elements[3].color = (0.0100851, 0.0402051, 0.467202, 1)


#Turn edit mode on for crown
bpy.ops.object.editmode_toggle()

# Merge vertices by distance with a threshold of 50 to have arround 6
bpy.ops.mesh.remove_doubles(threshold=49.2)

# Create a vertex group named "drones" and assign all vertices to it
# go to drone show tab and select the created vertex group
# Switch off edit mode

# Create a formation 
bpy.ops.skybrush.create_formation(name="crownn", contents='SELECTED_OBJECTS')

# Append the formation to the storyboard
# Recalculate transition of the entire storyboard
# Update time markers


bpy.context.scene.frame_end = 700

## exporting
bpy.context.space_data.params.filename = "CrownRender.skyc"