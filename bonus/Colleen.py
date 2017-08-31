'''
    Comment
'''
def tutu():
    return
def main():
    bn = chr(10)
    bc = chr(39)
    tutu()
    '''
        myComment
    '''
    s = '%c%c%c%c    Comment%c%c%c%c%cdef tutu():%c    return%cdef main():%c    bn = chr(10)%c    bc = chr(39)%c    tutu()%c'
    s1 = '    %c%c%c%c        myComment%c    %c%c%c%c    s = %c%s%c%c    s1 = %c%s%c%c    s3 = %c%s%c%c    s2 = %c%s%c%c'
    s3 = 'main()'
    s2 = '    print(s % (bc, bc, bc, bn, bn, bc, bc, bc, bn, bn, bn, bn, bn, bn, bn) + s1 % (bc, bc, bc, bn, bn, bc, bc, bc, bn, bc, s, bc, bn, bc, s1, bc, bn, bc, s3, bc, bn, bc, s2, bc, bn) + s2 + bn + s3)'
    print(s % (bc, bc, bc, bn, bn, bc, bc, bc, bn, bn, bn, bn, bn, bn, bn) + s1 % (bc, bc, bc, bn, bn, bc, bc, bc, bn, bc, s, bc, bn, bc, s1, bc, bn, bc, s3, bc, bn, bc, s2, bc, bn) + s2 + bn + s3)
main()
