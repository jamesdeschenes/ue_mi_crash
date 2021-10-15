# Unreal Editor Material Instance Crash

This is a Unreal Engine project to demonstrate an issue with the **Unreal Engine Editor** and **Material Instances**. The editor crashes when the parent material of a actively used material instance is changed by a script. This happens with both Blueprints and the Python API. The crash does not happen if the material instance is unassigned and not in use.

## Requirements

This project was setup with Unreal 4.27

## Steps to Reproduce from Scratch

1. Create a new material called "A"
2. Create another new material called "B"
3. Create a material instance of "A" called "MI"
4. Create a box and place it in the world
5. Assign the material instance "MI" to the box
6. Change the parent material of "MI" by script using *Blueprints* or *Python*
```python
# Python Example
import unreal
material_b = unreal.load_asset('/Game/B')
material_instance = unreal.load_asset('/Game/MI')
material_instance.set_editor_property('parent', material_b)
```
![image](https://user-images.githubusercontent.com/1924008/137536994-ebc74d4f-6e6e-4f62-afac-a4f186f86fea.png)
7. The editor will crash immediately or shortly their after with some graphical glitches on the box.

## Steps to Reproduce with Project Repo

1. Clone repository
2. Open project
3. * **Blueprint:** Right-click material instance "MI" and under *scripted actions* select *Change Parents*
   * **Python:** Right-click the `example_crash` Python script in the content browser and select *Run*
