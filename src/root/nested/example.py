'''
Created on 6. jun. 2018

@author: Morten
'''


def distcircle(num,radius):
    dist = 0.0
    dia = radius*2
    if num == 0:
        dist = DistCalc(122,dia,942.62)
    if num == 1:
        print("Ring 1")
    if num == 2:
        dist = DistCalc(92.5,dia,1086.49)
    if num == 3:
        print("Ring 3")
    if num == 4:
        dist = DistCalc(122,dia,942.62)
    if num == 5:
        dist = DistCalc(83.5,dia,1053.89)
    if num == 6:
        dist = DistCalc(83.5,dia,1053.89)
    if num == 7:
        dist = DistCalc(26.5,dia,1132.07)
    return dist

def DistCalc(width,dia,focal):
    dist = (width*focal)/dia
    return dist

def main():
    print(distcircle(5, 402))
    
main()