bl_info = {
        "name": "SDS only key :)",
        "location": "View3D > Add > Mesh > SDS only key,",
        "description": "Adds a poly cube to the scene via Add > Mesh > SDS only key,",
        "author": "Vladislav Kindushov",
        "version": (0,1),
        "blender": (2, 7, 7),
        "category": "Mesh",
        }
import bpy
 
class sds_key(bpy.types.Operator):
        bl_idname = "object.sds_key"
        bl_label = "SDS key"
       
        @classmethod
        def poll(cls, context):
                return context.active_objectv
       
       
        def execute(self, context):
                sel = bpy.context.selected_objects
 
                obj = bpy.context.object        
 
                GLmod = True
 
                var = True
 
                for i in sel:
                        for j in i.modifiers:
                                if (j.type == 'SUBSURF'):
                                        var = False
 
                if bpy.context.mode == 'EDIT_MESH':
                        GLmod = False
               
                if GLmod == False:
 
                        '''for i in sel:
                                for j in i.modifiers:
                                        if (j.type == 'SUBSURF'):
                                                var = False'''
               
                        #print(var)
                        if var == False:
                                for i in sel:
                                        for j in i.modifiers:
                                                if (j.type == 'SUBSURF'):
                                                        i.modifiers.remove(j)
                                                        #bpy.ops.object.shade_flat()
                                                        break
               
                        elif var == True:
                                bpy.ops.object.modifier_add(type='SUBSURF')
                                for j in i.modifiers:
                                        if (j.type == 'SUBSURF'):
                                                j.levels = 2
                                                j.render_levels = 2
                                                j.show_on_cage = True
                                                j.show_only_control_edges = True
                                                j.use_opensubdiv = True
                                                #bpy.ops.object.shade_smooth()
                                                break  
 
                elif GLmod == True:
 
                        '''for i in sel:
                                for j in i.modifiers:
                                        if (j.type == 'SUBSURF'):
                                                var = False'''
 
                       
                        #print(var)
                        if var == False:
                                for i in sel:
                                        for j in i.modifiers:
                                                if (j.type == 'SUBSURF'):
                                                        i.modifiers.remove(j)
                                                        bpy.ops.object.shade_flat()
                               
                               
 
                       
                        elif var == True:
                                for i in sel:
                                        bpy.context.scene.objects.active = i
                                        bpy.ops.object.modifier_add(type='SUBSURF')
                                        for j in i.modifiers:
                                                if (j.type == 'SUBSURF'):
                                                        j.levels = 2
                                                        j.render_levels = 2
                                                        j.show_on_cage = True
                                                        j.show_only_control_edges = True
                                                        j.use_opensubdiv = True
                                                        bpy.ops.object.shade_smooth()          
                return {'FINISHED'}
                       
def register():
        bpy.utils.register_class(sds_key)
       
        kc = bpy.context.window_manager.keyconfigs.addon
        if kc:
                km = kc.keymaps.new(name="3D View", space_type="VIEW_3D")
                kmi = km.keymap_items.new('object.sds_key', 'ACCENT_GRAVE', 'PRESS',)
 
               
def unregister():
        bpy.utils.unregister_class(sds_key)
        kc = bpy.context.window_manager.keyconfigs.addon
        if kc:
                km = kc.keymaps["3D View"]
                for kmi in km.keymap_items:
                        if kmi.idname == 'object.sds_key':
                                km.keymap_items.remove(kmi)
                                break
                               
if __name__ == "__main__":
        register()