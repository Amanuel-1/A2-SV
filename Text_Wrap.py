import textwrap

def wrap(string, max_width):
  j= max_width
  new_lines =0
  while j<len(string):
    string = string[:j+new_lines] + "\n" +string[j+new_lines:]
    new_lines +=1
   
    j+=max_width
  return string

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
