import re

html_code = input()
search_pattern_title = r"<title>(?P<title>.*)</title>"
search_pattern_body = r"<body>(?P<body>.*)</body>"
search_pattern_remove_tags = r"(<[^>]*>)"
search_pattern_remove_new_line = r"\\n"

title = re.search(search_pattern_title, html_code).group("title")
body = re.search(search_pattern_body, html_code).group("body")
body = re.sub(search_pattern_remove_tags,"",body)
body = re.sub(search_pattern_remove_new_line,"",body)
print(f"Title: {title}")
print(f"Content: {body}")