#You are going to tile a room whose dimensions are length by width feet. There are
#twelve tiles per box, each 1 foot by 1 foot. How many boxes of tiles do you need? You
#can only buy full boxes, not a partial box.


# room area = l*w sq ft
# tile area = 1*1 sq ft = 1.0 sqft and 12 tiles per box
#tiles needed with waste = (room area / tile area) * (1+ 0.10)
# boxes = tiles needed /12
length = 12 
width = 15 
room = length * width 
tile = 1.0 
waste = .10
tile_box = 12
tiles_needed = (room / tile)
waste_tiles = tiles_needed * (1 + waste)
box_tile = waste_tiles / tile_box
print('I need', round(box_tile), 'boxes of tile')

# with the round() im glad it rounded up my og answer was 16.5 so it rounded up to 17.