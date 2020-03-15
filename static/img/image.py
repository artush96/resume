from PIL import Image

image = Image.open('/mnt/d/PyProject/resume/static/img/linkedin.png')
imageTemproaryResized = image.resize( (250,250) ) 
imageTemproaryResized.save('/mnt/d/PyProject/resume/static/img/linkedin.png', optimize=True, format='PNG', quality=50)
