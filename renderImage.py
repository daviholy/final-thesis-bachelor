from ovito.io import import_file
from ovito.vis import Viewport
from PySide2.QtGui import QPixmap, QPainter

    
if __name__ == '__main__':
    pipeline = import_file("export.xml")
    pipeline.add_to_scene()
    vp1 = Viewport(type = Viewport.Type.Perspective, camera_dir = (-1, -1, -1)) #back up left corner
    vp1.zoom_all()
    #3840,2160
    f1 = vp1.render_image(alpha = True, size=(1920,1080))

    vp2 = Viewport(type = Viewport.Type.Perspective, camera_dir = (1, 1, -1)) #front up left corner
    vp2.zoom_all()
    f2 = vp2.render_image(alpha = True, size=(1920,1080))

    vp3 = Viewport(type = Viewport.Type.Perspective, camera_dir = (-1, 1, 1)) #front down right corner
    vp3.zoom_all()
    f3 = vp3.render_image(alpha = True, size=(1920,1080))

    vp4 = Viewport(type = Viewport.Type.Perspective, camera_dir = (1, -1, 1)) #back down right corner   
    vp4.zoom_all()
    f4 = vp4.render_image(alpha = True, size=(1920,1080 ))

    save_figure=QPixmap(3840,2160)
    painter=QPainter()
    painter.begin(save_figure)
    painter.drawImage(0,0,f1)
    painter.drawImage(1920,0,f2)
    painter.drawImage(0,1080,f3)
    painter.drawImage(1920,1080,f4)
    painter.end()
    save_figure.save("render.jpg")
