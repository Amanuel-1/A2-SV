if __name__ == '__main__':
  N = int(input())
  list_ =[]

  for _ in range(N):
    cmd  = list(map(str,input().split()))
    
    if len(cmd) ==1:
      if cmd[0] =="print":
        exec(cmd[0]+"(list_)")
      else:
        exec("list_."+cmd[0]+"()")
    elif len(cmd)==2:
      exec("list_."+cmd[0]+"("+cmd[1]+")")
    else:
      exec("list_."+cmd[0]+"("+cmd[1]+","+cmd[2]+")")
     
