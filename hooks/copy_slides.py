import shutil
import pathlib

def copy_slides(config, **kwargs):
    site_dir = config['site_dir']
    slides_path = pathlib.Path(site_dir) / 'slides'
    slides_path.mkdir(exist_ok=True)

    for slide in pathlib.Path('slides/html').glob('*.html'):
        shutil.copy(slide.resolve(), slides_path.resolve())
