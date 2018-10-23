# -*- coding: utf-8 -*-
"""
This is horribly messy, I'll clean it up soon
"""

perm_dna_list = list()
perm_dna_list.append(('YGBGRRGBRGBB','GYRYBBYRBYRR'))
perm_dna_list.append(('YGGYRRYYBBRRYBBRRY', 'GYYGBBGGRRBBGRRBBG'))
perm_dna_list.append(('RYGGYBBYYRRBYY','BGYYGRRGGBBRGG'))
perm_dna_list.append(('YBBYRRB','GRRGBBR'))
perm_dna_list.append(('GBRGBBGRRGBRGBBGRRGBYGBGRRG','YRBYRRYBBYRBYRRYBBYRGYRYBBY'))
perm_dna_list.append(('RGGBRRGBBRRGBBRRGGBYBG','BYYRBBYRRBBYRRBBYYRGRY'))


dna_list = list()
#dna_list.append(('YGBGRRGBR___','________BYRR'))
#dna_list.append(('YGGYRRYYBBRRYBB___', '____________GRRBBG'))
#dna_list.append(('R_____________','BGYYGRRGGBBRGG'))
#dna_list.append(('YBB____','__RGBBR'))
#dna_list.append(('GBRGBBG____________________','____RRYBBYRBYRRYBBYRGYRYBBY'))
#dna_list.append(('RGGBRRGBBRRGBBRRGGB___','__YRBBYRRBBYRRBBYYRGRY'))

# 0 to 4
dna_list.append(('GBRGBBGRRGBRGBBGRRGBYGBGRRGBRGBB','YRBYRRYBBYRBYRRYBBYRGYRYBBYRBYRR')) # LAST 
# 0 to 1 inverse
#dna_list.append(('YYBRRYYBBYGGYRRYYBBRRYBBRRY','GGRBBGGRRGYYGBBGGRRBBGRRBBG'))
# 0 to 3 inverse
#dna_list.append(('YBBYRRBBYRRBBYYRRYGGYBBYYRRBYY','GRRGBBRRGBBRRGGBBGYYGRRGGBBRGG'))
# 0 to 2 flipped
dna_list.append(('GRRGBBRRGBBRRGGBBGYYGRRGGBBRGGBRRGBBRRGBBRRGGBYBG','YBBYRRBBYRRBBYYRRYGGYBBYYRRBYYRBBYRRBBYRRBBYYRGRY')) # LAST
# 0 to 1
#GRRGBBRRGBBRRGGBBGYYGRRGGBBRGGBRRGBBRRGBBRRGGBYBGBRGBBGRRGBRGBBGRRGBYGBGRRGBRGBB

#dna_list.append(('',''))
#dna_list.append(('',''))

altered_flag = ['', ' flipped', ' inverse', ' inverse flipped']

pair = {'R':'B','B':'R','Y':'G','G':'Y','.':'.'}

def pair_up(tple):
    str1 = ''
    str2 = ''
    for x, y in zip(tple[0], tple[1]):
        if x == '_' and y == '_':
            str1 += '_'
            str2 += '_'
        elif x != '_' and y != '_':
            str1 += x
            str2 += y
        elif x == '_':
            str1 += pair[y]
            str2 += y
        else:
            str1 += x
            str2 += pair[x]
    return (str1, str2)

for i, dna in enumerate(dna_list):
    dna_list[i] = pair_up(dna)

def check_complete(tple):
    print 'Checking {}'.format(tple[0])
    if len(tple[0].replace('.','')) != 80:
        print '! Wrong size ({})'.format(len(tple[0].replace('.','')))
        return False
    
    for i, dna in enumerate(perm_dna_list):
        #        make sure its in tple
        if dna[0] not in tple[0] and reverse(dna)[0] not in tple[0] and flip(dna)[0] not in tple[0] and flip(reverse(dna))[0] not in tple[0]:
            print '! DNA {} not found'.format(i)
            return False
    return True
        
def match_letters(a,b):
    if (a == '_') or (b == '_') or (a == 'Y' and b == 'G') or (a == 'G' and b == 'Y') or (a == 'R' and b == 'B') or (a == 'B' and b == 'R') or (a == '.' and b == '.'):
        return True
    return False

def print_tuple(tple):
    print "{}\n{}\n".format(tple[0], tple[1])

def confirm_match(tple):
    for i in range(len(tple[0])):
        if not match_letters(tple[0][i], tple[1][i]):
            return False
    return True

def check_gaps(tple):
    first_pair = False
    first_gap = False
    for x, y in zip(tple[0], tple[1]):
        if x != '_' and y != '_':
            if first_gap:
                return True
            first_pair = True
        else:
            if first_pair:
                first_gap=True
    return False

def reverse(tple):
    return (tple[0][::-1], tple[1][::-1])

def flip(tple):
    return (tple[1], tple[0])

def merge(tple):
    str1, str2 = tple
    out_str = ""
    for z in zip(str1, str2):
        if (z[0] == z[1]):
            out_str += z[0]
        elif (z[0] == '_'):
            out_str += z[1]
        elif (z[1] == '_'):
            out_str += z[0]
        else:
            return 0
    return out_str



def pad_strings(str1, str2, offset):
    return ('_' * (max(0, offset + 1 - len(str1))) + str1 + '_' * (max(0, len(str2) - 1 - offset)), 
            '_' * (max(0, len(str1) - 1 - offset)) + str2 + '_' * (max(0, offset + 1 - len(str2))))

def check_compatible(tple1, tple2, threshold=0):
    #compatibility_list = list()
    compatible_tple = 0
    for pad in range(threshold, len(tple1[0]) + len(tple2[0]) - 1 - threshold):
        s1pm = pad_strings(tple1[0], tple2[0], pad)
        s2pm = pad_strings(tple1[1], tple2[1], pad)
        s1 = merge(s1pm)
        s2 = merge(s2pm)
#        print "Pad {}:\nMerging s1:\n{} merged with\n{} =\n{}\n".format(pad, s1pm[0], s1pm[1], s1)
#        print "Merging s2:\n{} merged with\n{} =\n{}\n".format(s2pm[0], s2pm[1], s2)
        if s1 and s2:
#            print "Pad {}:\nMerging s1:\n{} merged with\n{} =\n{}\n".format(pad, s1pm[0], s1pm[1], s1)
#            print "Merging s2:\n{} merged with\n{} =\n{}\n".format(s2pm[0], s2pm[1], s2)
            temp_tple = (s1, s2)
#            print "Pad {}:".format(pad)
#            print_tuple(temp_tple)
#            print "Match: {}, Gaps: {}".format(confirm_match(temp_tple), check_gaps(temp_tple))
            if confirm_match(temp_tple) and not check_gaps(temp_tple):
#                print "+ match pad {} (gaps {}):\n\n{}\n{}\n\n".format(pad, check_gaps(temp_tple), s1, s2)
#                and not check_gaps(temp_tple):
#                compatibility_list.append((pad, temp_tple, abs(len(s1[1]) - max(len(tple1[0]), len(tple2[0])))))
                if compatible_tple == 0 or len(compatible_tple[0]) > len(temp_tple[0]):
                    compatible_tple = temp_tple
#                print "+ match pad {}:".format(pad)
#                print_tuple(temp_tple)
    return compatible_tple


if __name__ == '__main__':
    
    print "DNA List:\n"
    for di, dna in enumerate(dna_list):
        print "DNA {}".format(di)
        print_tuple(dna)
        
    dna_list_copy = dna_list[:]
    
    for repeat in range(1):
        
        print '> Repeat', repeat
        
        dna_list_copy_copy = dna_list_copy[:]
        
        for di, dna in enumerate(dna_list_copy_copy):
            # Try to match with other dna
            for dj, other_dna in enumerate(dna_list_copy_copy):
                if di >= dj:
                    continue
                
    #            if dj != 1:
    #                continue
                
                for dx, other_dna_tmp in enumerate([other_dna, flip(other_dna), reverse(other_dna), flip(reverse(other_dna))]):  
                    
    #                if dx != 0:
    #                    continue
                        
                    compatible = check_compatible(dna, other_dna_tmp)
                        
                    if compatible:
                        
                        length = len(compatible[0])
                        print "{} to {}{} Length {}, Size Reduction {}%\n".format(di, dj, altered_flag[dx], length, 100*(length+0.0)/(len(other_dna[0])+len(dna[0])))
                        print_tuple(compatible)
                        
                        dna_list_copy.append(compatible)
                    
        #check
        for dna in dna_list_copy:
            if check_complete(dna):
                print "Oh my god we're done"
                print_tuple(dna)
                raise