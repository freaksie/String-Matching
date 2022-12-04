'''
    Author : Neel Vora
    Email: nxv8988@mavs.uta.edu
'''
class Knuth_Morris:
    def pie_table(pattern, window, pie):
        pie[0]
        len = 0 
        i = 1
        while i < window:
            if pattern[i]== pattern[len]:
                len += 1
                pie[i] = len
                i += 1
            else:
                if len != 0:
                    len = pie[len-1]
                else:
                    pie[i] = 0
                    i += 1
    def KMPSearch(pattern, input):
        window = len(pattern)
        input_length = len(input)
        pie = [0]*window
        j = 0 
        Knuth_Morris.pie_table(pattern, window, pie)
        i = 0
        while i < input_length:
            if pattern[j] == input[i]:
                i += 1
                j += 1
            if j == window:
                print ("Found pattern at follwing index", str(i-j))
                j = pie[j-1]
            elif i < input_length and pattern[j] != input[i]:
                if j != 0:
                    j = pie[j-1]
                else:
                    i += 1