import bpy

bpy.ops.export_scene.fbx(filepath='C:\\Users\\user\\Desktop\\test_mesh.fbx', object_types={'MESH'}, use_mesh_modifiers=False, add_leaf_bones=False, bake_anim=False)

# +Armature, Animation
bpy.ops.export_scene.fbx(filepath='C:\\Users\\user\\Desktop\\test_armature.fbx', object_types={'ARMATURE', 'MESH', 'OTHER'}, use_mesh_modifiers=False, add_leaf_bones=False, bake_anim=True, bake_anim_use_nla_strips=False, bake_anim_force_startend_keying=False)

