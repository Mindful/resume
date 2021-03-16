from itertools import product
from subprocess import run
from shutil import copyfile
from os import remove
from os.path import exists

toggle_placeholder = r'%TOGGLES%'
file_placeholder = r'%FILE%'
base_compile_string = r'\AtBeginDocument{' + toggle_placeholder + r'}\input{' + file_placeholder + '}'
base_command = 'xelatex -synctex=1 -interaction=nonstopmode'

if exists('resume.pdf'):
	remove('resume.pdf')

def compile_toggle(toggle, value):
	if value:
		return r'\toggletrue{' + toggle + '}'
	else:
		return r'\togglefalse{' + toggle + '}'


def compile_for_toggle_combinations(filename, toggles):
	for toggle_values in product([True, False], repeat=len(toggles)):
		toggle_string = ''.join(compile_toggle(toggle, value) for toggle, value in zip(toggles, toggle_values))
		compile_string = base_compile_string.replace(toggle_placeholder, toggle_string).replace(file_placeholder, filename)

		file_identifier = '-'.join(toggle if value else 'no'+toggle for toggle, value in zip(toggles, toggle_values))
		target_filename = 'pdfs/' + filename + '-' + file_identifier + '.pdf'
		print(target_filename)
		print(base_command + ' "' + compile_string +'"')
		run(base_command.split(), input=bytes(compile_string, 'utf-8'), check=True, capture_output=True)

		copyfile(filename+'.pdf', target_filename)


compile_for_toggle_combinations('resume', ['pii', 'useja', 'long'])
compile_for_toggle_combinations('interpreter_resume', ['pii', 'useja'])






