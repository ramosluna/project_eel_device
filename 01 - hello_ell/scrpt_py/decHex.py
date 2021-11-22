count = 0
with open('v4.html', 'w') as arquivo:
        arquivo.writelines('</tr>\n')
        arquivo.writelines('<th>00</th>\n')
        for r in range(0, 65535): #131071

            if count <= 15:
                s = hex(r)[2:]

                arquivo.writelines('<th id=%s></th>\n' %s)
                #arquivo.writelines(s)
                count += 1
            else:
                count = 1
                arquivo.writelines('</tr>\n')
                s = hex(r)[2:]
                arquivo.writelines('<th>%s</th>\n' % s)
                arquivo.writelines('<th id=%s></th>\n' % r)

print('success')



    

