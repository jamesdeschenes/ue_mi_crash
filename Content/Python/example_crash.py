import unreal
material_b = unreal.load_asset('/Game/B')
material_instance = unreal.load_asset('/Game/MI')
material_instance.set_editor_property('parent', material_b)
