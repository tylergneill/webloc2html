import sys
import re

def change_extension(fn, old_ext, new_ext):
	return "%s%s" % ( fn[:fn.find(old_ext)], new_ext )

try:
	fn = sys.argv[1]
except IndexError:
	print("no argument given")
	sys.exit(1)
webloc_data = open(fn,'r').read()

string_search = re.search('<string>(.*)</string>', webloc_data, re.IGNORECASE)
if string_search: result = string_search.group(1)

html_data = """<html>
<body>
<script type="text/javascript">
\twindow.location.href = "%s";
</script>
</body>
</html>"""

new_fn = change_extension(fn, 'webloc', 'html')
f_out = open(new_fn, 'w')

print(html_data % result)

f_out.write(html_data % result)
f_out.close()
