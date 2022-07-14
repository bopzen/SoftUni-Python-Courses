title = input()
content = input()
print("<h1>")
print(f"    {title}")
print("</h1>")
print("<article>")
print(f"    {content}")
print("</article>")

while True:
    command = input()
    if command == 'end of comments':
        break
    print("<div>")
    print(f"    {command}")
    print("</div>")