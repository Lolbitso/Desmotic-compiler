notc = input("what to compile?")
c = notc.split()
l = len(c)
t = 1
r = 0
nott = 1
nottf = 7
notte = 6
nottd = 5
nottc = 4
nottb = 3
notta = 2
code = ['null']
comped = [r]
for l in range(l):
  code.append(c[l])

code.append('null')
code.append('null')
code.append('null')
code.append('null')
code.append('null')
code.append('null')
code.append('null')
code.append('null')

#compiler - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

for t in range(l):
  t = code[nott]
  tf = code[nottf]
  te = code[notte]
  td = code[nottd]
  tc = code[nottc]
  tb = code[nottb]
  ta = code[notta]
  if t == 'if':
    comped.append('{' + str(ta) +'=' + str(tb) + ',' + str(tc) + '}')
  else:
    if t == 'xor':
      comped.append('{' + str(ta) + '>' + str(tb) + ',' + str(tb) + '>' + str(ta) + ',' + str(tc) + '}')
    else:
      if t == 'or':
        comped.append('{' + str(ta) +'=1,' + str(tb) + '=1,' + str(tc) + '}')
      else:
        if t == 'and':
          comped.append('{{' + str(ta) + '=1}{' + str(tb) + '=1}=1,' + str(tb) + '}')
        else:
          if t == 'nand':
            comped.append('{{{' + str(ta) + '=1}{' + str(tb) + '=1}=1,0}=0,' + str(tc) + '}')
          else:
            if t == 'xnor':
              comped.append('{' + str(ta) + '=' + str(tb) + ',' + str(tc) + '}')
            else:
              if t == 'nor':
                comped.append('{{' + str(ta) + '=1,' + str(tb) + '=1,0}=0,' + str(tc) + '}')
              else:
                  if t == 'make':
                    comped.append( str(ta) + '=' + str(tb) )
                  else:
                    if t == 'line':
                      comped.append( 'polygon((' + str(ta) + ',' + str(tb) + '),(' + str(tc) + ',' + str(td) + '))')
                    else:
                      if t == 'tri':
                        comped.append( 'polygon((' + str(ta) + ',' + str(tb) + '),(' + str(tc) + ',' + str(td) + '),(' + str(te) + ',' + str(tf) + '))')
                      else:
                          if t == 'if=':
                           comped.append(str(ta) + '={' + str(tb) +'=' + str(tc) + ',' + str(td) + '}')
                          else:
                            if t == 'xor=':
                             comped.append(str(ta) + '={' + str(tb) + '>' + str(tc) + ',' + str(td) + '>' + str(tb) + ',' + str(td) + '}')
                            else:
                              if t == 'or=':
                               comped.append(str(ta) + '={' + str(tb) +'=1,' + str(tc) + '=1,' + str(td) + '}')
                              else:
                                if t == 'and=':
                                 comped.append(str(ta) + '={{' + str(tb) + '=1}{' + str(tc) + '=1}=1,' + str(tc) + '}')
                                else:
                                  if t == 'nand=':
                                     comped.append(str(ta) + '={{{' + str(tb) + '=1}{' + str(tc) + '=1}=1,0}=0,' + str(td) + '}')
                                  else:
                                      if t == 'xnor=':
                                        comped.append(str(ta) + '={' + str(tb) + '=' + str(tc) + ',' + str(td) + '}')
                                      else:
                                       if t == 'nor=':
                                         comped.append(str(ta) + '={{' + str(tb) + '=1,' + str(tc) + '=1,0}=0,' + str(td) + '}')
                                       else:
                                         if t == '+':
                                           r += ta += tb


  nott = nott + 1
  nottf = nottf + 1
  notte = notte + 1
  nottd = nottd + 1
  nottc = nottc + 1
  nottb = nottb + 1
  notta = notta + 1

print(code)
print('compiled equals:')
print(comped)
print(r)

input('waiting')
