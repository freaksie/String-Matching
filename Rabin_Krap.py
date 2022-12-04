'''
    Author : Neel Vora
    Email: nxv8988@mavs.uta.edu
'''
class Rabin_Karp:
       def search(pat, txt, q):
        d = 256 #Highest ascii char that can be found in text
        window = len(pat)
        input_length = len(txt)
        p = 0 # hash value for pattern
        t = 0 # hash value for txt
        h = 1 # hash co-efficient

        # Hash Function 
        for i in range(window-1):
            h = (h*d) % q
        for i in range(window):
            p = (d*p + ord(pat[i])) % q 
            t = (d*t + ord(txt[i])) % q
        for i in range(input_length-window+1):
            if p == t:
                for j in range(window):
                    if txt[i+j] != pat[j]:
                        break
                    else:
                        j += 1
                if j == window:
                    print("Found pattern at following index " + str(i))
            if i < input_length-window:
                t = (d*(t-ord(txt[i])*h) + ord(txt[i+window])) % q
                if t < 0:
                    t = t+q