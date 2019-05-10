# Problem solving

F1 = open (r'C:\Chetan\Repo\Day3\venv\log\logfile.txt')
F2 = open (r'C:\Chetan\Repo\Day3\venv\log\out3.txt','w')

for line in F1:
    if line[:3].isdigit():
        print (line)
        sp = line.split()
        #print(sp)
        ip = sp[0]
        print ('IP Address = ', ip)
        date = sp[3].split(':')
        dt = date[0].strip('[')
        print('Date = ', dt)

        if 'pics' in sp[6]:
            img = sp[6].replace('/pics/','')
            print ('Image File = ',img)
        else:
            print('No Image File.')

        if 'http' in sp[10]:
            url = sp[10].strip('"')
            print('URL = ', url)
        else:
            print('No URL.')

        browser = sp[11].split('/')
        browsername = browser[0].lstrip('"')
        browserVer = browser[1]
        print('Browser Name = ', browsername)
        print('Browser Version = ', browserVer)

        F2.writelines ([ip+'\t',dt+'\t',img+'\t',url+'\t',browsername+'\t',browserVer+'\t'])
        F2.writelines(['\n'])
        #print(ip, dt, img, url, browsername, browserVer, sep='\n',file=F2)