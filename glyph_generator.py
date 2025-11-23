import os
from PIL import Image

class Log:
    
    def info(text):
        print(f'Info - {text}')
        
    def notice(text):
        print(f'Notice - {text}')
        
    def error(text):
        print(f"Error - {text}")
    #...

def make_unicodes_glyph():
    
    images_folder=input('Images Folder -> ')
    glyph_name=input('Glyph Name (e.g, E3) -> ')
    grid_cells=16
    
    max_size=0
    files=sorted([
        f for f in os.listdir(images_folder)
        if f.lower().endswith(('.png','.jpg','.jpeg'))
    ])
    
    Log.info(f"Found Images:\n{files}")
    
    for f in files:
        img=Image.open(os.path.join(images_folder, f))
        w,h=img.size
        max_size=max(max_size,w,h)
        
    cell_size=max_size
    Log.notice(f'Largest Size Detected({cell_size}px)!')
    
    output_size=cell_size*grid_cells
    
    canvas=Image.new("RGBA", (output_size, output_size), (0, 0, 0, 0))
    
    index=0
    for filename in files:
        img_path=os.path.join(images_folder, filename)
        img=Image.open(img_path).convert("RGBA")
        
        row=index//grid_cells
        col=index%grid_cells
        
        if row >= grid_cells:
            Log.error("Number Of Images Exceeds 16x16!")
            break
        
        cell_x=col*cell_size
        cell_y=row*cell_size
        
        offset_x=cell_x+(cell_size-img.width)//2
        offset_y=cell_y+(cell_size-img.height)//2
        
        canvas.paste(img, (offset_x,offset_y), img)
        index+=1
        
    glyph_file_name=f"glyph_{glyph_name}.png"
    
    canvas.save(glyph_file_name)
    Log.info(f"Output: {glyph_file_name}")
    
    Log.notice(f"Done!")
    
while True:
    
    make_unicodes_glyph()
    
    print("")
    print("")
    print("")