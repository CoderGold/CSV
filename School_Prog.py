import csv

def Write_Into_File(list):
    with open('Student_Info.csv','a',newline='') as csv_file:
        writer=csv.writer(csv_file)
        writer.writerow(list)
header=['Name','Phone Number','Email Id']
Write_Into_File(header)
while(True):
    info=input('Enter Info Of Student In The Following Format:Name Phone Number Email: ')
    x=input('Is The Given Info Correct(y/n): '+ info+'\n')
    if x=='n':
        print('Please Try Again')
        continue
    else:
        info_list=info.split(' ')
        Write_Into_File(info_list)
        x=input('Would You Like To Enter More?(y/n): ')
        if x=='y':
            continue
        else:
            print('Your File Is Created.Please Open It In Excel')
            break;
