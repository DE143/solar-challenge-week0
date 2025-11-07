md = open('docs/final_report.md').read()
# Option: use pypandoc or weasyprint to convert
# Example (requires pypandoc & pandoc installed):
# import pypandoc
# pypandoc.convert_text(md, 'pdf', format='md', outputfile='final_report.pdf')
print('Please convert docs/final_report.md to PDF using your preferred tool.')
