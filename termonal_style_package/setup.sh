from setuptools import setup, find_packages

setup(
    name='termonal_style',  # نامی که با آن پکیج را نصب می‌کنند: pip install term_styles
    version='1.1',    # شماره ورژن اولیه
    packages=find_packages(), # به setuptools می‌گوید که پوشه‌هایی با فایل __init__.py را پیدا کند
    description='A simple library for terminal text styling and colors.',
    author='GFardad',
    author_email='greengame986@gmail.com',
    url='https://github.com/GFardad', # (اختیاری) آدرس گیت‌هاب
)