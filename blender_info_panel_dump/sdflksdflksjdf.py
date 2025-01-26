bpy.ops.mesh.primitive_cube_add(size=2, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
bpy.context.space_data.context = 'WORLD'
bpy.context.space_data.context = 'PARTICLES'
bpy.context.space_data.context = 'PHYSICS'
bpy.context.space_data.context = 'CONSTRAINT'
bpy.context.space_data.context = 'PHYSICS'
bpy.context.space_data.context = 'CONSTRAINT'
bpy.context.space_data.context = 'PARTICLES'
bpy.context.space_data.context = 'MODIFIER'
bpy.context.space_data.context = 'PARTICLES'
bpy.context.space_data.context = 'PHYSICS'
bpy.context.space_data.context = 'PARTICLES'
bpy.ops.object.particle_system_add()
bpy.data.particles["ParticleSettings"].use_modifier_stack = True
bpy.data.particles["ParticleSettings"].use_modifier_stack = False
bpy.context.space_data.shading.type = 'MATERIAL'
bpy.context.space_data.shading.type = 'WIREFRAME'
bpy.context.space_data.shading.type = 'SOLID'
bpy.context.space_data.shading.type = 'MATERIAL'
bpy.context.space_data.shading.type = 'RENDERED'
bpy.context.space_data.shading.type = 'SOLID'
bpy.context.space_data.shading.type = 'WIREFRAME'
bpy.context.space_data.shading.type = 'SOLID'
bpy.context.area.ui_type = 'CONSOLE'
bpy.context.area.ui_type = 'INFO'
bpy.context. = 0
bpy.context. = 0
bpy.ops.object.text_add(enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
bpy.data.particles["ParticleSettings"].use_emit_random = False
bpy.data.particles["ParticleSettings"].use_even_distribution = False
bpy.data.particles["ParticleSettings"].use_even_distribution = True
bpy.data.particles["ParticleSettings"].use_emit_random = True
bpy.data.particles["ParticleSettings"].use_rotations = True
bpy.data.particles["ParticleSettings"].use_dynamic_rotation = True
bpy.data.particles["ParticleSettings"].use_dynamic_rotation = False
bpy.ops.object.particle_system_remove()
bpy.ops.object.delete(use_global=False, confirm=False)
Deleted 1 object(s)
bpy.context.area.ui_type = 'CONSOLE'
bpy.context.area.ui_type = 'OUTLINER'
bpy.context.area.ui_type = 'PROPERTIES'
bpy.context.area.ui_type = 'FILES'
bpy.context.area.ui_type = 'ASSETS'
bpy.context.area.ui_type = 'SPREADSHEET'
bpy.context.area.ui_type = 'PREFERENCES'
bpy.context.area.ui_type = 'TEXT_EDITOR'
bpy.context.area.ui_type = 'CONSOLE'
bpy.context.area.ui_type = 'INFO'
bpy.context.area.ui_type = 'DOPESHEET'
bpy.context.area.ui_type = 'TIMELINE'
bpy.context.area.ui_type = 'FCURVES'
bpy.context.area.ui_type = 'DRIVERS'
bpy.context.area.ui_type = 'NLA_EDITOR'
bpy.context.area.ui_type = 'VIEW_3D'
bpy.context.area.ui_type = 'IMAGE_EDITOR'
bpy.context.area.ui_type = 'UV'
bpy.context.area.ui_type = 'CompositorNodeTree'
bpy.context.area.ui_type = 'TextureNodeTree'
bpy.context.area.ui_type = 'GeometryNodeTree'
bpy.context.area.ui_type = 'ShaderNodeTree'
bpy.context.area.ui_type = 'SEQUENCE_EDITOR'
bpy.context.area.ui_type = 'CLIP_EDITOR'
bpy.context.area.ui_type = 'INFO'
bpy.context.area.ui_type = 'CONSOLE'
bpy.context.space_data.context = 'WORLD'
bpy.context.space_data.context = 'SCENE'
bpy.context.space_data.context = 'VIEW_LAYER'
bpy.context.space_data.context = 'TOOL'
bpy.context.space_data.context = 'RENDER'
bpy.context.space_data.context = 'OUTPUT'
bpy.context.space_data.context = 'VIEW_LAYER'
bpy.context.space_data.context = 'SCENE'
bpy.context.space_data.context = 'WORLD'
bpy.context.space_data.context = 'COLLECTION'
bpy.ops.view3d.blenderkit_asset_bar_widget(do_search=False, keep_running=False, tooltip="Click to Show Asset Bar.\nShortcut: ;")
bpy.data.window_managers["WinMan"].blenderkit_models.search_keywords = ""
bpy.data.window_managers["WinMan"].blenderkit_models.search_keywords = "rigged"
bpy.data.window_managers["WinMan"].blenderkit_models.search_keywords = "low poly"
bpy.data.window_managers["WinMan"].blenderkit_models.search_keywords = "low poly"
bpy.ops.view3d.blenderkit_set_category(category_browse="character", category_search="character", asset_type="MODEL")
bpy.ops.view3d.blenderkit_set_category(category_browse="people", category_search="people", asset_type="MODEL")
bpy.ops.view3d.blenderkit_set_category(category_browse="people", category_search="man", asset_type="MODEL")
bpy.ops.view3d.blenderkit_set_category(category_browse="people", category_search="man", asset_type="MODEL")
bpy.ops.view3d.blenderkit_set_category(category_browse="", category_search="character", asset_type="MODEL")
bpy.ops.view3d.blenderkit_set_category(category_browse="", category_search="model", asset_type="MODEL")
bpy.data.window_managers["WinMan"].blenderkitUI.free_only = True
bpy.data.window_managers["WinMan"].blenderkitUI.free_only = False
bpy.data.collections["Collection"].hide_select = True
bpy.data.collections["Collection"].hide_select = False
bpy.data.collections["Collection"].hide_select = True
bpy.data.collections["Collection"].hide_select = False
bpy.context.space_data.context = 'TOOL'
bpy.ops.view3d.blenderkit_asset_bar_widget(do_search=False, keep_running=True)
bpy.data.window_managers["WinMan"].blenderkit_models.search_keywords = "low poly human"
bpy.ops.view3d.blenderkit_asset_bar_widget(do_search=False, keep_running=True)
bpy.ops.scene.blenderkit_download(asset_index=4, target_object="", model_location=(0.0608091, -0.147102, 0), model_rotation=(0, 0, 2.38419e-07))
bpy.ops.object.select_all(action='DESELECT')
bpy.ops.view3d.blenderkit_download_gizmo_widget(asset_base_id="7a4e5e1f-1599-42b4-9481-66a7432af60e")
bpy.ops.view3d.blenderkit_download_gizmo_widget(asset_base_id="7a4e5e1f-1599-42b4-9481-66a7432af60e")
bpy.ops.object.delete(use_global=False, confirm=False)
Deleted 1 object(s)
bpy.ops.view3d.blenderkit_asset_bar_widget(do_search=False, keep_running=True)
bpy.ops.scene.blenderkit_download(asset_index=0, target_object="", model_location=(0.000300169, -0.00115013, 0), model_rotation=(0, 0, 2.38419e-07))
bpy.ops.object.select_all(action='DESELECT')
bpy.ops.view3d.blenderkit_download_gizmo_widget(asset_base_id="f2329b67-240f-4875-a3d9-9fe6445bc86f")
bpy.ops.view3d.blenderkit_download_gizmo_widget(asset_base_id="f2329b67-240f-4875-a3d9-9fe6445bc86f")
bpy.ops.view3d.blenderkit_asset_bar_widget(do_search=False, keep_running=True)
bpy.ops.outliner.item_activate(deselect_all=True)
bpy.ops.outliner.item_activate(deselect_all=True)
bpy.context.space_data.display_mode = 'SCENES'
bpy.context.space_data.display_mode = 'VIEW_LAYER'
bpy.context.space_data.display_mode = 'SEQUENCE'
bpy.context.space_data.display_mode = 'LIBRARIES'
bpy.ops.outliner.item_activate(deselect_all=True)
bpy.context.space_data.display_mode = 'DATA_API'
bpy.context.space_data.display_mode = 'LIBRARY_OVERRIDES'
bpy.context.space_data.display_mode = 'ORPHAN_DATA'
bpy.ops.outliner.item_activate(deselect_all=True)
bpy.ops.outliner.item_activate(deselect_all=True)
bpy.ops.outliner.item_rename()
bpy.ops.outliner.item_rename()
bpy.context.space_data.display_mode = 'SCENES'
bpy.context.space_data.display_mode = 'VIEW_LAYER'
bpy.context. = True
bpy.context. = False
bpy.ops.object.delete(use_global=False, confirm=False)
Deleted 1 object(s)
bpy.ops.object.delete(use_global=False, confirm=False)
Deleted 1 object(s)
bpy.ops.view3d.blenderkit_asset_bar_widget(do_search=False, keep_running=True)
bpy.context.space_data.shading.type = 'MATERIAL'
bpy.context.space_data.shading.type = 'RENDERED'
bpy.context.space_data.shading.type = 'WIREFRAME'
bpy.context.space_data.shading.type = 'SOLID'
bpy.context.space_data.shading.type = 'SOLID'
bpy.context.space_data.shading.type = 'MATERIAL'
bpy.context.space_data.shading.type = 'RENDERED'
bpy.context.space_data.shading.type = 'WIREFRAME'
bpy.context.space_data.shading.type = 'SOLID'
bpy.context.space_data.shading.type = 'MATERIAL'
bpy.context.space_data.shading.type = 'RENDERED'
bpy.context.space_data.shading.wireframe_color_type = 'OBJECT'
bpy.context.space_data.shading.wireframe_color_type = 'RANDOM'
bpy.context.space_data.shading.wireframe_color_type = 'THEME'
bpy.context.space_data.shading.use_scene_world_render = False
bpy.context.space_data.shading.use_scene_world_render = True
bpy.context.space_data.shading.use_scene_lights_render = False
bpy.context.space_data.shading.use_scene_lights_render = True
bpy.context.space_data.shading.use_scene_world_render = False
bpy.context.space_data.shading.studio_light = 'studio.exr'
bpy.context.space_data.shading.studio_light = 'sunrise.exr'
bpy.context.space_data.shading.studio_light = 'sunset.exr'
bpy.context.space_data.shading.studio_light = 'sunrise.exr'
bpy.context.space_data.shading.studio_light = 'studio.exr'
bpy.data.window_managers["WinMan"]. = True
bpy.data.window_managers["WinMan"]. = False
bpy.data.window_managers["WinMan"]. = True
bpy.data.window_managers["WinMan"]. = False
bpy.data.window_managers["WinMan"]. = True
bpy.data.window_managers["WinMan"]. = False
bpy.data.window_managers["WinMan"]. = True
bpy.data.window_managers["WinMan"]. = False
bpy.data.window_managers["WinMan"]. = True
bpy.data.window_managers["WinMan"]. = False
bpy.data.window_managers["WinMan"]. = True
bpy.data.window_managers["WinMan"]. = True
bpy.data.window_managers["WinMan"]. = False
bpy.data.window_managers["WinMan"]. = True
bpy.data.window_managers["WinMan"]. = False
bpy.data.window_managers["WinMan"]. = True
bpy.data.window_managers["WinMan"]. = False
bpy.data.window_managers["WinMan"]. = True
bpy.data.window_managers["WinMan"]. = False
bpy.data.window_managers["WinMan"]. = True
bpy.data.window_managers["WinMan"]. = False
bpy.data.window_managers["WinMan"]. = True
bpy.data.window_managers["WinMan"]. = False
bpy.data.window_managers["WinMan"]. = False
bpy.data.window_managers["WinMan"]. = True
bpy.data.window_managers["WinMan"]. = False
bpy.data.window_managers["WinMan"]. = True
bpy.data.window_managers["WinMan"]. = True
bpy.data.window_managers["WinMan"]. = False
bpy.data.window_managers["WinMan"]. = False
bpy.data.window_managers["WinMan"]. = True
bpy.data.window_managers["WinMan"]. = False
bpy.data.window_managers["WinMan"]. = True
bpy.data.window_managers["WinMan"]. = False
bpy.data.window_managers["WinMan"]. = True
bpy.data.window_managers["WinMan"]. = False
bpy.data.window_managers["WinMan"]. = True
bpy.data.window_managers["WinMan"]. = False
bpy.data.window_managers["WinMan"]. = True
bpy.data.window_managers["WinMan"]. = True
bpy.data.window_managers["WinMan"]. = False
bpy.data.window_managers["WinMan"]. = False
bpy.data.window_managers["WinMan"]. = True
bpy.data.window_managers["WinMan"]. = False
bpy.data.window_managers["WinMan"]. = True
bpy.data.window_managers["WinMan"]. = False
bpy.data.window_managers["WinMan"]. = True
bpy.data.window_managers["WinMan"]. = False
bpy.data.window_managers["WinMan"]. = True
bpy.data.window_managers["WinMan"]. = False
bpy.data.window_managers["WinMan"]. = True
bpy.data.window_managers["WinMan"]. = False
bpy.data.window_managers["WinMan"]. = True
bpy.data.window_managers["WinMan"]. = False
bpy.data.window_managers["WinMan"]. = True
bpy.data.window_managers["WinMan"]. = False
bpy.data.window_managers["WinMan"]. = True
bpy.data.window_managers["WinMan"]. = False
bpy.ops.object.collection_instance_add(collection='Low Poly Big Man', align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
bpy.ops.transform.translate(value=(0.222179, 0.0362106, 0.0233316), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False)
bpy.ops.outliner.item_activate(deselect_all=True)
bpy.ops.outliner.item_activate(deselect_all=True)
bpy.context.space_data.context = 'OUTPUT'
bpy.context.scene.render.use_stamp_frame_range = True
bpy.context.scene.render.use_stamp_frame_range = False
bpy.context.scene.render.use_stamp_memory = True
bpy.context.scene.render.use_stamp_memory = False
bpy.context.scene.render.use_stamp_hostname = True
bpy.context.scene.render.use_stamp_hostname = False
bpy.context.scene.render.use_stamp_lens = True
bpy.context.scene.render.use_stamp_lens = False
bpy.context.space_data.context = 'VIEW_LAYER'
bpy.context.scene.view_layers["ViewLayer"].use_pass_diffuse_direct = True
bpy.context.scene.view_layers["ViewLayer"].use_pass_diffuse_direct = False
bpy.context.scene.view_layers["ViewLayer"].use_pass_diffuse_color = True
bpy.context.scene.view_layers["ViewLayer"].use_pass_diffuse_color = False
bpy.context.scene.view_layers["ViewLayer"].use_pass_glossy_direct = True
bpy.context.scene.view_layers["ViewLayer"].use_pass_glossy_direct = False
bpy.context.scene.view_layers["ViewLayer"].use_pass_glossy_color = True
bpy.context.scene.view_layers["ViewLayer"].use_pass_glossy_color = False
bpy.context.scene.view_layers["ViewLayer"].use_pass_ambient_occlusion = True
bpy.context.scene.view_layers["ViewLayer"].use_pass_ambient_occlusion = False
bpy.context.scene.view_layers["ViewLayer"].use_pass_ambient_occlusion = True
bpy.context.scene.view_layers["ViewLayer"].use_pass_ambient_occlusion = False
bpy.context.space_data.context = 'SCENE'
bpy.context.space_data.context = 'WORLD'
bpy.ops.outliner.item_activate(deselect_all=True)
bpy.context.space_data.context = 'PARTICLES'
bpy.context.space_data.context = 'MODIFIER'
bpy.context.object.modifiers["WeightedNormal"].show_render = False
bpy.context.object.modifiers["WeightedNormal"].show_render = True
bpy.context.object.modifiers["WeightedNormal"].show_render = False
bpy.context.object.modifiers["WeightedNormal"].show_render = True
bpy.ops.object.modifier_set_active(modifier="WeightedNormal")
bpy.context.object.modifiers["WeightedNormal"].weight = 98
bpy.ops.object.modifier_remove(modifier="WeightedNormal")
bpy.context.object.modifiers["Subdivision"].levels = 2
bpy.context.object.modifiers["Subdivision"].levels = 3
bpy.context.object.modifiers["Subdivision"].levels = 4
bpy.context.object.modifiers["Subdivision"].levels = 5
bpy.context.object.modifiers["Subdivision"].levels = 4
bpy.context.object.modifiers["Subdivision"].levels = 3
bpy.context.object.modifiers["Subdivision"].levels = 2
bpy.ops.object.modifier_remove(modifier="Subdivision")

