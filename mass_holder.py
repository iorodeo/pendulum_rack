"""
Makes a simple rack for the pendulum experiment kit
"""
from py2scad import *
import scipy

INCH2MM = 25.4

# Inside dimensions
x,y,z = 5.0*INCH2MM, 3.0*INCH2MM, 0.5*INCH2MM
top_row_edge_gap = 1.0*INCH2MM
bottom_row_edge_gap = 0.75*INCH2MM
hole_list = []

# Create top row holes
top_row_diams = [1.0*INCH2MM+0.5, (7.0/8.0)*INCH2MM+0.5, (3.0/4.0)*INCH2MM+0.5]
x_pos_array = scipy.linspace(-0.5*x+top_row_edge_gap, 0.5*x-top_row_edge_gap, len(top_row_diams))
y_pos = +0.25*y
for x_pos, diam in zip(x_pos_array, top_row_diams):
    hole = { 
            'panel'     : 'top',
            'type'      : 'round',
            'location'  : (x_pos,y_pos),
            'size'      : diam, 
            }
    hole_list.append(hole)


# Create bottom row holes
bottom_row_diams = [(5.0/8.0)*INCH2MM+0.5, (1.0/2.0)*INCH2MM+0.5,(3.0/8.0)*INCH2MM+0.5,(1.0/4.0)*INCH2MM+0.5]
x_pos_array = scipy.linspace(-0.5*x+bottom_row_edge_gap, 0.5*x-bottom_row_edge_gap, len(bottom_row_diams))
y_pos = -0.25*y
for x_pos, diam in zip(x_pos_array, bottom_row_diams):
    hole = { 
            'panel'     : 'top',
            'type'      : 'round',
            'location'  : (x_pos,y_pos),
            'size'      : diam, 
            }
    hole_list.append(hole)


params = {
        'inner_dimensions'        : (x,y,z), 
        'wall_thickness'          : (1.0/8.0)*INCH2MM, 
        'lid_radius'              : 0.25*INCH2MM,  
        'top_x_overhang'          : 0.2*INCH2MM,
        'top_y_overhang'          : 0.2*INCH2MM,
        'bottom_x_overhang'       : 0.2*INCH2MM,
        'bottom_y_overhang'       : 0.2*INCH2MM, 
        'lid2front_tabs'          : (0.2,0.5,0.8),
        'lid2side_tabs'           : (0.25, 0.75),
        'side2side_tabs'          : (0.5,),
        'lid2front_tab_width'     : 0.00*INCH2MM,
        'lid2side_tab_width'      : 0.00*INCH2MM, 
        'side2side_tab_width'     : 0.0*INCH2MM,
        'standoff_diameter'       : 0.25*INCH2MM,
        'standoff_offset'         : 0.05*INCH2MM,
        'standoff_hole_diameter'  : 0.116*INCH2MM, 
        'hole_list'               : hole_list,
        }

enclosure = Basic_Enclosure(params)
enclosure.make()

part_assembly = enclosure.get_assembly(explode=(5,5,5),show_front=False, show_back=False, show_left=False, show_right=False)
part_projection = enclosure.get_projection()

prog_assembly = SCAD_Prog()
prog_assembly.fn = 50
prog_assembly.add(part_assembly)
prog_assembly.write('enclosure_assembly.scad')

prog_projection = SCAD_Prog()
prog_projection.fn = 50
prog_projection.add(part_projection)
prog_projection.write('enclosure_projection.scad')
