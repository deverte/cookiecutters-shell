import shutil
import os

ext = 'py'

os.chdir('..')
shutil.move(
    os.path.join('{{cookiecutter.class_name}}', f'{{cookiecutter.class_name}}.{ext}'),
    f'{{cookiecutter.class_name}}.{ext}'
)
os.rmdir('{{cookiecutter.class_name}}')